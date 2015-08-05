import re

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox_short.txt"
try:
	fh = open(fname)
except:
	print "Cannot open file",fname
	exit()

dictionary = dict()
for line in fh:
	hour_list = re.findall('^From .*[0-9] ([0-9]+):[0-9]+:[0-9]+.*', line)
	if len(hour_list) == 1:
		hour = hour_list[0]
		dictionary[hour] = dictionary.get(hour, 0) + 1

lst = dictionary.items();
lst.sort()

for time,count in lst:
	print time,count