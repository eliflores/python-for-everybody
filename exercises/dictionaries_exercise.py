fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox_short.txt"
try:
	fh = open(fname)
except:
	print "Cannot open file",fname
	exit()

dictionary = dict()
for line in fh:
	if line.startswith('From '):
		words = line.split()
		email_address = words[1]
		dictionary[email_address] = dictionary.get(email_address, 0) + 1

largest = None
for key,value in dictionary.items():
	if (value > largest):
		largest = value
		email_address_with_most_lines = key

print email_address_with_most_lines, largest