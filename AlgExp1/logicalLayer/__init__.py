import time
import sys
import math
import decimal
from functools import lru_cache

fibGloCounter = 0

# 递归

@lru_cache(maxsize=1024)
def Fibonacci_Recursion_tool(n):
    global fibGloCounter
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibGloCounter = fibGloCounter + 1
        return (Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2))


def Fibonacci_Recursion_tool_slow(n):
    global fibGloCounter
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibGloCounter = fibGloCounter + 1
        return (Fibonacci_Recursion_tool_slow(n - 1) + Fibonacci_Recursion_tool_slow(n - 2))

def demoFibonacci_Recursion_tool(i):
    global fibGloCounter
    res = {
        "name": 3,
        "resVal": 0.0,
        "optNum": 0,
        "time": 0.0,
    }
    t0 = time.perf_counter()
    fibGloCounter = 0
    res["resVal"] = Fibonacci_Recursion_tool(i)
    t1 = time.perf_counter()
    res["time"] = t1 - t0
    res["optNum"] = fibGloCounter
    return res


def multi(a, b):  # 计算二阶矩阵的相乘
    c = [[0, 0], [0, 0]]  # 定义一个空的二阶矩阵
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
    return c


def fib_matrix(n, counter):
    base = [[1, 1], [1, 0]]
    ans = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            counter = counter + 8
            ans = multi(ans, base)
        counter = counter + 8
        base = multi(base, base)
        n >>= 1
    return ans[0][1], counter


def demofib_matrix(i):
    res = {
        "name": 5,
        "resVal": 0.0,
        "optNum": 0,
        "time": 0.0,
    }
    t0 = time.perf_counter()
    counter_matrix = 0
    res["resVal"], res["optNum"] = fib_matrix(i, counter_matrix)
    t1 = time.perf_counter()
    res["time"] = t1 - t0
    return res


# 递归法求系统环境最大斐波那契数列
def maxNumFib():
    # 将要返回的数据
    res = {
        "index": 0,
        "time": 0.0
    }
    t0 = time.perf_counter()
    for num in range(100000):
        fnum = Fibonacci_Recursion_tool(num)
        # print("第", str(num), "个数的值为：", str(fnum))
        if fnum >= sys.maxsize:
            res['index'] = num
            # print("最大值为：", str(fnum))
            break
    t1 = time.perf_counter()
    # print('运行的时间长度为：' + str(t1 - t0))
    res['time'] = t1 - t0
    return res


# 1分钟递归求系统最大支持值接口
# 用户输入的数值
def oneMinFib(num):
    res = {
        "finish": 0,
        "time": 0.0
    }
    t0 = time.perf_counter()
    Fibonacci_Recursion_tool(num)
    t1 = time.perf_counter()
    # print('运行的时间长度为：' + str(t1 - t0))
    timeRes = t1 - t0
    res['time'] = timeRes
    if (timeRes <= 60):
        # print("递归可以在1分钟内完成求解")
        res['finish'] = 0
    else:
        # print("递归不可以在1分钟内完成求解")
        res['finish'] = 1
    return res


def thirtyMinFib():
    nameArr = {
        "index": 0,
        "time": 0.0,
        "name": 2
    }
    for num in range(100000000):
        print("num 为 " + str(num))
        t1 = time.perf_counter()
        Fibonacci_Recursion_tool_slow(num + 1)
        t2 = time.perf_counter()
        print(t2 - t1)
        if (t2 - t1) > 30:
            break
    print("30秒内最大数为：", str(num - 1))
    print("计算下一个数的时间为：", str(t2 - t1), "s")
    nameArr["index"] = num - 1
    nameArr["time"] = t2 - t1
    print(nameArr)
    return nameArr


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
    if (num <= 0):
        return 0
    if (num == 1) or (num == 2):
        return 1
    first = 0
    second = 1
    third = 0
    for i in range(2, num + 1):
        count = count + 1
        third = first + second
        first = second
        second = third
    t2 = time.perf_counter()
    print("操作次数：" + str(count))
    # print("使用迭代法运行递归斐波那契数列的计算结果: " + str(third))
    # print("使用迭代法运行递归斐波那契数列程序的运行时间为: " + str(t2 - t1))
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
    if (num > 1):
        b = 1
        num = num - 1
        a = num & 1
        num = num / 2
        num = num - 1
        while (num >= 0):
            a = a + b
            count = count + 1
            b = b + a
            count = count + 1
            num = num - 1
        t2 = time.perf_counter()
        # print("操作次数：" + str(count))
        # print("使用迭代法改进法运行递归斐波那契数列的计算结果: " + str(b))
        # print("使用迭代改进法运行递归斐波那契数列程序的运行时间为: " + str(t2 - t1))
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
    x = 1 / math.sqrt(5)
    y = (math.sqrt(5) + 1) / 2
    z = (math.sqrt(5) - 1) / 2
    result = x * (y ** num - z ** num)
    t2 = time.perf_counter()
    # print("操作次数：" + str(num - 2))
    # print("使用通项公式法改进法运行递归斐波那契数列的计算结果: " + str(result))
    # print("使用通项公式法运行递归斐波那契数列程序的运行时间为: " + str(t2 - t1))
    res['optNum'] = num - 2
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
    # print("利用迭代算法寻找不超过编程环境能够支持的最大整数的斐波那契数是第 " + str(num), "个斐波那契数")
    # print("运行时间为: " + str(t2 - t1))
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
        if (t2 - t1) > 30:
            nextfnum = first + second
            t3 = time.perf_counter()
            break
    # print("利用迭代法求不超过30s的最大斐波那契整数是第" + str(num), "个斐波那契数")
    # print("计算出下一个斐波那契数的时间是：" + str(t3 - t1))
    nameArr['index'] = num
    nameArr['time'] = t3 - t1
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
        if (decimal.Decimal(result) - decimal.Decimal(result1) >= 1):
            # print("出现误差的最小n值为：" + str(i))
            res['num'] = i
            return res
