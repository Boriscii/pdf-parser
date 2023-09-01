from convertor import Converter

SCANNED_FILE = './docs/scanned.pdf'
TEXTUAL_FILE = './docs/textual.pdf'
INVOICE = './docs/invoice.pdf'
DOCX_FILE = 'test.docx'

def runTextract():
  print('Document re-routed for Textract processing')

# convert pdf to docx

cv = Converter(INVOICE)
is_textual = cv.parse(**cv.default_settings)

if is_textual:
  cv.make_docx(DOCX_FILE)
else:
    # LIKELY A SCANNED DOCUMENT / HANDWRITING
  runTextract()



cv.close()