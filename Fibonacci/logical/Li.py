import time
import sys
from functools import lru_cache
@lru_cache(maxsize=1024)


# 递归
def Fibonacci_Recursion_tool(n):
    global counter_recursion
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        counter_recursion = counter_recursion + 1
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

def demoFibonacci_Recursion_tool()
    i = int(input('请输入求第几个斐波那契数：'))
    t0 = time.perf_counter()
    counter_recursion = 0
    print('结果为：' + str(Fibonacci_Recursion_tool(i,)))
    t1 = time.perf_counter()
    print('运行的时间长度为：' + str(t1 - t0))
    print('基本操作的次数：' + str(counter_recursion))

counter_matrix = 0

def multi(a,b):  # 计算二阶矩阵的相乘
    global counter_matrix
    c=[[0,0],[0,0]]  # 定义一个空的二阶矩阵
    counter_matrix = counter_matrix + 8
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):  # 新二阶矩阵的值计算
#                 counter_matrix = counter_matrix + 1
#                 c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c


def fib_matrix(n):
    base=[[1,1],[1,0]]
    ans=[[1,0],[0,1]]
    while n:
        if n&1:
            ans=multi(ans,base)
        base=multi(base,base)
        n>>=1
    return ans[0][1]


def demofib_matrix():
    i = int(input('请输入求第几个斐波那契数：'))
    t0 = time.perf_counter()
    print('结果为：' + str(fib_matrix(i)))
    t1 = time.perf_counter()
    print('运行的时间长度为：' + str(t1 - t0))
    print('基本操作的次数：' + str(counter_matrix))

def maxNumFib():
    t0 = time.perf_counter()
    for num in range(100000):
        fnum=Fibonacci_Recursion_tool(num)
        print("第",str(num),"个数的值为：",str(fnum))
        if fnum >= sys.maxsize:
            print("最大值为：",str(fnum))
            break
    t1 = time.perf_counter()
    print('运行的时间长度为：' + str(t1 - t0))
    
def oneMinFib():    
    t0 = time.perf_counter()
    Fibonacci_Recursion_tool(num)
    t1 = time.perf_counter()
    print('运行的时间长度为：' + str(t1 - t0))
    if (t1-t0<=60):
        print("递归可以在1分钟内完成求解")
    else:
        print("递归不可以在1分钟内完成求解")
        
def thirtyMinFib():
    for num in range(100000000):
        t1 = time.perf_counter()
        Fibonacci_Recursion_tool(num)
        t2 = time.perf_counter()
        if (t2-t1) > 30:
            break
    print("30秒内最大数为：",str(num-1))
    print("计算下一个数的时间为：",str(t2-t1),"s")
