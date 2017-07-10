import sys
x=int(sys.argv[1])
fact=1
for i in range(1,x+1):
	fact=fact*i
print "Factorial is:" +str(fact)