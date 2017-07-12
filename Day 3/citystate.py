d={'mumbai':'maharashtra','jaipur':'rajasthan','ahmedabad':'gujarat'}
print "please enter city or state:"
ip=raw_input()
for c, s in d.items():
	if ip==s:
		print c
print d.keys()[d.values().index(str(raw_input("Enter a state:")))]