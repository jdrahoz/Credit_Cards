
# ------------------------------------------- #
#
# file: main.py
# author: julia drahozal
#
# run credit card agreement analysis
#
# ------------------------------------------- #

# include files
from match import runMatch
from convert import runConversion
from search import runBasicSearch
from search import runAdvancedSearch
from search import runInternalSearch
from save import runSave
from helper import *
from constants import *

# ------------------------------------------- #

# run main program
def run ():

	# set up variables
	logging.basicConfig (filename=NAME_LOGGING, format="%(message)s")
	logging.warning (LOG_INTRO_MSG);
	print TXT_INTRO_MSG
	agmts = []

	# loop through directories
	print TXT_ANALYSIS_MSG

	for d in getSubDir (FILESYS_AGMTS):
		d_path = getPath (FILESYS_AGMTS, d)
		agmt_num = 0

		# run matching
		bank_master = runMatch (cleanApostrophes (d))

		# loop through pdfs
		if (isDir (d_path)):
			for f in getSubDir (d_path):
				f_path = getPath (d_path, f)
				if (isPdf (f_path)):

					# set up variables
					agmt_num += 1
					agmt = []
					agmt.insert (NUM_INST_NAME, cleanApostrophes (d))
					agmt.insert (NUM_AGMT_NUM, agmt_num)
					agmt.insert (NUM_AGMT_NAME, getPrintableTxtName(f))
					agmt.insert (NUM_STATUS_CONV, STATUS_PENDING)
					agmt.insert (NUM_STATUS_SEARCH, STATUS_PENDING)
					agmt.insert (NUM_INST_MATCH_NAME, bank_master)
					agmt.insert (NUM_STATUS_COMP, STATUS_PENDING)

					# run conversion
					if (toConvert (f_path)):
						if (runConversion (f_path)):
							agmt[NUM_STATUS_CONV] = STATUS_CONV_SUCCESS
						else:
							agmt[NUM_STATUS_CONV] = STATUS_CONV_FAILED
							agmt[NUM_STATUS_SEARCH] = STATUS_UNKNOWN
							agmt[NUM_STATUS_COMP] = STATUS_UNKNOWN
					else:
						agmt[NUM_STATUS_CONV] = STATUS_CONV_SUCCESS

					# run search
					if (toSearch (f_path)):

						# run basic search
						if (runBasicSearch (getTxtName (f_path))):
							agmt[NUM_STATUS_SEARCH] = STATUS_SEARCH_FOUND

							# run advanced search
							if (bank_master != ""):
								agmt[NUM_STATUS_COMP] = runAdvancedSearch (getTxtName (f_path), bank_master);

							# run internal comparison search
							if (agmt_num == 1 and sum ([len (f) for r, d, f in os.walk (d_path)]) > 2):
								runInternalSearch (d_path)

						else:
							agmt[NUM_STATUS_SEARCH] = STATUS_SEARCH_NOT_FOUND
							agmt[NUM_STATUS_COMP] = STATUS_NA

					# add to list
					agmts.append (agmt)

	# run save
	print TXT_SAVE_MSG
	runSave (agmts)
	print TXT_EXIT_MSG

# ------------------------------------------- #

# reset ()
run ()

# ------------------------------------------- #
