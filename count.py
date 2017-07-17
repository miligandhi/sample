"""""
import collections
ip=raw_input("Enter string:")
results =collections.Counter(ip)
print results

"""""
ip=raw_input("Enter string:")
print dict(map(lambda letter:(letter,len(ip)-len(ip.replace(letter,''))),ip))