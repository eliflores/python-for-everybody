import re
fname = raw_input("Enter file name: ")
if len(fname) < 1 : 
	fname = "mbox_short.txt"

fh = open(fname)

count = 0
for line in fh:
	if re.search('^From ', line):
		words = line.split()
		print words[1]
		count = count + 1

print "There were", count, "lines in the file with From as the first word"