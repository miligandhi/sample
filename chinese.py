try:
	heads=int(raw_input("Number of heads:"))
	legs=int(raw_input("Number of legs:"))
	for rabbits in range(heads+1):
		chickens=heads-rabbits
		if 2*chickens +4*rabbits==legs:
			print "Number of chickens are " + str(chickens) + " and Number of rabbits are " + str(rabbits)
except ValueError:
	print "only numeric values are allowed"