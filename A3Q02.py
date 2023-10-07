h_age = int(input("Enter the age of the human: "))
n=h_age-2
d_age_1 = 10.5
if h_age == 1 :
	print("The dog's age is ",d_age_1)
elif h_age == 2 :
	print("The dog's age is ",d_age_1*2)
elif h_age>2:
	print("The dog's age is ",d_age_2+(n*4))
else:
	print("There is an error in age")
