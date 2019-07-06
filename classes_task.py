print ("\tWelcome to HR Pro 2019 \n")

from datetime import datetime

class Employee:
	def __init__(self, name, age, salary, employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
	def get_working_years(self):
		today = datetime.now()
##							^^ don't forget the paranthesis!
		current_year = today.year
		return current_year - int(self.employment_date)
##								   ^^Always remember to call on 'self' in a class!


class Manager(Employee):
#				^^^^ this means that the Manager class will inherit from the Employee class
	def __init__(self, name, age, salary, employment_date, bonus_percentage):
		super (self, name, age, salary, employment_date, bonus_percentage)
		self.bonus_percentage = bonus_percentage
#this line will call the init method of the parent (i.e Employee) class defined above.
#So that we dont have to trouble ourselves writing all the #code below in lines 26-29
#		self.name = name
#		self.age = age
#		self.salary = salary
#		self.employment_date = employment_date

	def get_bonus(self):
		return float(self.bonus_percentage) * int(self.salary)


Employees_List = []

Managers_List = []

print ("\tChoose an action to do: \n\t\t1. Show Employees\n\t\t2. Show Managers\n\t\t3. Add An Employee\n\t\t4. Add a Manager\n\t\t5. Exit\n")
# These are the options displayed to the user to choose from
action = ""
while action != "5":
	action = input("What would you like to do? ")
	if action == "5":
		break
	
	elif action == "1":
		print ("-----------------")
		print ("Employees")
#		if len(Employees_List) == 0   <----- to check if the list is empty! then you 
# can prompt the user for an entry to the list :)
		for q in Employees_List:
			print ("Name: %s, Age: %s, Salary: %s, Working Years %s" %(q.name, q.age, q.salary, q.get_working_years()))

		print ("-----------------")
	
	elif action == "2":
		print ("-----------------")
		print ("Managers")
		for q in Managers_List:
			print ("Name: %s, Age: %s, Salary: %s, Working Years %s, Bonus: %s" %(q.name, q.age, q.salary, q.get_working_years(), q.get_bonus()))
		print ("-----------------")		

	elif action == "3":
		print ("-----------------")
		print ("Please enter the details of the employee you'd like to add to the employee list")
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_year = input("Employment Year: ")

		employee = Employee (name, age, salary, employment_year)
#this line here will create a new 'employee' object that will have the name, age, salary, employment year that the user inputs/types
		Employees_List.append(employee)
#this line will add the new employee entry by the user to the Employee_List 
	elif action == "4":
		print ("-----------------")
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_year = input("Employment Year: ")
		bonus_percentage = input("Bonus Percentage: ")

		manager = Employee (name, age, salary, employment_year, bonus_percentage)
#this line here will create a new 'employee' object that will have the name, age, salary, employment year that the user inputs/types
		Managers_List.append(manager)

	print ("\tChoose an action to do: \n\t\t1. Show Employees\n\t\t2. Show Managers\n\t\t3. Add An Employee\n\t\t4. Add a Manager\n\t\t5. Exit\n")

#	action = input("What would you like to do? ")