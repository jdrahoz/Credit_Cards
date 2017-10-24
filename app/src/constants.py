
# ------------------------------------------- #
#
# file: constants.py
# author: julia drahozal
#
# any shared constants
#
# ------------------------------------------- #

# include libraries
import datetime

FILESYS_AGMTS = 	"../agmts_2016"
FILESYS_ARBS = 		"../arbs"
FILESYS_NEW_ARBS = 	FILESYS_ARBS + "/arbs_2016"

# ------------------------------------------- #

NAME_SS_WB =		"../arb.xls"
NAME_SS_WS = 		"phase 1"

NAME_MASTER_SS = 	"../master_spreadsheet.xlsx"

NAME_LOGGING =		"../conversion.log"

# ------------------------------------------- #

TXT_SEARCH = "arbitr"
NAME_MASTER_END = ".2009.txt"
TIMEOUT_DURATION = 5

# ------------------------------------------- #

STATUS_PENDING = 			"PENDING"
STATUS_UNKNOWN =			"UNKNOWN"
STATUS_NA =					"N/A"

STATUS_CONV_SUCCESS = 		"OK"
STATUS_CONV_FAILED = 		"FAILED"

STATUS_SEARCH_FOUND = 		"FOUND"
STATUS_SEARCH_NOT_FOUND = 	"NOT FOUND"

STATUS_COMP_SAME =			"SAME"
STATUS_COMP_DIFF = 			"DIFFERENT"
STATUS_COMP_NONE_PRIOR =	"NONE PRIOR"

# ------------------------------------------- #

NUM_INST_NAME = 		0
NUM_AGMT_NUM = 			1
NUM_AGMT_NAME = 		2
NUM_STATUS_CONV = 		3
NUM_STATUS_SEARCH = 	4
NUM_INST_MATCH_NAME = 	5
NUM_STATUS_COMP = 		6

# ------------------------------------------- #

TXT_INST_NAME = 		"Institution"
TXT_AGMT_NUM = 			"#"
TXT_AGMT_NAME = 		"Agreement"
TXT_STATUS_CONV = 		"Converted"
TXT_STATUS_SEARCH = 	"Searched"
TXT_INST_MATCH_NAME = 	"Institution Match"
TXT_STATUS_COMP = 		"Comparison"

# ------------------------------------------- #

COLOR_CONV_FAILED = 	"coral"
COLOR_SEARCH_FOUND = 	"aqua"
COLOR_NEW_INST =		"bright_green"

# ------------------------------------------- #

WIDTH_INST_NAME = 		50
WIDTH_AGMT_NUM = 		5
WIDTH_AGMT_NAME = 		75
WIDTH_STATUS_CONV = 	15
WIDTH_STATUS_SEARCH = 	15
WIDTH_STATUS_COMP = 	15

# ------------------------------------------- #

FONT_HEADER_SIZE = 	12
FONT_HEADER_BOLD = 	True
FONT_BODY_SIZE = 	11

# ------------------------------------------- #

TXT_INTRO_MSG = """
--------------------------
  CREDIT CARD AGREEMENTS

   julia drahozal, 2017
--------------------------

starting ...
"""

TXT_ANALYSIS_MSG = """
running conversions & analysis
"""

TXT_SAVE_MSG = """
saving to spreadsheet
"""

TXT_EXIT_MSG = """
exiting ...

--------------------------
"""

# ------------------------------------------- #

LOG_TIME = datetime.datetime.now ().strftime ("%Y-%m-%d %H:%M")

LOG_INTRO_MSG = """
@ """ + LOG_TIME + """
--------------------------
CREDIT CARD AGREEMENTS
--------------------------"""

LOG_CONV_SUCCESS = """
CONVERTED:
	%s
	%s"""

LOG_CONV_FAILED_PDF = """
CONVERSION FAILED - text extraction error
	%s
	%s"""

LOG_CONV_FAILED_TIMEOUT = """
CONVERSION FAILED - timed out
	%s
	%s """

LOG_SEARCH_FOUND = """
ARBITRATION CLAUSE FOUND!
	%s
	%s"""

# ------------------------------------------- #
