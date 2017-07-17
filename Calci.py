class Calci:
	def ip(self):
		try:	
			print "Enter number: "
			x=raw_input()
			return float(x)
		except ValueError, Argument:
			print "The argument does not contain numbers \n", Argument

	def add(self,x,y):
		z=x+y
		print "Sum of "+str(x)+ " and " +str(y)+ " is " + str(z)+". \n"

	def sub(self,x,y):
		z=x-y
		print "Difference between "+str(x)+ " and " +str(y)+ " is " + str(z)+".\n"

	def mul(self,x,y):
		z=x*y
		print "Product of "+str(x)+ " and " +str(y)+ " is " + str(z)+".\n"

	def div(self,x,y):
		z=int(x/y)
		z1=x%y
		print "Division of "+str(x)+ " and " +str(y)+ " gives " + str(z)+" as quotient and "+str(z1)+" as remainder.\n"


print "My Calculator"	
e=1
obj=Calci()
while e<>0:
	print "Select the operation"
	print "\n1.Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5.Exit"
	choice=int(raw_input())
	if choice==1:
		x=obj.ip()
		y=obj.ip()
		obj.add(x,y)
		e=1
	elif choice==2:
		x=obj.ip()
		y=obj.ip()
		obj.sub(x,y)
		e=1
	elif choice==3:
		x=obj.ip()
		y=obj.ip()
		obj.mul(x,y)
		e=1
	elif choice==4:
		x=obj.ip()
		y=obj.ip()
		try:
			obj.div(x,y)
		except ZeroDivisionError:
			print "Division by zero is not possible"
		finally:
			x=obj.ip()
			y=obj.ip()
			obj.div(x,y)
		e=1
	elif choice==5:
		print "Thank you for using my calculator."
		e=0
	else:
		print "Wrong Choice! Please try again"
		e=1