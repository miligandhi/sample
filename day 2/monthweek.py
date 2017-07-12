import string
month=['january','february','march','april','may','june','july','august','september','october','november','december']
week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
ch=1
while ch==1 or ch==2:
	print "Enter your choice: \n 1. Month \n 2. Day of the week \n 3. Exit"
	ch=int(raw_input())
	if ch==1:
		print "Enter name of the month: "
		m=str(raw_input())
		if m.isalpha():
			while len(m)<=4:
				print "please enter full forms."
				print "Enter name of the month: "
				m=str(raw_input())
			print m+" is the month " + str(month.index(m.lower())+1) + " of the year."
	if ch==2:
		print "Enter day of the week: "
		w=str(raw_input())
		if w.isalpha():
			while len(m)<=4:
				print "please enter full forms."
				print "Enter name of the week: "
				w=str(raw_input())
			print w+" is the day " + str(week.index(w.lower())+1) + " of the week."
		
