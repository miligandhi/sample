m=int(input("Enter m: "))
n=int(input("Enter n: "))
str1=""
for row in range(1,m+1):
	for column in range(1,n+1):
		if (row==1 or row==m):  
			if(column==1 or column==n):
				str1=str1+" "
			else:
				str1=str1+"*"
		if (row>=2 and row<=(m/2)):
			if(column==1):
				str1=str1+"*"
			else: 
				str1=str1+" "
		if (row==(m/2)+1):
			if(column==1 or (column>n/2 and column<=n)):
				str1=str1+"*"
			else:
				str1=str1+" "
		if (row>(m/2)+1 and row<m):
			if(column==1 or column==n):
				str1=str1+"*"
			else:
				str1=str1+" "
	str1=str1+"\n"  
print str1
