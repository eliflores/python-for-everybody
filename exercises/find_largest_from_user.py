largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done": 
		break
	try:
		num = int(num)
	except:
		print('Invalid input')
		continue
	if num > largest:
		largest = num
	if smallest is None:
		smallest = num
	elif num < smallest:
		smallest = num
print "Maximum is",largest
print "Minimum is",smallest