#!/usr/bin/python3.5

import sys
import csv
import pickle

# value at index 0 is the file name
inputArgs=sys.argv[1:]
for arg in inputArgs:
	key,value=arg.split('=',1)
	if (key.lower()=="-csv") or (key.lower()=="--csv"):
		csvFile=value
	elif (key.lower()=="-file") or (key.lower()=="--file"):
		serializedObjectFile=value

try:
	csvFile
	try:
		csvFile=open(csvFile)
	except FileNotFoundError:
		print("%s does not exist" % csvFile)
		exit()
	
	serializedObjectFile
	try:
		serializedObjectFile=open(serializedObjectFile,'wb')
	except OSError:
		print("could not open \"%s\"" % serializedObjectFile)
		exit()
except NameError:
	print("Usage: %s --csv=inputFile --file=outputFile" % sys.argv[0])
	exit()

List=list()
isHeader=True
for row in csv.reader(csvFile):
	#ignores the header of the CSV file
	if isHeader:
		isHeader=False
		continue
	# some hex values that contain 'E' are interpreted as floating point numbers
	List.append(list([row[1].replace('.','').replace('+',''),row[2]]))

pickle.dump(List,serializedObjectFile)

csvFile.close()
serializedObjectFile.flush()
serializedObjectFile.close()
