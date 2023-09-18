import fitz
from langchain import text_splitter
import tiktoken

TOKEN_LIMIT = 800
enc = tiktoken.get_encoding('cl100k_base')

def count_tokens(text: str) -> int:
    return len(
        enc.encode(
            text,
        )
    )

splitter = text_splitter.RecursiveCharacterTextSplitter(separators=["\n", ".", " ", ""],
                                                        chunk_size=TOKEN_LIMIT,
                                                        chunk_overlap=TOKEN_LIMIT / 10,
                                                        length_function=count_tokens
)



SCANNED_FILE = './docs/scanned.pdf'
TEXTUAL_FILE = './docs/textual.pdf'
INVOICE = './docs/invoice.pdf'
DOCX_FILE = 'test.docx'

def runTextract():
  print('Document re-routed for Textract processing')

def is_text_page(fitz_page):
  return True

doc = fitz.Document('./docs/textual.pdf')
all_doc = []

for page in doc.pages():
  if not is_text_page(page):
    runTextract()
    break

  all_doc.append(page.get_text())
  print(page.get_text())

# SHOULD NOT HAPPEN IF PROCESSING WAS BROKEN, MAYBE USE A FLAG?
text = "\n".join(all_doc)
chunks = splitter.split_text(text)
print([len(chunk.split(' ')) for chunk in chunks])
print(chunks[1])

doc.close()