# pairingScript

This is a python script meant to pair students for pair programming.

It accomplishes that by gathering their names from the submitted files
of their assignments and then using that to randomly pair them together.

The resulting pairings are outputed as a csv file.

If there is an odd number of student submissions, the leftover student
will be added at the end without a pair, to be dealt with manually.

# Example Usage

Give all info as arguments
python pairingScript.py path/To/Folder/With/Submissions pathForNew/CSVfile.csv

Only give path to submissions
python pairingScript.py path/To/Folder/With/Submissions

Give nothing as argument, you will be prompted about the submissions folder
python pairingScript.py
