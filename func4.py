#!/usr/bin/python

# Recursive fibonacci for phase 4

def func4(x):
	if x <= 1 :
		return 1
	else :
		y = func4(x-1)
		z = func4(x-2)
		return y + z
		
if __name__ == "__main__":
	print func4(9)
