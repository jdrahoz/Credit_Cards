
# ------------------------------------------- #
#
# file: convert.py
# author: julia drahozal
#
# convert pdf to txt file
#
# ------------------------------------------- #

# include libraries
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfdocument import PDFEncryptionError

# include files
from helper import *
from constants import *
from timeout import *

# ------------------------------------------- #

# run conversion
def runConversion (pdf_name):

	# convert
	try:
		with Timeout (TIMEOUT_DURATION):
			convertToText (pdf_name)
		if (not toSearch (pdf_name)):
			logging.warning (LOG_CONV_FAILED_PDF % (getPrintableBankName (pdf_name), getPrintableTxtName (pdf_name)))
			return False
		else:
			logging.warning (LOG_CONV_SUCCESS % (getPrintableBankName (pdf_name), getPrintableTxtName (pdf_name)))
			return True
	except Timeout.TimeoutException:
		logging.warning (LOG_CONV_FAILED_TIMEOUT % (getPrintableBankName (pdf_name), getPrintableTxtName (pdf_name)))
		return False
	except PDFTextExtractionNotAllowed:
		logging.warning (LOG_CONV_FAILED_PDF % (getPrintableBankName (pdf_name), getPrintableTxtName (pdf_name)))
		return False
	except PDFEncryptionError:
		logging.warning (LOG_CONV_FAILED_PDF % (getPrintableBankName (pdf_name), getPrintableTxtName (pdf_name)))
		return False

# ------------------------------------------- #

# write to txt file
def convertToText (pdf_name, pages=None):

	# convert to plain text
	txt = pdfToText (pdf_name, pages=None)

	# create txt file
	if (not isEmpty (txt)):
		writer = open (getTxtName (pdf_name), "w")
		writer.write (txt)
		writer.close ()

# convert to plain text
def pdfToText (pdf_name, pages=None):

	# get number of pages
	if not pages:
		page_nums = set ()
	else:
		page_nums = set (pages)

	# set up pdf converter
	output = StringIO ()
	manager = PDFResourceManager ()
	converter = TextConverter (manager, output, laparams=LAParams ())
	interpreter = PDFPageInterpreter (manager, converter)

	# convert
	in_file = file (pdf_name, "rb")

	for page in PDFPage.get_pages (in_file, page_nums):
		interpreter.process_page (page)


	# close pdf converter
	in_file.close ()
	converter.close ()
	txt = output.getvalue ()
	output.close

	# return
	return txt

# ------------------------------------------- #
