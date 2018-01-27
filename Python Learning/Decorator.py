#!/usr/bin/env python


def auth(authType):
	def outerWrapper(func):
		def wrapper(*args, **kwargs):
			print(authType)
			func(*args, **kwargs)
		return wrapper
	return outerWrapper

def index():
	print("index")

# auth("Local Authenticated!")调用完毕后的返回值是一个函数对象，该对象继续调用home，
# 所以可以表示成 home = auth("Local Authenticated!")(home)
@auth("Local Authenticated!")   # home = auth("Local Authenticated!")(home)
def home():
	print("home")

@auth("Remote Authenticated!")	# bbs = auth("Remote Authenticated!")(bbs)
def bbs():
	print("bbs")

index()
home()
bbs()

