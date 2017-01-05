#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 2
b = 3
c = 0
#运算符
c = a + b		#5
print "1 - c 的值为：", c 
c = a - b		#-1
print "2 - c 的值为：", c 
c = a * b		#6
print "3 - c 的值为：", c 
c = a / b		#0
print "4 - c 的值为：", c 
c = a % b		#2
print "5 - c 的值为：", c
c = a ** b 		#8 幂 - 返回x的y次幂
print "6 - c 的值为：", c
c = a // b 		#0 取整除 - 返回商的整数部分
print "7 - c 的值为：", c
#比较预算符
if ( a == b ):
  print "a 等于 b"
if ( a != b ):
  print "a 不等于 b"
if ( a <> b ):
  print "a 不等于 b"
if ( a < b ):
  print "a 大 于 b"
if ( a <= b ):
  print ("a 小于等于 b")
if( a >= b ):
  print "a 大于等于 b"
#赋值运算符
c = a + b
print "1 - c 的值为：", c
c += a
print "2 - c 的值为：", c 
c *= a
print "3 - c 的值为：", c 
c /= a 
print "4 - c 的值为：", c 
c = 2
c %= a		#取模赋值运算符c %= a 等效于 c = c % a
print "5 - c 的值为：", c
c **= a		#幂赋值运算符c **= a 等效于 c = c ** a
print "6 - c 的值为：", c
c //= a		#取整除赋值运算符c//= a等效于c =c //a
print "7 - c 的值为：", c
#逻辑运算符
if ( a and b ):
  print "a 和 b 都为 true"
if ( a or b ):
  print "a 或 b 为 true"
if not ( a and b ):
  print "a 不为 true"
#成员运算符
list=[1,2,3,4,5]
if ( a in list ):
  print "a 在 list 中"
if ( a not in list ):
  print "a 不在 list 中"
#身份运算符
if ( a is not b ):
  print "1 - a 和 b 有相同的标识"






