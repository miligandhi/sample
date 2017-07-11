h_age=float(input("Input a dog's age in human years: "))
d_age=0.0
for i in range(1,int(h_age)+1):
	if i==1 or i==2:
		d_age=d_age+10.5
	else:
		d_age=d_age+4
print "The dog's age in dog's years is " +str(int(d_age))

		