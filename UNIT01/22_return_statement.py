def return_value(a):
	if a > 0:
		return a
	elif a == 0:
		return abs(a + 3)
	else:
		return -a
print(return_value(2))
print(return_value(-4))
print(return_value(0))




