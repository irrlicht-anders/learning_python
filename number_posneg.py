# Program checks wether the number is negative
# or not and displays an approbiate message

num = input("Please enter a postive or negative number! ")
a = int(num) #convert from string to int

if a >= 0:
	print("Postive or Zero")
else:
	print("Negative number")
