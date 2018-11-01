#!/usr/bin/python3.6

import threading
import time

def thr_loop(t):
	print(t)
	time.sleep(0.5)

thr_list = []

for i in range(4400):	
	t = threading.Thread(target=thr_loop, args=(i,))
	try:
		t.start()
	except RuntimeError as e:
		print("thread start error")
	thr_list.append(t)

for i in thr_list:
	try:
		i.join()
	except RuntimeError as e:
		print("thread join error")

print("thread num : %d" %len(thr_list))
print("main thread go on")
