def binary_search(a, x):
    low=0
    high=None
    if high is None:
        high = len(a)
    while low < high:
        mid = (low+high)//2
        mid_val = a[mid]
        if mid_val < x:
            low = mid+1
        elif mid_val > x: 
            high = mid
        else:
            return mid+1
    return -1

a=list()
for i in range(5):
	a.append(input())
x=int(input("Enter search number:"))
print binary_search(a,x)