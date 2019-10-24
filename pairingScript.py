import sys
import os
import re
import random
import csv

csvPath = "pairings_file.csv"

if (len(sys.argv) > 1):
	# set the folder name of submissions as the next argument when running the script
	filesPath = sys.argv[1]
else:
	filesPath = input("Please input the path to the folder of the student submissions: ")
if (len(sys.argv) > 2):
	# set the output csv file
	csvPath = sys.argv[2]

# get all file names of current folder
files = os.listdir(filesPath)

# create empty dict of student names who have submitted
names = {}

# populate the dict
for file in files:
	reResult = re.search("^[a-zæáéíóäëiöúàèììùå][a-zæáéíóäëiöúàèììùå]*", file.lower())
	if (reResult):
		studentName = reResult.group()
		names[studentName] = True

# create pairings dict
pairings = {}

# populate pairings dictionary
# there will be a leftover name in names
# if there's an odd amount of names
while (len(names) >= 2):
	choice1 = random.choice(tuple(names))
	del names[choice1]
	choice2 = random.choice(tuple(names))
	del names[choice2]
	pairings[choice1] = choice2

# write out csv file with pairings
with open(csvPath, mode = "w") as pairings_file:
	writer = csv.writer(pairings_file, delimiter = ',')
	for choice1 in pairings:
		writer.writerow([choice1, pairings[choice1]])

	if len(names) == 1:
		writer.writerow([tuple(names)[0], "No Pairing, PLEASE FIX MANUALLY!"])

# DONE
print("Done pairing students!")
