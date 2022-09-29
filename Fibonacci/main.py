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


i = int(input('请输入求第几个斐波那契数：'))
print('结果为：' + str(Fib_matrix_power(i)))

FibonacciD(7)
FibonacciDImproment(7)
FibonacciEquation(7)
