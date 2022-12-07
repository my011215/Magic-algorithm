import numpy as np

def get_bag_information():
    option = input('是否选择使用默认数据（Y/N）: ')
    if option == 'Y':
        weight = [35, 30, 60, 50, 40, 10, 25]
        price = [10, 40, 30, 50, 35, 40, 30]
        C = 150
    else:
        weight = list(map(int, input('请输入物品重量，用空格分开：').split()))
        price = list(map(int, input('请输入相应的物品价值，用空格分开： ').split()))
        C = int(input('背包容量： '))
    item = list(zip(weight, price))
    print('重量，价值：' + item.__str__() + '\n总重量限制：' + C.__str__())
    return item, C, weight

# 选重量最小的物品
def Weight(item):
    data = np.array(item)
    idex = np.lexsort([-1*data[:,1], data[:,0]])
    return idex

# 贪心算法
def GreedyAlgo(item, C, idex):
    v = [0 for _ in range(len(item))]
    w = [0 for _ in range(len(item))]
    number = len(item)
    # status = [0] * number
    total_weight = 0
    total_value = 0
    for i in range(number):
        if item[idex[i],0] <= C:
            total_weight += item[idex[i],0]
            total_value += item[idex[i],1]
            w[i] = item[idex[i], 0]
            v[i] = item[idex[i],1]
            # status[idex[i]] = 1
            C -= item[idex[i],0]
        else:
            continue
    return w, v

def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (weight, prize) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += prize
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return m

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


def solve(vlist: list, wlist: list, totalWeight: int, totalLength: int) -> int:
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


def solve2(vlist: list, wlist: list, totalWeight: int, totalLength: int) -> int:
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


def backpack(i: int, w: int, weight: list, value: list) -> int:
    if w < 0:
        return -float("inf")
    if i < 0:
        return 0
    return max(backpack(i-1, w-weight[i], weight, value)+value[i], backpack(i-1, w, weight, value))


if __name__ == '__main__':
    print(1)
    # item, C, weight = get_bag_information()
    # m = fractional_backpack(item, C)
    # print("最优解总价值：", total_v)
    # lis = list(zip(weight, m))
    # print("最优解价值列表", m)
    item0, C, weight = get_bag_information()
    # print(item0)
    item = np.array(item0)
    # print(item)
    idex_weight = Weight(item)
    w, v = GreedyAlgo(item, C, idex_weight)
    print(w)
    print(v)
    print('贪心法（重量）近似解：', w, v)







