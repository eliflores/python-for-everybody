try:
	hours = raw_input('Enter hours:')
	hours_number = float(hours)
	rate = raw_input('Enter rate:')
	rate_number = float(rate)
except:
	print('Error. Please enter numberic input')
	quit()

if hours_number > 40:
	pay = (40 * rate_number) + (hours_number - 40) * (rate_number * 1.5)
else:
	pay = hours_number * rate_number
print pay