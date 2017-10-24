
# ------------------------------------------- #
#
# file: search.py
# author: julia drahozal
#
# search txt file for arbitration
#
# ------------------------------------------- #

# include files
from helper import *
from constants import *
import sys

# ------------------------------------------- #

# run basic search for string
def runBasicSearch (txt_name):
	txt = open (txt_name).read ().lower ()
	if TXT_SEARCH in txt:
		# print TXT_SEARCH_FOUND % (getPrintableBankName (pdf_name), getPrintableTxtName (pdf_name))
		return True
	return False

# run search for master clause
def runAdvancedSearch (txt_name, bank_master):

	# build master arb clause txt file name
	master_agmt_name = bank_master.replace (" ", "_") + NAME_MASTER_END

	# check if master arb clause exists
	master_agmt_path = os.path.abspath (FILESYS_ARBS) + "/" + master_agmt_name
	if (not os.path.isfile (master_agmt_path)):
		return STATUS_COMP_NONE_PRIOR

	# get master txt
	master_reader = open (master_agmt_path, "r")
	master_clause = master_reader.read ()
	master_clause = master_clause.split ("XXXXX")
	for piece in master_clause:
		piece = stripWhitespace (piece)
	master_reader.close ()

	# get new txt
	new_reader = open (txt_name, "r")
	new_clause = new_reader.read ()
	new_clause = stripWhitespace (new_clause)
	new_reader.close ()

	# search for each piece
	found = []
	for piece in master_clause:
		if piece in new_clause:
			found.append (True)
		else:
			found.append (False)
	for piece in found:
		if (piece == False):
			return STATUS_COMP_DIFF

	return STATUS_COMP_SAME

# ------------------------------------------- #

def runInternalSearch (d):

	# set up arrays
	clauses = []
	unique_clauses = []

	# loop through agreements
	for f in getSubDir (d):
		f_path = getPath (d, f)
		if (isTxt (f_path)):

			# get txt
			reader = open (f_path, "r")
			clause = reader.read ()
			clause = stripWhitespace (clause)
			reader.close ()
			if TXT_SEARCH in clause:
				clause = clause[clause.index (TXT_SEARCH) - 20:]
				clauses.append (clause)

	# compare all clauses
	for clause in clauses:
		if clause in unique_clauses:
			continue
		else:

			# store unique clause
			unique_clauses.append (clause)
			clause_txt_name = FILESYS_NEW_ARBS + "/" + getPrintableDirName (d) + "_" + str (len (unique_clauses)) + ".txt"
			writer = open (clause_txt_name, "w")
			writer.write (clause)
			writer.close ()

	# compare unique clauses
	if (len (unique_clauses) > 1):
		for i in xrange (0, len (unique_clauses)):
			for j in xrange (i + 1, len (unique_clauses) - i):

				# get clauses
				clause_1 = unique_clauses[i]
				clause_2 = unique_clauses[j]

				# find diff
				diff = difflib.context_diff (clause_1.split (), clause_2.split (), lineterm='')
				diff_txt = '\n'.join(list(diff))

				# store diff
				diff_dir_name = FILESYS_NEW_ARBS + "/" + getPrintableDirName (d) + "_diff"
				if not os.path.exists (diff_dir_name):
					os.makedirs (diff_dir_name)
				diff_txt_name = FILESYS_NEW_ARBS + "/" + getPrintableDirName (d) + "_diff/" + str (i) + "_&_" + str (j) + ".txt"
				writer = open (diff_txt_name, "w")
				writer.write (diff_txt)
				writer.close ()

# ------------------------------------------- #
