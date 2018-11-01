#!/usr/bin/python3.6

import sys,time

print("range type:", dir(range(100)))
sys.stdout.write('[')
for i in range(100):
	sys.stdout.write('#')
	sys.stdout.flush()
	time.sleep(0.05)
sys.stdout.write(']')
