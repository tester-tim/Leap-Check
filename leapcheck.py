print('Welcome to Leap Check! This application will check to see if a year is a leap year')
user_year = int(input('Please enter the year you want to check: '))

if user_year % 4 == 0: 
	if user_year % 100 == 0:
		if user_year % 400 == 0:
			print(str(user_year) + ' is a leap year.')
		else:
			print(str(user_year) + ' is not a leap year.')
	else:
		print(str(user_year) + ' is a leap year.')
else:	
	print(str(user_year) + ' is not a leap year.')
	