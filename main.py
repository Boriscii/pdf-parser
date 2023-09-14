from convertor import Converter
from langchain import text_splitter

TOKEN_LIMIT = 3500
splitter = text_splitter.RecursiveCharacterTextSplitter(separators=["\n", ".", " ", ""]).from_tiktoken_encoder(encoding_name='cl100k_base')


SCANNED_FILE = './docs/scanned.pdf'
TEXTUAL_FILE = './docs/textual.pdf'
INVOICE = './docs/invoice.pdf'
DOCX_FILE = 'test.docx'

def runTextract():
  print('Document re-routed for Textract processing')

# convert pdf to docx

cv = Converter('./docs/order.pdf')
text = cv.parse(**cv.default_settings)

chunks = splitter.split_text(text)
print([len(chunk.split(' ')) for chunk in chunks])
print(chunks[1])

cv.close()