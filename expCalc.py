def expCalc(base, exp):
	return base + " to the power of " + exp + " equals " + int(base) ** int(exp)

getBase = raw_input("Enter the base number: ")
getExp = raw_input("Enter the exponent: ")

print expCalc(getBase, getExp)

