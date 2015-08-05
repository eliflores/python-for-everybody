fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line = line.rstrip()
	words_in_line = line.split()
	for word in words_in_line:
		if word not in lst:
			lst.append(word)

lst.sort()
print lst