# Program checks wether the number is negative
# or not and displays an approbiate message
# ------------------------------------------------
# added additional line whicht checks wether the
# input is zero OR negative

num = input("Please enter a postive or negative number! ")
a = int(num) #convert from string to int

if a > 0:
	print("Postive or Zero")
elif num == 0:
	print("Zero")
else:
	print("Negative number")
