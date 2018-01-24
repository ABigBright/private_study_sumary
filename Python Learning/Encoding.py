#!/usr/bin/python3.6

import sys

print("Default Encoding:", sys.getdefaultencoding())

s = "你好"

print("encode()'s default encoding action :", s.encode())
print("encode('gbk') encoding : ", s.encode('gbk'))
print("encode('utf-8') encoding : ", s.encode('utf-8'))
print("encode('gb2312') encoding : ", s.encode('gb2312'))
print("encode('gb18030') encoding : ", s.encode('gb18030'))
