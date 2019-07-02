print()
print()
print ("This is a simple calculator \n \n")
number1= input("Enter the first number: ")
number2= input("Enter the second number: ")

if number1.isnumeric() and number2.isnumeric():
# alternatively you can check if the input is a number using number1.isdigit() and number2.isdigit()
	operation= input("Choose the operation (+, -, /, *): ")

	total = ""
	#if operation=="+":
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
		print("The operation entered is not valid, please try again.")

	#print ("The answer is %s" % answer)
	#^^^ using this method (and line 11 where we define total as empty), saves us from repeating the same code under every if and elif

else:
	print ("One of the numbers entered is not valid, please try again.")


