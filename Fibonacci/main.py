# coding:utf-8
import math
# 迭代法求第n个斐波那契数
def FibonacciD(num):
	if(num <= 0):
		return 0
	if(num == 1) or (num == 2):
		return 1
	first = 1
	second = 1
	third = 0
	for i in range(3,num+1):
		third = first + second
		first = second
		second = third
	print(third)

# 迭代改进法求第n个斐波那契数
def FibonacciDImproment(num):
	if(num>1):
		b = 1
		num = num-1
		a = num & 1
		num = num/2
		while (num>0):
			num=num-1
			a = a+b
			b = b+a
		print(b)

# 通项公式求第n个斐波那契数/
def FibonacciEquation(num):
	x = 1/math.sqrt(5)
	y = (math.sqrt(5)+1)/2
	z = (math.sqrt(5)-1)/2
	result = x*(y**num-z**num)
	print(result)




FibonacciD(7)
FibonacciDImproment(7)
FibonacciEquation(7)