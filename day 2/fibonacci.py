a=1
b=1
s=0
print a,
print b,
while s<50:
	s=a+b
	if s<50:
		print s,
	a=b
	b=s
