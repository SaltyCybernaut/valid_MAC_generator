#!/usr/bin/python3.5

import sys
import pickle
import random
import string

#01:23:45:67:89:AB
MAC_LENGTH=12
SEP=':'

# value at index 0 is the file name
inputArgs=sys.argv[1:]
for arg in inputArgs:
	key,value=arg.split('=',1)
	if (key.lower()=="-list") or (key.lower()=="--list"):
		listName=value

try:
	listName
	try:
		listName=open(listName,'rb')
	except OSError:
		print("could not open \"%s\"" % listName)
		exit()
except  NameError:
	print("Usage: %s --list=serializedList" % sys.argv[0])
	exit()

List=pickle.load(listName)

# add loop here for multiple addresses
#--------------------------------
while True:
	manufacturer=random.randint(0,len(List)-1)
	if List[manufacturer][1].lower()!="private":
		break
validHex=List[manufacturer][0]
while len(validHex) < MAC_LENGTH:
	validHex = validHex + random.choice('0123456789ABCDEF')
#print(validHex)
print(validHex[0:2]+SEP+validHex[2:4]+SEP+validHex[4:6]+SEP+validHex[6:8]+SEP+validHex[8:10]+SEP+validHex[10:12])
#--------------------------------

listName.close()
