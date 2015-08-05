fname = raw_input("Enter file name: ")
try:
	file_handle = open(fname)
except:
	print "Cannot open file",fname
	exit()

count = 0
sum_numbers = 0
line_to_find = 'X-DSPAM-Confidence: '
line_to_find_lenght = len(line_to_find)
for line in file_handle:
	line = line.rstrip()
	if line.startswith(line_to_find): 
		count = count + 1
		number_pos = line_to_find_lenght
		number = line[number_pos:]
		sum_numbers = sum_numbers + float(number)
	
average = sum_numbers / count
print "Average spam confidence:", average