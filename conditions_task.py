print()
print()
print ("This is a simple calculator")
print()
print()
number1= input("Enter the first number: ")
number2= input("Enter the second number: ")

print ()
print ()
print ()
print ()
if number1.isnumeric() and number2.isnumeric():
	operation= input("Choose the operation (+, -, /, *): ")

	if operation=="+":
		answer = int(number1) + int(number2)
		print ("The answer is %s" % answer)
	elif operation=="-":
		answer = int(number1) - int(number2)
		print ("The answer is %s" % answer)
	elif operation=="*":
		answer = int(number1) * int(number2)
		print ("The answer is %s" % answer)
	elif operation=="/":
		answer = int(number1) / int(number2)
		print ("The answer is %s" % answer)
	else:
		print("The operation entered is not valid")


else:
	print ("One of the numbers entered is not valid")


