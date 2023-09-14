from langchain import text_splitter
import time
from lorem import paragraph

TOKEN_LIMIT = 3500
N=20000

splitter = text_splitter.RecursiveCharacterTextSplitter(separators=["\n", ".", " ", ""]).from_tiktoken_encoder(encoding_name='cl100k_base')

paragraph = next(paragraph(count=1)) + '\n'
text = paragraph * N
print('Paragraphs generated')

start_time = time.perf_counter()
chunks = splitter.split_text(text)
end_time = time.perf_counter()

runtime = end_time - start_time
word_count = len(text.split(' '))
print(f'String with {word_count} words was split in {runtime} seconds.')
print([len(chunk.split(' ')) for chunk in chunks])
print(chunks[0])