# Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
fname = raw_input("Enter file name: ")
try:
	file_handle = open(fname)
except:
	print "Cannot open file",fname
	exit()

for line in file_handle:
	line = line.rstrip()
	print line.upper()