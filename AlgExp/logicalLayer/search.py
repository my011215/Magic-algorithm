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
            arr.append(arr[i - 1] + random.randint(1, 10))
    elif pattern == 2:
        # 随机生成首元素，后面的元素依次递增随机值
        arr.append(random.randint(0, arrLen))
        for i in range(1, arrLen):
            # 负数也是整数（doge
            arr.append(arr[i - 1] - random.randint(1, 10))
    elif pattern == 3:
        # 先升后降
        # 发生大小变化的位置，必须加一，不然有可能是从第一个数或者最后一个数进行转变
        changeIndex = random.randint(1, arrLen - 1)
        arr.append(random.randint(0, arrLen))
        # 两个for循环，一个for前面的部分，另一个for后面的部分
        for i in range(1, arrLen):
            if i <= changeIndex:
                arr.append(arr[i - 1] + random.randint(1, 10))
            else:
                arr.append(arr[i - 1] - random.randint(1, 10))
    elif pattern == 4:
        # 先降后升
        # 发生大小变化的位置，必须加一，不然有可能是从第一个数或者最后一个数进行转变
        changeIndex = random.randint(1, arrLen - 1)
        arr.append(random.randint(0, arrLen))
        # 两个for循环，一个for前面的部分，另一个for后面的部分
        for i in range(1, arrLen):
            if i <= changeIndex:
                arr.append(arr[i - 1] - random.randint(1, 10))
            else:
                arr.append(arr[i - 1] + random.randint(1, 10))
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


def lomutoPartition(a: list, l: int, r: int) -> int:
    global partitionCount
    pivot = a[l]
    j = l
    for i in range(l + 1, r + 1):
        partitionCount += 1
        if a[i] < pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j


def quickSelect(a: int, l: int, r: int, k: int) -> int:
    s = lomutoPartition(a, l, r)
    if s == l+k-1:
        return a[s]
    elif s > l+k-1:
        return quickSelect(a, l, s-1, k)
    else:
        return quickSelect(a, s+1, r, k-(s-l+1))


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
    countTime = 0
    tmp = arr.copy()
    # 蛮力法
    if state == 0:
        for i in range(0, k):
            minItem = sys.maxsize
            for j in range(0, len(tmp)):
                countTime += 1
                if tmp[j] < minItem:
                    minItem = tmp[j]
            tmp.remove(minItem)
    elif state == 1:
        tmp.sort(reverse=False)
        minItem = tmp[k - 1]
        countTime = 1
    elif state == 2:
        minItem = quickSelect(tmp, 0, len(tmp) - 1, k)
        global partitionCount
        countTime = partitionCount
        partitionCount = 0
    return minItem, countTime


# 顺序查找
def sequential_search(lis, key, s):
    method1 = {
        "haveOrNot": 0,
        "compareTime": 24795171261,
        "position": 73
    }
    length = len(lis)
    count = 0
    if s == 0:
        lis = sorted(lis, reverse=False)
        for i in range(length):
            count = count + 1
            if lis[i] == key:
                method1["haveOrNot"] = 0
                # print("比较次数：" + str(count))
                method1["compareTime"] = count
                # print(lis[i])
                # print("元素所在的位置(从0开始):", i)
                method1["position"] = i
                return method1
            elif lis[i] > key:
                if i > 0:
                    method1["haveOrNot"] = 1
                    # print("比较次数：" + str(count))
                    method1["compareTime"] = count
                    # print(lis[i-1])
                    # print("小于最接近该具体元素的位置(从0开始):", i-1)
                    method1["position"] = i-1
                else:
                    method1["haveOrNot"] = 1
                    # print("比较次数：" + str(count))
                    method1["compareTime"] = count
                    # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
                    method1["position"] = -1
                return method1
        else:
            if i == length-1:
                method1["haveOrNot"] = 1
                # print(lis[i])
                # print("小于最接近该具体元素的位置(从0开始):",i)
                method1["position"] = i
            # print("比较次数：" + str(count))
            method1["compareTime"] = count
            return method1
    if s == 1:
        sorted(lis, reverse=True)
        for i in range(length):
            count = count + 1
            if lis[i] == key:
                method1["haveOrNot"] = 0
                # print("比较次数：" + str(count))
                method1["compareTime"] = count
                # print(lis[i])
                # print("元素所在的位置(从0开始):", i)
                method1["position"] = i
                return method1
            elif lis[i] < key:
                if i <= length-1:
                    method1["haveOrNot"] = 1
                    # print("比较次数：" + str(count))
                    method1["compareTime"] = count
                    # print(lis[i])
                    # print("小于最接近该具体元素的位置(从0开始):", i)
                    method1["position"] = i
                else:
                    method1["haveOrNot"] = 1
                    # print("比较次数：" + str(count))
                    method1["compareTime"] = count
                    # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
                    method1["position"] = -2
                return method1
        else:
            if i == length-1:
                method1["haveOrNot"] = 1
                method1["position"] = -2
                # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
            # print("比较次数：" + str(count))
            method1["compareTime"] = count
            return method1

# 二分查找
def binary_search(lis, key, s):
    method2 = {
        "haveOrNot": 0,
        "compareTime": 24795171261,
        "position": 73
    }
    length = len(lis)
    count = 0
    first = 0
    last = length - 1
    if s == 0:
        lis = sorted(lis, reverse=False)
        while first <= last:
            mid = (last + first) // 2
            if lis[mid] > key:
                count = count + 1
                last = mid - 1
                if last < first:
                    method2["haveOrNot"] = 1
                    method2["position"] = -1
                    # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
            elif lis[mid] < key:
                count = count + 1
                first = mid + 1
                if first > last:
                    method2["haveOrNot"] = 1
                    # print("小于最接近该具体元素的位置(从0开始):", length-1)
                    method2["position"] = length-1
                    # print(lis[length-1])
            else:
                method2["haveOrNot"] = 0
                method2["compareTime"] = count
                method2["position"] = mid
                # print("比较次数：" + str(count))
                # print(lis[mid])
                return method2
    elif s == 1:
        lis = sorted(lis, reverse=True)
        while first <= last:
            mid = (last + first) // 2
            if lis[mid] > key:
                count = count + 1
                first = mid + 1
                if first > last:
                    method2["haveOrNot"] = 1
                    method2["position"] = -2
                    # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
            elif lis[mid] < key:
                count = count + 1
                last = mid - 1
                if last < first:
                    method2["haveOrNot"] = 1
                    method2["position"] = 0
                    # print("小于最接近该具体元素的位置(从0开始):0")
                    # print(lis[0])
            else:
                method2["haveOrNot"] = 0
                method2["compareTime"] = count
                method2["position"] = mid
                # print("比较次数：" + str(count))
                # print(lis[mid])
                return method2
    method2["compareTime"] = count
    # print("比较次数：" + str(count))
    return method2

# 三分查找
count = 0
mid1 = 0
mid2 = 0
def three_search(lis, key, left, right, s):
    method3 = {
        "haveOrNot": 0,
        "compareTime": 24795171261,
        "position": 73
    }
    s = s
    global count
    global mid1
    global mid2
    #分5种情况讨论,包括3个区间，2个点
    if s == 0:
        print(left, right)
        if left >= right:
            count = count + 1
            if mid1 != mid2 and mid2 == len(lis)-1:
                method3["haveOrNot"] = 1
                method3["position"] = mid2
                print("小于最接近该具体元素的位置(从0开始):", mid2)
            elif mid1 != mid2 and mid1 == 0:
                method3["haveOrNot"] = 1
                method3["position"] = -1
                print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
            elif mid1 == mid2 and mid1 == 0:
                method3["haveOrNot"] = 1
                method3["position"] = -1
                print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
            method3["compareTime"] = count
            print("比较次数：" + str(count))
            return method3
        # 确定将区间三等分的2个点
        mid1 = (right - left) // 3 + left
        mid2 = (right - left) * 2 // 3 + left
        print(mid1)
        print(mid2)
        if lis[mid1] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid1
            method3["compareTime"] = count
            print("比较次数：" + str(count))
            return method3
        elif lis[mid2] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid2
            method3["compareTime"] = count
            print("比较次数：" + str(count))
            return method3
        elif lis[mid1] > key:
            count = count + 1
            return three_search(lis, key, left=left, right=mid1, s=0)
        elif key > lis[mid1] and key < lis[mid2]:
            count = count + 1
            return three_search(lis, key, left=mid1 + 1, right=mid2, s=0)
        else:
            return three_search(lis, key, left=mid2 + 1, right=right, s=0)
    elif s == 1:
        if left >= right:
            count = count + 1
            print(mid1, mid2)
            if mid1 != mid2 and mid1 == 0:
                method3["haveOrNot"] = 1
                method3["position"] = 0
                print("小于最接近该具体元素的位置(从0开始):0")
            elif mid1 == mid2 and mid1 == len(lis) - 1:
                method3["haveOrNot"] = 1
                method3["position"] = -2
                print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
            elif mid1 == mid2:
                method3["haveOrNot"] = 1
                method3["position"] = mid1 +1
                print("小于最接近该具体元素的位置(从0开始):",mid1+1)
            method3["compareTime"] = count
            print("比较次数：" + str(count))
            return method3
        # 确定将区间三等分的2个点
        mid1 = (right - left) // 3 + left
        mid2 = (right - left) * 2 // 3 + left
        if lis[mid1] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid1
            method3["compareTime"] = count
            print("比较次数：" + str(count))
            print(lis[mid1])
            return method3
        elif lis[mid2] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid2
            method3["compareTime"] = count
            print("比较次数：" + str(count))
            print(lis[mid2])
            return method3
        elif lis[mid1] > key:
            count = count + 1
            return three_search(lis, key, left=mid1 + 1, right=right, s=1)
        elif key > lis[mid1] and key < lis[mid2]:
            count = count + 1
            return three_search(lis, key, left=mid1 + 1, right=mid2, s=1)
        else:
            return three_search(lis, key, left=left, right=mid1, s=1)

# 插值查找
def interpolation_search(lis, key, s):
    method4 = {
        "haveOrNot": 0,
        "compareTime": 24795171261,
        "position": 73
    }
    mid = 0
    count = 0
    left = 0
    right = (len(lis) - 1)
    right1 = (len(lis) - 1)
    print(left,right,key,lis[left],lis[right])
    if s == 0:
        while left <= right and key >= lis[left] and key <= lis[right]:
            print(1)
            # Find the mid point
            mid = left + int(((float(right - left) / (lis[right] - lis[left])) * (key - lis[left])))
            # Compare the value at mid point with search value
            if lis[mid] == key:
                count += 1
                method4["haveOrNot"] = 0
                method4["position"] = mid
                method4["compareTime"] = count
                print("比较次数：" + str(count))
                return method4
            if lis[mid] < key:
                count += 1
                left = mid + 1
    elif s == 1:
        while left <= right and key <= lis[left] and key >= lis[right]:
            print(1)
            # Find the mid point
            mid = left + int(((float(right - left) / (lis[right] - lis[left])) * (key - lis[left])))
            # Compare the value at mid point with search value
            if lis[mid] == key:
                count += 1
                method4["haveOrNot"] = 0
                method4["position"] = mid
                method4["compareTime"] = count
                print("比较次数：" + str(count))
                return method4
            if lis[mid] < key:
                count += 1
                right = mid - 1
    if s == 0 and lis[0] > key:
        method4["haveOrNot"] = 1
        method4["position"] = -1
        print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
    elif s == 0 and lis[right] < key:
        print(1)
        method4["haveOrNot"] = 1
        method4["position"] = right
        print("小于最接近该具体元素的位置(从0开始):", right)
        print(lis[right1])
    elif s == 1 and key > lis[0]:
        method4["haveOrNot"] = 0
        method4["position"] = 0
        print("小于最接近该具体元素的位置(从0开始):0")
        print(lis[0])
    elif s == 1 and key < lis[right1]:
        method4["haveOrNot"] = 1
        method4["position"] = -2
        print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
    else:
        method4["position"] = mid
        print(mid)
    method4["compareTime"] = count
    print("比较次数：" + str(count))
    return method4

def get_result(result):
    if (result != False):
        print("该元素存在！")
    else:
        print("该元素不存在！")

# 二分查找求先升后降最大值
count1 = 0
def binary_search_max(lis, left, right):
    global count1
    if (left > right - 2):
        if lis[left]>lis[right]:
            count1 += 1
            max = lis[left]
        else:
            count1 += 1
            max = lis[right]
    else:
        mid = (left + right) // 2
        leftMax = binary_search_max(lis, left = left, right = mid)
        rightMax = binary_search_max(lis, left = mid + 1, right = right)
        if leftMax > rightMax:
            count1 += 1
            max = leftMax
        else:
            count1 += 1
            max = rightMax
    return max

def get_binary_search_max(lis, left, right):
    global count1
    print("binary",count1)
    method1 = {
        "position": 73,
        "compareTime": 24795171261,
    }
    max = binary_search_max(lis, left, right)
    method1["position"] = max
    method1["compareTime"] = count1
    return method1

# 二分查找求先降后升最小值
count2 = 0
def binary_search_min(lis, left, right):
    global count2
    if (left > right - 2):
        if lis[left]<lis[right]:
            count2 += 1
            min = lis[left]
        else:
            count2 += 1
            min = lis[right]
    else:
        mid = (left + right) // 2
        leftMin = binary_search_min(lis, left, mid)
        rightMin = binary_search_min(lis, mid + 1, right)
        if leftMin < rightMin:
            count2 += 1
            min = leftMin
        else:
            count2 += 1
            min = rightMin
    return min

def get_binary_search_min(lis, left, right):
    global count2
    method1 = {
        "position": 73,
        "compareTime": 24795171261,
    }
    min = binary_search_min(lis, left, right)
    method1["position"] = min
    method1["compareTime"] = count2
    return method1

# 三分查找求先升后降最大值
count3 = 0
def three_search_max(lis, left, right):
    global count3
    mid = (left + right) // 2
    if (left > right - 3):
        if lis[left]>=lis[right]:
            count3 += 1
            if lis[left]>lis[mid]:
                count3 += 1
                max = lis[left]
            else:
                count3 += 1
                max = lis[mid]
        elif lis[left]<lis[right]:
            count3 += 1
            if lis[right] > lis[mid]:
                count3 += 1
                max = lis[right]
            else:
                count3 += 1
                max = lis[mid]
    else:
        mid1 = (right - left) // 3 + left
        mid2 = (right - left) * 2 // 3 + left
        leftMax = three_search_max(lis, left = left, right = mid1)
        midMax = three_search_max(lis,left = mid1 + 1, right = mid2)
        rightMax = three_search_max(lis, left = mid2 + 1, right = right)
        if leftMax >= rightMax:
            count3 += 1
            if leftMax > midMax:
                count3 += 1
                max = leftMax
            else:
                count3 += 1
                max = midMax
        elif leftMax < rightMax:
            count3 += 1
            if rightMax>midMax:
                count3 += 1
                max = rightMax
            else:
                count3 += 1
                max = midMax
    return max

def get_three_search_max(lis, left, right):
    global count3
    print("three", count3)
    method2 = {
        "position": 73,
        "compareTime": 24795171261,
    }
    max = three_search_max(lis, left, right)
    method2["position"] = max
    method2["compareTime"] = count3
    return method2

# 三分查找求先降后升求最小值
count4 = 1
def three_search_min(lis, left, right):
    global count4
    mid = (left + right) // 2
    if (left > right - 3):
        if lis[left] <= lis[right]:
            count4 += 1
            if lis[left] < lis[mid]:
                count4 += 1
                min = lis[left]
            else:
                count4 += 1
                min = lis[mid]
        elif lis[left] > lis[right]:
            count4 += 1
            if lis[right] < lis[mid]:
                count4 += 1
                min = lis[right]
            else:
                count4 += 1
                min = lis[mid]
    else:
        mid1 = (right - left) // 3 + left
        mid2 = (right - left) * 2 // 3 + left
        leftMin = three_search_min(lis, left=left, right=mid1)
        midMin = three_search_min(lis, left=mid1 + 1, right=mid2)
        rightMin = three_search_min(lis, left=mid2 + 1, right=right)
        if leftMin <= rightMin:
            count4 += 1
            if leftMin < midMin:
                count4 += 1
                min = leftMin
            else:
                count4 += 1
                min = midMin
        elif leftMin > rightMin:
            count4+= 1
            if rightMin < midMin:
                count4 += 1
                min = rightMin
            else:
                count4 += 1
                min = midMin
    return min

def get_three_search_min(lis, left, right):
    global count4
    method2 = {
        "position": 73,
        "compareTime": 24795171261,
    }
    min = three_search_min(lis, left, right)
    method2["position"] = min
    method2["compareTime"] = count4
    return method2

if __name__ == '__main__':
# 插值查找（适用于数组分布较为均匀情况，如果中间一部分不均匀某些值会出现死循环情况）
    arr = [1,2,3,4,8,9,10,15,21,17,36,45,33,29,18]
    s = 1
    if s == 0:
        arr = sorted(arr, reverse=False)
    elif s == 1:
        arr = sorted(arr, reverse=True)
    print(arr)
    result = interpolation_search(arr, -5, s)
    print(result)
