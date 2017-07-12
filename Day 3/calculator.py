def ip_x():
	print "Enter first number: "
	x=raw_input()
	while x.isalpha():
		print "Only numbers can be used."
		print "Enter first number: "
		x=raw_input()
	return float(x)

def ip_y():
	print "Enter second number: "
	y=raw_input()
	while y.isalpha():
		print "Only numbers can be used."
		print "Enter first number: "
		y=raw_input()
	return float(y)

def add(x,y):
	z=x+y
	print "Sum of "+str(x)+ " and " +str(y)+ " is " + str(z)+". \n"

def sub(x,y):
	z=x-y
	print "Difference between "+str(x)+ " and " +str(y)+ " is " + str(z)+".\n"

def mul(x,y):
	z=x*y
	print "Product of "+str(x)+ " and " +str(y)+ " is " + str(z)+".\n"

def div(x,y):
	z=int(x/y)
	z1=x%y
	print "Division of "+str(x)+ " and " +str(y)+ " gives " + str(z)+" as quotient and "+str(z1)+" as remainder.\n"


print "My Calculator"
e=1
while e<>0:
	print "Select the operation"
	print "\n1.Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5.Exit"
	choice=int(raw_input())
	if choice==1:
		x=ip_x()
		y=ip_y()
		add(x,y)
		e=1
	elif choice==2:
		x=ip_x()
		y=ip_y()
		sub(x,y)
		e=1
	elif choice==3:
		x=ip_x()
		y=ip_y()
		mul(x,y)
		e=1
	elif choice==4:
		x=ip_x()
		y=ip_y()
		if(y==0):
			print "Wrong input, Try again (number must be greater than 0)"
			x=ip_x()
			y=ip_y()
			div(x,y)
		else:
			div(x,y)
			e=1
	elif choice==5:
		print "Thank you for using my calculator."
		e=0
	else:
		print "Wrong Choice! Please try again"
		e=1
