month = input("Enter the month's name: ").lower()
if month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
	print(month," has 31 days in it")
elif month == 'april' or month == 'june' or month == 'september' or month == 'november':
	print(month, " has 30 days in it")
elif month == 'february':
	print(month, " has 28 days in normal year and 29 days in leap year")
else :
 	print("Error") 
