#!/usr/bin/python3.6

def test1(x):
	print("test1")
	return 2

def test2(x, y, z):
	print("test2")
	return test1(x)

a = test1(1)
b = test2(1, 2, z = 3)

print(b)

a = 3
b = 4

print(a if a > b else b)

print("-------**kwargs-----------")

def test3(**kwargs):
	print(type(kwargs))

test3()

test3(a = 1,b = 2)
