import random
import sys

'''
判断数组是否有序？
参数：
1. 数组
返回值：
1. 数组状态
    - 无序 0
    - 升序 1
    - 降序 2
    - 先升后降 3
    - 先降后升 4

对judgeArr的测试 ---》 通过测试
print(judgeArr([1, 6, 1, 10, 4, 3]))
print(judgeArr([1, 2, 3, 4, 5]))
print(judgeArr([5, 4, 3, 2, 1]))
print(judgeArr([1, 2, 3, 4, 3, 2, 2, 1]))
print(judgeArr([5, 3, 2, 1, 1, 2, 3, 4]))
'''


def judgeArr(arr: list) -> int:
    length = len(arr)
    flag = []
    for i in range(0, length - 1):
        if arr[i] < arr[i + 1]:
            # 代表前面小于后面
            flag.append(1)
        elif arr[i] > arr[i + 1]:
            # 代表前面大于后面
            flag.append(0)
    # 如果去重以后的长度不是1则代表不是纯升序or降序，因为里面有0有1
    # 那么就要进一步去检查是无序or先升后降or先降后升
    if len(list(set(flag))) != 1:
        # flag[i-1]就是上一个
        changeCount = 0
        for i in range(1, len(flag)):
            if flag[i - 1] != flag[i]:
                changeCount += 1
            if changeCount > 1:
                # 变化超过一次说明是乱序的
                state = 0
                print(arr)
                print('上面的数组是乱序')
                break
        if changeCount <= 1:
            if flag[0] == 1:
                # 先升后降
                state = 3
                print(arr)
                print('上面的数组先升后降')
            else:
                state = 4
                print(arr)
                print('上面的数组先降后升')
    # 这里代表全是1or全是0
    else:
        if flag[0] == 1:
            # 代表升序
            state = 1
            print(arr)
            print('上面的数组升序')
        else:
            # 代表降序
            state = 2
            print(arr)
            print('上面的数组降序')
    return state


'''
随机生成不重复的数组
参数：
1. 数组
2. 生成的数组是什么
    - 无序 0
    - 升序 1
    - 降序 2
    - 先升后降 3
    - 先降后升 4
返回值：
1. 生成数组
备注：长度上线就是range的上线


creatArr函数测试完成 --》 通过测试

arr = creatArr(10, 0)
print(judgeArr(arr))

arr = creatArr(10, 1)
print(judgeArr(arr))

arr = creatArr(10, 2)
print(judgeArr(arr))

arr = creatArr(10, 3)
print(judgeArr(arr))

arr = creatArr(10, 4)
print(judgeArr(arr))
'''


def creatArr(arrLen: int, pattern: int) -> list:
    arr = []
    if pattern == 0:
        # 随机生成一个长度为n的整数数组，要求数组任意两个元素都互不相同随机生成一个长度为n的整数数组，要求数组任意两个元素都互不相同
        arr = random.sample(range(arrLen), arrLen)
        flag = judgeArr(arr)
        # flag的判断依据是是否为乱序，可以使用下面的judge，如果state返回值不是0，那么就重新对arr进行重排就ok
        while flag != 0:
            random.shuffle(arr)
            flag = judgeArr(arr)
    elif pattern == 1:
        # 随机生成首元素，后面的元素依次递增随机值
        arr.append(random.randint(0, arrLen))
        for i in range(1, arrLen):
            arr.append(arr[i - 1] + random.randint(0, 10))
    elif pattern == 2:
        # 随机生成首元素，后面的元素依次递增随机值
        arr.append(random.randint(0, arrLen))
        for i in range(1, arrLen):
            # 负数也是整数（doge
            arr.append(arr[i - 1] - random.randint(0, 10))
    elif pattern == 3:
        # 先升后降
        # 发生大小变化的位置，必须加一，不然有可能是从第一个数或者最后一个数进行转变
        changeIndex = random.randint(1, arrLen - 1)
        arr.append(random.randint(0, arrLen))
        # 两个for循环，一个for前面的部分，另一个for后面的部分
        for i in range(1, arrLen):
            if i <= changeIndex:
                arr.append(arr[i - 1] + random.randint(0, 10))
            else:
                arr.append(arr[i - 1] - random.randint(0, 10))
    elif pattern == 4:
        # 先降后升
        # 发生大小变化的位置，必须加一，不然有可能是从第一个数或者最后一个数进行转变
        changeIndex = random.randint(1, arrLen - 1)
        arr.append(random.randint(0, arrLen))
        # 两个for循环，一个for前面的部分，另一个for后面的部分
        for i in range(1, arrLen):
            if i <= changeIndex:
                arr.append(arr[i - 1] - random.randint(0, 10))
            else:
                arr.append(arr[i - 1] + random.randint(0, 10))
    return arr


'''
顺序算法查找元素以及关键词比较次数

形参：
1. 数组
2. 需比较元素

返回值：
1. 是否查找到元素
2. 是否进行关键词比较

测试通过
print(sequentialSearch([1,3,4,5,23,123,2],100))
print(sequentialSearch([1,3,4,5,23,123,2],5))
'''


def sequentialSearch(arr: list, item: int) -> (bool, int):
    count = 0
    for i in range(0, len(arr)):
        count += 1
        if arr[i] == item:
            return True, count
    return False, count


partitionCount = 0


def partition(nums, left, right):
    global partitionCount
    pivot = nums[left]  # 初始化一个待比较数据
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:  # 从后往前查找，直到找到一个比pivot更小的数
            j -= 1
            partitionCount += 1
        nums[i] = nums[j]  # 将更小的数放入左边
        while i < j and nums[i] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
            i += 1
            partitionCount += 1
        nums[j] = nums[i]  # 将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot  # 待比较数据放入最终位置
    return i  # 返回待比较数据最终位置


def topk_split(nums, k, left, right):
    # 寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
    if left < right:
        index = partition(nums, left, right)
        if index == k:
            return
        elif index < k:
            topk_split(nums, k, index + 1, right)
        else:
            topk_split(nums, k, left, index - 1)


'''
给定无序数组，使用多种方法(蛮力法、预排序、减可变规模)查找数组中第k个最小元素，并统计关键字比较的次数。
参数：
1. 待搜索数组
2. 第k个元素的k值
3. 搜索模式
    - 蛮力法 0
    - 预排序 1
    - 减可变规模 2
返回值：
1. 第k个最小元素
2. 关键字比较次数
'''


def threeMethodFindKMin(arr: list, k: int, state: int) -> (int, int):
    minItem = sys.maxsize
    countTime = 0
    # 蛮力法
    if state == 0:
        for i in range(0, k - 1):
            for j in range(0, len(arr)):
                countTime += 1
                if arr[j] < minItem:
                    minItem = arr[j]
            arr.remove(minItem)
        minItem = minItem(arr)
    elif state == 1:
        arr.sort(reverse=False)
        minItem = arr[k - 1]
        countTime = 1
    elif state == 2:
        topk_split(arr, k, 0, len(arr) - 1)
        minItem = arr[k]
        global partitionCount
        countTime = partitionCount
        partitionCount = 0
    return minItem, countTime
