import fitz
from langchain import text_splitter

TOKEN_LIMIT = 3500
splitter = text_splitter.RecursiveCharacterTextSplitter(separators=["\n", ".", " ", ""], chunk_size=800)\
  .from_tiktoken_encoder(encoding_name='cl100k_base')


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