def fullName(fName,lName):
	return "Name: " + lName + ", " + fName

getFirst = raw_input("Enter the first name: ")
getLast = raw_input("Enter the last name: ")

print fullName(getFirst,getLast)
