import re
email = raw_input("Enter your email ID:")
cmp = "(\w+)@(\w+)\.(com)"
cmp1 = re.match(cmp,email)
print cmp1.group(2)
