x=raw_input("Enter password")
if len(x)<6:
	print "minimum 6 characters needed"
if len(x)>16:
	print "Password can be only 16 charachters long"
a=0
A=0
n=0
s=0
for char in str(x):
	if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		A=A+1
for char in str(x):
	if char in 'abcdefghijklmnopqrstuvwxyz':
		a=a+1
for char in str(x):
	if char in '1234567890':
		n=n+1
for char in str(x):
	if char in '$#@':
		s=s+1

if a==0:
	print "Password should have atleast 1 lower case character"
if A==0:
	print "Password should have atleast 1 upper case character"
if n==0:
	print "Password should have atleast 1 numeric value"	
if s==0:
	print "Password should have atleast 1 special character from $#@"
