# coding:utf-8
import math
import time
import sys
import decimal
# 迭代法求第n个斐波那契数
def FibonacciD(num):
	res = {
		"name": 1,
		"resVal": 0.0,
		"optNum": 0,
		"time": 0.0,
	}
	count = 0
	t1 = time.perf_counter()
	if(num <= 0):
		return 0
	if(num == 1) or (num == 2):
		return 1
	first = 0
	second = 1
	third = 0
	for i in range(2,num+1):
		count = count + 1
		third = first + second
		first = second
		second = third
	t2 = time.perf_counter()
	print("操作次数：" + str(count))
	print("使用迭代法运行递归斐波那契数列的计算结果: " + str(third))
	print("使用迭代法运行递归斐波那契数列程序的运行时间为: " + str(t2 - t1))
	res['optNum'] = count
	res['resVal'] = third
	res['time'] = t2 - t1
	return res

# 迭代改进法求第n个斐波那契数
def FibonacciDImproment(num):
	res = {
		"name": 2,
		"resVal": 0.0,
		"optNum": 0,
		"time": 0.0,
	}
	count = 0
	t1 = time.perf_counter()
	if(num>1):
		b = 1
		num = num-1
		a = num & 1
		num = num/2
		num = num - 1
		while (num>=0):
			a = a+b
			count = count + 1
			b = b+a
			count = count + 1
			num = num - 1
		t2 = time.perf_counter()
		print("操作次数：" + str(count))
		print("使用迭代法改进法运行递归斐波那契数列的计算结果: " + str(b))
		print("使用迭代改进法运行递归斐波那契数列程序的运行时间为: " + str(t2 - t1))
		res['optNum'] = count
		res['resVal'] = b
		res['time'] = t2 - t1
		return res

# 通项公式求第n个斐波那契数/
def FibonacciEquation(num):
	res = {
		"name": 4,
		"resVal": 0.0,
		"optNum": 0,
		"time": 0.0,
	}
	t1 = time.perf_counter()
	x = 1/math.sqrt(5)
	y = (math.sqrt(5)+1)/2
	z = (math.sqrt(5)-1)/2
	result = x*(y**num-z**num)
	t2 = time.perf_counter()
	print("操作次数：" + str(num-2))
	print("使用通项公式法改进法运行递归斐波那契数列的计算结果: " + str(result))
	print("使用通项公式法运行递归斐波那契数列程序的运行时间为: " + str(t2 - t1))
	res['optNum'] = num-2
	res['resVal'] = result
	res['time'] = t2 - t1
	return res

# 迭代法求不超过编程环境的最大斐波那契整数
def GetFibonacciD():
	# 将要返回的数据
	res = {
		"index": 0,
		"time": 0.0
	}
	t1 = time.perf_counter()
	fnum = 0
	num = 0
	first = 0
	second = 1
	max = sys.maxsize
	for num in range(100000):
		if (num <= 0):
			fnum = 0
		if (num == 1) or (num == 2):
			fnum = 1
		fnum = first + second
		first = second
		second = fnum
		num = num + 1
		if fnum > max:
			break
	t2 = time.perf_counter()
	print("利用迭代算法寻找不超过编程环境能够支持的最大整数的斐波那契数是第 " + str(num),"个斐波那契数")
	print("运行时间为: " + str(t2 - t1))
	res['index'] = num
	res['time'] = t2 - t1
	return res

# 迭代法求不超过30s的最大斐波那契整数
def GetMaxFibonacciD():
	nameArr = {
		"index": 0,
		"time": 0.0,
		"name": 1
	}
	t1 = time.perf_counter()
	fnum = 0
	num = 0
	first = 0
	second = 1
	i = 1
	for num in range(100000000):
		if (num <= 0):
			fnum = 0
		if (num == 1) or (num == 2):
			fnum = 1
		fnum = first + second
		first = second
		second = fnum
		num = num + 1
		t2 = time.perf_counter()
		if (t2-t1) > 30:
			nextfnum = first + second
			t3 = time.perf_counter()
			break
	print("利用迭代法求不超过30s的最大斐波那契整数是第" + str(num),"个斐波那契数")
	print("计算出下一个斐波那契数的时间是：" + str(t3-t1))
	nameArr['index'] = num
	nameArr['time'] = t3-t1
	return nameArr

# 返回正确的斐波那契数
def GetFibonacciD1(num):
	if (num <= 0):
		return 0
	if (num == 1) or (num == 2):
		return 1
	first = 0
	second = 1
	third = 0
	for i in range(2, num + 1):
		third = first + second
		first = second
		second = third
	return third

# 求出现误差时的最小n值
def GetMaxFibonacci():
	res = {
		"num": 0,
	}
	for i in range(100):
		x = 1 / math.sqrt(5)
		y = (math.sqrt(5) + 1) / 2
		z = (math.sqrt(5) - 1) / 2
		result = decimal.Decimal(x) * (decimal.Decimal(y) ** i - decimal.Decimal(z) ** i)
		result = decimal.Decimal(result)
		result1 = GetFibonacciD1(i)
		if (decimal.Decimal(result) - decimal.Decimal(result1)>=1):
			print("出现误差的最小n值为：" + str(i))
			res['num'] = i
			return res
			break

if __name__ == '__main__':
	GetMaxFibonacci()
	print(1)