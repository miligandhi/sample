import sys
net = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        net+=amount
    elif operation=="W":
        net-=amount
    else:
        pass
print net