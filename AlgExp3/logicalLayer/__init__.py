import numpy as np

'''
动态规划算法求解0-1背包问题
参数：
1. vlist 价值列表
2. wlist 重量列表
3. 背包总承重
4. 物品总数量
返回值：
1. 最优结果
'''


def solve(vlist: list, wlist: list, totalWeight: int, totalLength: int) -> tuple[list, list]:
    resArr = np.zeros((totalLength + 1, totalWeight + 1), dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(1, totalWeight + 1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i - 1, j - wlist[i]] + vlist[i], resArr[i - 1, j])
            else:
                resArr[i, j] = resArr[i - 1, j]
    return resArr[-1, -1]


'''
使用记忆功能改进6中的动态规划算法
参数：
1. vlist 价值列表
2. wlist 重量列表
3. 背包总承重
4. 物品总数量
返回值：(选择的重量列表，选择的价值列表)
'''


def solve2(vlist: list, wlist: list, totalWeight: int, totalLength: int) -> tuple[list, list]:
    resArr = np.zeros(totalWeight + 1, dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(totalWeight, 0, -1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j - wlist[i]] + vlist[i])
    return resArr[-1]


'''
蛮力法算法求解0-1背包问题给定实例的最优解
参数：
1. i 一共有i种物品可以选择
2. w 背包目前的最大载重
3. weight 0-i号物品对应的重量列表
4. value 0-i号物品对应的价值列表
返回值：(选择的重量列表，选择的价值列表)
'''


def backpack(i: int, w: int, weight: list, value: list) -> tuple[list, list]:
    if w < 0:
        return -float("inf")
    if i < 0:
        return 0
    return max(backpack(i-1, w-weight[i])+value[i], backpack(i-1, w))
