hours = raw_input('Enter hours:')
rate = raw_input('Enter rate:')
hours_number = float(hours)
rate_number = float(rate)
if hours_number > 40:
	pay = (40 * rate_number) + (hours_number - 40) * (rate_number * 1.5)
else:
	pay = hours_number * rate_number
print pay