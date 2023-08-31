from convertor import Converter

SCANNED_FILE = './docs/scanned.pdf'
TEXTUAL_FILE = './docs/textual.pdf'
DOCX_FILE = 'test.docx'

def runTextract():
  print('Document re-routed for Textract processing')

# convert pdf to docx
try:
  cv = Converter(SCANNED_FILE)
  word_count = cv.parse(**cv.default_settings)

  if word_count > 50:
    cv.make_docx(DOCX_FILE)
  else:
    # LIKELY A SCANNED DOCUMENT / HANDWRITING
    runTextract()
except:
  runTextract()

cv.close()