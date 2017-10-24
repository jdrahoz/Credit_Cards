
# ------------------------------------------- #
#
# file: save.py
# author: julia drahozal
#
# store data in spreadsheet
#
# ------------------------------------------- #

# include libraries
import xlwt

# include files
from constants import *

# ------------------------------------------- #

# run save
def runSave (agmts):

	# open spreadsheet
	wb = xlwt.Workbook (encoding="latin-1")
	ws = wb.add_sheet (NAME_SS_WS)
	setColWidths (ws)

	# set up header
	header_style = getHeaderStyle ()
	ws.write (0, NUM_INST_NAME, TXT_INST_NAME, style=header_style)
	ws.write (0, NUM_AGMT_NUM, TXT_AGMT_NUM, style=header_style)
	ws.write (0, NUM_AGMT_NAME, TXT_AGMT_NAME, style=header_style)
	ws.write (0, NUM_STATUS_CONV, TXT_STATUS_CONV, style=header_style)
	ws.write (0, NUM_STATUS_SEARCH, TXT_STATUS_SEARCH, style=header_style)
	ws.write (0, NUM_INST_MATCH_NAME, TXT_INST_MATCH_NAME, style=header_style)
	ws.write (0, NUM_STATUS_COMP, TXT_STATUS_COMP, style=header_style)

	# write to spreadsheet
	row = 1
	for agmt in agmts:

		body_style = getBodyStyle ()
		if (agmt[NUM_STATUS_SEARCH] == STATUS_SEARCH_FOUND):
			body_style.font.colour_index = xlwt.Style.colour_map[COLOR_SEARCH_FOUND]
		if (agmt[NUM_INST_MATCH_NAME] == ""):
			body_style.font.colour_index = xlwt.Style.colour_map[COLOR_NEW_INST]
		if (agmt[NUM_STATUS_CONV] == STATUS_CONV_FAILED):
			body_style.font.colour_index = xlwt.Style.colour_map[COLOR_CONV_FAILED]

		ws.write (row, NUM_INST_NAME, agmt[NUM_INST_NAME], style=body_style)
		ws.write (row, NUM_AGMT_NUM, agmt[NUM_AGMT_NUM], style=body_style)
		ws.write (row, NUM_AGMT_NAME, agmt[NUM_AGMT_NAME], style=body_style)
		ws.write (row, NUM_STATUS_CONV, agmt[NUM_STATUS_CONV], style=body_style)
		ws.write (row, NUM_STATUS_SEARCH, agmt[NUM_STATUS_SEARCH], style=body_style)
		ws.write (row, NUM_INST_MATCH_NAME, agmt[NUM_INST_MATCH_NAME], style=body_style)
		ws.write (row, NUM_STATUS_COMP, agmt[NUM_STATUS_COMP], style=body_style)
		row += 1

	# save spreadsheet
	wb.save (NAME_SS_WB)

# ------------------------------------------- #

# set column widths
def setColWidths (ws):
	ws.col (NUM_INST_NAME).width = 256 * WIDTH_INST_NAME
	ws.col (NUM_AGMT_NUM).width = 256 * WIDTH_AGMT_NUM
	ws.col (NUM_AGMT_NAME).width = 256 * WIDTH_AGMT_NAME
	ws.col (NUM_STATUS_CONV).width = 256 * WIDTH_STATUS_CONV
	ws.col (NUM_STATUS_SEARCH).width = 256 * WIDTH_STATUS_SEARCH
	ws.col (NUM_INST_MATCH_NAME).width = 256 * WIDTH_INST_NAME
	ws.col (NUM_STATUS_COMP).width = 256 * WIDTH_STATUS_COMP

# format header
def getHeaderStyle ():

	# font
	header_font = xlwt.Font ()
	header_font.height = FONT_HEADER_SIZE * 20
	header_font.bold = FONT_HEADER_BOLD

	# alignment
	header_align = xlwt.Alignment ()
	header_align.horz = xlwt.Alignment.HORZ_CENTER

	# set style
	header_style = xlwt.XFStyle ()
	header_style.font = header_font
	header_style.alignment = header_align
	return header_style

# format body
def getBodyStyle ():

	# font
	body_font = xlwt.Font ()
	body_font.height = FONT_HEADER_SIZE * 20

	# set style
	body_style = xlwt.XFStyle ()
	body_style.font = body_font
	return body_style

# ------------------------------------------- #
