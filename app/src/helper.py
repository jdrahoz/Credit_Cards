
# ------------------------------------------- #
#
# file: helper.py
# author: julia drahozal
#
# any helper methods
#
# ------------------------------------------- #

# include libraries
from cStringIO import StringIO
import os
import os.path
import difflib
import logging

# include files
from constants import *

# ------------------------------------------- #

def getPath (d, x):
	return os.path.abspath (os.path.join (d, x))

def getSubDir (path):
	return os.listdir (path)

def isDir (path):
	return os.path.isdir (path)

def isPdf (path):
	return path.endswith (".pdf")

def isTxt (path):
	return path.endswith (".txt")

def getTxtName (pdf_name):
	return pdf_name[:-3] + "txt"

def getPrintableTxtName (path):
	return path.split ("/")[-1][:-4]

def getPrintableDirName (path):
	return path.split ("/")[-1].replace (" ", "_")

def getPrintableBankName (path):
	return path.split ("/")[-2]

def isEmpty (txt):
	return (len (txt) < 20)

def toConvert (pdf_name):
	return (isPdf (pdf_name) and not toSearch (pdf_name))

def toSearch (pdf_name):
 	return os.path.isfile (getTxtName (pdf_name))

# ------------------------------------------- #

# fix weird apostrophe issue
def cleanApostrophes (txt):

	newTxt = ''.join ([c if ord (c) < 128 else '\'' for c in txt])
	newTxt = newTxt.replace ("\'\'\'", "\'")
	return newTxt

def stripWhitespace (txt):
	return " ".join (txt.split ())

# ------------------------------------------- #

# delete converted pdfs
def reset (num="ALL"):
	deleted = 0
	for root, dirs, files in os.walk (FILESYS_AGMTS):
		for f in files:
			if isTxt (root + "/" + f):
				os.remove (root + "/" + f)
				deleted += 1
			if (num != "ALL"):
				if deleted == num:
					return

# ------------------------------------------- #
