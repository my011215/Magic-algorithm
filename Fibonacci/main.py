# coding:utf-8
import math
import time
import datetime
import sys
# 迭代法求第n个斐波那契数
def FibonacciD(num):
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
	print(count)
	print("使用迭代法运行递归斐波那契数列的计算结果: {}".format(third))
	print("使用迭代法运行递归斐波那契数列程序的运行时间为: {}".format(t2 - t1))

# 迭代改进法求第n个斐波那契数
def FibonacciDImproment(num):
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
		print(count)
		print("使用迭代法改进法运行递归斐波那契数列的计算结果: {}".format(b))
		print("使用迭代改进法运行递归斐波那契数列程序的运行时间为: {}".format(t2 - t1))

# 通项公式求第n个斐波那契数/
def FibonacciEquation(num):
	t1 = time.perf_counter()
	x = 1/math.sqrt(5)
	y = (math.sqrt(5)+1)/2
	z = (math.sqrt(5)-1)/2
	result = x*(y**num-z**num)
	t2 = time.perf_counter()
	print(num-2)
	print("使用通项公式法改进法运行递归斐波那契数列的计算结果: {}".format(result))
	print("使用通项公式法运行递归斐波那契数列程序的运行时间为: {}".format(t2 - t1))

# 迭代法求不超过编程环境的最大斐波那契整数
def GetFibonacciD():
	t1 = time.perf_counter()
	fnum = 0
	num = 0
	first = 0
	second = 1
	i = 1
	for num in range(100000):
		if (num <= 0):
			fnum = 0
		if (num == 1) or (num == 2):
			fnum = 1
		fnum = first + second
		first = second
		second = fnum
		num = num + 1
		if fnum > 9223372036854775807:
			break
	t2 = time.perf_counter()
	print("利用迭代算法寻找不超过编程环境能够支持的最大整数的斐波那契数是第{}".format(num),"个斐波那契数")
	print("运行时间为: {}".format(t2 - t1))

# 迭代法求不超过30s的最大斐波那契整数
def GetMaxFibonacciD():
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
			break
	print("利用迭代法求不超过30s的最大斐波那契整数是第{}".format(num),"个斐波那契数")

# 递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

# 递归
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

i = int(input('请输入求第几个斐波那契数：'))
print('结果为：' + str(Fibonacci_Recursion_tool(i)))

# 两个n阶矩阵相乘
def matrix_multiplication(n, A, B):
    C = []
    for line in range(n):
        line_arr = []
        for column in range(n):
            item = 0
            for i in range(n):
                item += A[line][i] * B[i][column]
            line_arr.append(item)
        C.append(line_arr)
    return C

# 矩阵快速幂求解，所求元素为A^{n-1} 中的 A[0][0], 或 A^n 中的 A[0][1]
def Fib_matrix_power(n):
    # 检查输入
    if n < 2: return n
    A = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    matrix_n = 2
    while n > 0:
        # 判断最后一位是否为1，即可知奇偶
        if n & 1:
            result = matrix_multiplication(matrix_n, result, A)
        A = matrix_multiplication(matrix_n, A, A)
        n //= 2
        # n = n >> 1
    return result[0][1]

# 两个n阶矩阵相乘
def matrix_multiplication(n, A, B):
    C = []
    for line in range(n):
        line_arr = []
        for column in range(n):
            item = 0
            for i in range(n):
                item += A[line][i] * B[i][column]
            line_arr.append(item)
        C.append(line_arr)
    return C

# 矩阵快速幂求解，所求元素为A^{n-1} 中的 A[0][0], 或 A^n 中的 A[0][1]
def Fib_matrix_power(n):
    # 检查输入
    if n < 2: return n
    A = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    matrix_n = 2
    while n > 0:
        # 判断最后一位是否为1，即可知奇偶
        if n & 1:
            result = matrix_multiplication(matrix_n, result, A)
        A = matrix_multiplication(matrix_n, A, A)
        n //= 2
        # n = n >> 1
    return result[0][1]

i = int(input('请输入求第几个斐波那契数：'))
print('结果为：' + str(Fib_matrix_power(i)))

if __name__ == '__main__':
	# i = int(input('请输入求第几个斐波那契数：'))
	# print('结果为：' + str(Fib_matrix_power(i)))
	# t1 = time.perf_counter()
	# # t1 = time.time()
	# print(t1)
	FibonacciD(20)
	FibonacciDImproment(20)
	FibonacciEquation(20)
	# t2 = time.perf_counter()
	# print(t2)
	# print("使用迭代法运行递归斐波那契数列程序的运行时间为: {}".format(t2 - t1))
	# FibonacciDImproment(7)
	# FibonacciEquation(7)
FibonacciD(7)
FibonacciDImproment(7)
FibonacciEquation(7)

