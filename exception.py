class NumberError(Exception):
	def __init__(self,er):
		print er
ip=raw_input("Enter a number:")
if not ip.isdigit():
	raise NumberError("Value must be an integer")