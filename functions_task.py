from datetime import datetime


#userdate=datetime.(year, month, day)
#or you can use today = datetime.now()
#birthdat

def check_birthdate(year, month, day):
	today = datetime.now()
	DOB = datetime(year, month, day)
	#DOB has to be defined here within the function so the code can recognise the paramters of year month day)
	if DOB < today:
		return True
		
	else:
		return False

def calculate_age(year, month, day):
	today = datetime.now()
	DOB = datetime(year, month, day)
#   		^^^ this recollects the 'class' imported with the library in Line 1!
	Age = today - DOB
	AgeDays = Age.days
#we do this step so that we get the 'days' 

	AgeYear = int(AgeDays/365)
	AgeDay = AgeDays%365
#this will give us number of days since (our) last birthday

	AgeMonth = int(AgeDays/30)
	AgeDays = AgeDays%30
#This line was missing in the last commit. Now updated thanks to Mshary.

	print ("You are %d years, %d months, and %d days" % (AgeYear, AgeMonth, AgeDay))



year=int(input("Please enter year of birth: "))
month=int(input("Please enter month of birth: "))
day=int(input("Please enter day of birth: "))

if check_birthdate(year, month, day) == True:
 	calculate_age(year, month, day)
else:
	print ("The birthdate entered is not valid. This is real life, not \'Back From The Future\'.")
