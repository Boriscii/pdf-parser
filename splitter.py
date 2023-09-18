from langchain import text_splitter
import time
from lorem import paragraph
import tiktoken

N=200

enc = tiktoken.get_encoding('cl100k_base')
def count_tokens(text: str) -> int:
    return len(
        enc.encode(
            text,
        )
    )

splitter = text_splitter.RecursiveCharacterTextSplitter(separators=["\n", ".", " ", ""],
                                                        chunk_size=800,
                                                        chunk_overlap=50,
                                                        length_function=count_tokens
)

paragraph = next(paragraph(count=1)) + '\n'
text = paragraph * N
print('Paragraphs generated')

start_time = time.perf_counter()
chunks = splitter.split_text(text)
end_time = time.perf_counter()

runtime = end_time - start_time
word_count = len(text.split(' '))
print(f'String with {word_count} words was split in {runtime} seconds.')
print([count_tokens(chunk) for chunk in chunks])