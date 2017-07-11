x=""
for row in range(1,8):
	for column in range(1,6):
		if row==1:
			if column>=2 and column<=4:
				x=x+"*"
			else:
				x=x+" "
		if (row in [2,3,5,6,7]):
			if column==1 or column==5:
				x=x+"*"
			else:
				x=x+" "
		if row==4:
			x=x+"*"
	x=x+"\n"
print x
	