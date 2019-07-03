print ("\n \nA simple system to assist cashiers with printing a receipt! \n \n")


shoppinglist = []

item=""

#while True:
# the above code is the same as whats below and will work too!
while item != "done":
	item = input("Please enter an item (enter \"done\" when finished): ")
	if item == "done":
		break
#^^without this line of code, the loop will continue, even when the user enters "done!"
	price = float(input("Price: "))
	quantity = int(input("Quantity: "))
	user_items = {
	"item" : item,
	"price" : price,
	"quantity" : quantity
	}
	shoppinglist.append(user_items)


print ("------------------- \nReceipt\n-------------------")

total = 0

for x in shoppinglist:
#here we redefine the List shopping list to "x"
	print ("%s %s %.3f K.D." % (x["quantity"], x["item"], x["price"]*x["quantity"]))
	total = total + x["price"]*x["quantity"]
	#
	# Keep in mind that the key in your dictionary is always a String! i.e. use ""

#total = 

print ("-------------------")
print ("Your total is: %.3f K.D." %total)

