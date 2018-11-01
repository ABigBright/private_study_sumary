#!/usr/bin/python3.6

def DividTwo(n):
	if (int(n) <= 0):
		return 0;
	print(int(n))
	return DividTwo(n/2)

DividTwo(8)

