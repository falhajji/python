print ("Welcome to the special recruitment program, please answer the following questions:")

skills = ["python", "html", "singing", "eating", "sleeping", "running"]

cv={}

name=input("What is your name? ")
cv["name"]=name

age=input("How old are you? ")
cv["age"]=age

experience=input("How many years of experience do you have? ")
cv["experience"]=experience

cv["skills"]=[]

print("Skills: ")
print("1. %s" % skills [0])
print("2. %s" % skills [1])
print("3. %s" % skills [2])
print("4. %s" % skills [3])
print("5. %s" % skills [4])
print("6. %s" % skills [5])

skill1 = input("Please choose a skill from the list above: ")
#step 8
cv["skills"].append(skills[int(skill1)-1])
# why do we subtract 1? So that we get the index of that skill

skill2 = input("Please choose another skill from the list above: ")
cv["skills"].append(skills[int(skill2)-1])

#to start defining the criteria for applicant acceptance....
#if int(cv["age"] <= 17) and int(cv["age"] <30) and (cv["skills"][0] == skills[2] or cv["skills"] ==skills[2]):
#originL attempt
if (int(cv["age"]) >= 17 and int(cv["age"]) <30) and int(cv["experience"]) >= 2 and (cv["skills"][0] == skills[0] or cv["skills"][1] ==skills[0]):
#															here we check if user inputted skill^^ is the same as criteria required (skills[0])
#
#if (int(dictionary["age"]) > 25 and int(dictionary["age"]) < 40) and int(dictionary["experience"]) > 3 and dictionary["skills"].count(wanted_skill) > 0:
#Line above is an alternate method of setting the criteria. See Mshary's message on Slack dated July 1, 2019
	print("You have been accepted, %s!" %cv["name"])
else:
	print("Sorry, you're not awesome enough to work with us")