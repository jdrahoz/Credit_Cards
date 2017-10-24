
# ------------------------------------------- #
#
# file: match.py
# author: julia drahozal
#
# match to master spreadsheet
#
# ------------------------------------------- #

# include libraries
import xlrd

# include files
from constants import *

# ------------------------------------------- #

# run match to master spreadsheet
def runMatch (bank_name_folder):

	# open spreadsheet
	wb = xlrd.open_workbook (NAME_MASTER_SS)
	ws = wb.sheet_by_index (0)

	# search bank names
	for i in xrange (ws.nrows):
		bank_name_master = ws.cell_value (rowx=i, colx=0)
		if (bank_name_master.lower () == bank_name_folder.lower ()):
			return bank_name_master

	if ("american express" in bank_name_folder.lower ()):
		return "American Express"

	return ""

# ------------------------------------------- #
