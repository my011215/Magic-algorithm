import random

'''
随机生成不重复的数组
参数：
1. 用户的选择（0 自己输入，1 系统自动生成）
2. 生成数组长度
3. 数组
返回值：
1. 生成数组
2. 是否成功,0成功，1失败
'''
def creatArr(state, arrLen, arr):
    if state == 1:
        # 随机生成一个长度为n的整数数组，要求数组任意两个元素都互不相同随机生成一个长度为n的整数数组，要求数组任意两个元素都互不相同
        arr = random.sample(range(0,100),arrLen)
        flag = 0
    else: # 说明用户自己输入的
        setArr = set(arr)
        # 判断一下是否有重复的元素，保证用户按照规定输入，满足题目需要
        if len(setArr) == len(arr):
            # 满足题目
            flag = 0
        else:
            # 不满足题目
            flag = 1
    return arr, flag

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
        if left >= right:
            count = count + 1
            if mid1 == mid2 and mid1 == len(lis)-1:
                method3["haveOrNot"] = 1
                method3["position"] = mid1
                # print("小于最接近该具体元素的位置(从0开始):", mid1)
            elif mid1 != mid2 and mid1 == 0:
                method3["haveOrNot"] = 1
                method3["position"] = -1
                # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
            method3["compareTime"] = count
            # print("比较次数：" + str(count))
            return method3
        # 确定将区间三等分的2个点
        mid1 = (right - left) // 3 + left
        mid2 = (right - left) * 2 // 3 + left
        if lis[mid1] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid1
            method3["compareTime"] = count
            # print("比较次数：" + str(count))
            # print(lis[mid1])
            return method3
        elif lis[mid2] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid2
            method3["compareTime"] = count
            # print("比较次数：" + str(count))
            # print(lis[mid2])
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
            if mid1 != mid2 and mid1 == 0:
                method3["haveOrNot"] = 1
                method3["position"] = 0
                # print("小于最接近该具体元素的位置(从0开始):0")
            elif mid1 == mid2 and mid1 == len(lis) - 1:
                method3["haveOrNot"] = 1
                method3["position"] = -2
                # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
            method3["compareTime"] = count
            # print("比较次数：" + str(count))
            return method3
        # 确定将区间三等分的2个点
        mid1 = (right - left) // 3 + left
        mid2 = (right - left) * 2 // 3 + left
        if lis[mid1] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid1
            method3["compareTime"] = count
            # print("比较次数：" + str(count))
            # print(lis[mid1])
            return method3
        elif lis[mid2] == key:
            count = count + 1
            method3["haveOrNot"] = 0
            method3["position"] = mid2
            method3["compareTime"] = count
            # print("比较次数：" + str(count))
            # print(lis[mid2])
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
    if s == 1:
        lis.sort()
    while left <= right and key >= lis[left] and key <= lis[right]:
        # Find the mid point
        mid = left + int(((float(right - left) / (lis[right] - lis[left])) * (key - lis[left])))
        # Compare the value at mid point with search value
        if lis[mid] == key:
            count += 1
            method4["haveOrNot"] = 0
            method4["position"] = mid
            method4["compareTime"] = count
            # print("比较次数：" + str(count))
            return method4
        if lis[mid] < key:
            count += 1
            left = mid + 1
    if s == 0 and lis[0] > key:
        method4["haveOrNot"] = 1
        method4["position"] = -1
        # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数比第一个数还要小！")
    elif s == 0 and lis[right] < key:
        method4["haveOrNot"] = 1
        method4["position"] = right
        # print("小于最接近该具体元素的位置(从0开始):", right)
        # print(lis[right])
    elif s == 1 and key > lis[0]:
        method4["haveOrNot"] = 1
        method4["position"] = 0
        # print("小于最接近该具体元素的位置(从0开始):0")
        # print(lis[0])
    elif s == 1 and key < lis[right]:
        method4["haveOrNot"] = 1
        method4["position"] = -2
        # print("小于最接近该具体元素的位置(从0开始)的数不存在，该数最后一个数比它还要大！")
    method4["compareTime"] = count
    # print("比较次数：" + str(count))
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
count = 4
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

# if __name__ == '__main__':
#     str = [0,1,2,3]  # 有的题目要输出字符串，但是有时候list更好操作，于是可以最后list转string提交
#     str1 = ','.join(str)
#     print(str1)
#     # 四种情况的测试数组
#     # 先升后降
#     LIST = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,78,89,99,100,19,18,17,15,12,11,10,9,2,1,0]
#     # 先降后升
#     LIST1 = [99,98,97,95,88,47,35,36,32,29,28,21,20,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,10,20,30,40,50,60,70,80,90]
#     # 升序
#     LIST2 = [-1,1,2,3,4,5,6,7,8,9,10,11,12,15,18,28,29,100]
#     # 降序
#     LIST3 = [100,99,98,97,95,92,91,78,75,54,52,51,40,30,20,10,9,8,7,6,5,3,2,1,0,-2]
#
#     LIST4 =[]
#     # 自动生成
#     lis, flag = creatArr(1, 20, LIST4)
#     # 升序
#     LIST2 = sorted(lis, reverse=False)
#     # 降序
#     LIST3 = sorted(lis, reverse=True)
#     print(flag)
#
#     # 四种查找
#
#     # 顺序查找
#     print(LIST3)
#     result = sequential_search(LIST3, 15, '降序')

    # 二分查找
    # result = binary_search(LIST3, -3, "降序")

    # 三分查找
    # result = three_search(LIST3, -3, 0, len(LIST3), "降序")

    # 插值查找（适用于数组分布较为均匀情况，如果中间一部分不均匀某些值会出现死循环情况）
    # result = interpolation_search(LIST3, -5, "降序")

    # 二分和三分对先升后降或先降后升数组求极值

    # 二分对先升后降数组求最大值
    # count = 0  # 给全局变量重新赋值
    # max = binary_search_max(LIST, 0, len(LIST)-1)
    # print("最大值：", max)
    # print("执行次数：", count)

    # 二分对先降后升数组求最小值
    # count = 0   # 给全局变量重新赋值
    # min = binary_search_min(LIST1, 0, len(LIST1) - 1)
    # print("最小值：", min)
    # print("执行次数：", count)

    # 三分对先升后降数组求最大值
    # count = 0 # 给全局变量重新赋值
    # max = three_search_max(LIST, 0, len(LIST)-1)
    # print("最大值：", max)
    # print("执行次数：", count)

    # 三分对先降后升数组求最小值
    # count = 0  # 给全局变量重新赋值
    # min = three_search_min(LIST1, 0, len(LIST1) - 1)
    # print("最小值：", min)
    # print("执行次数：", count)
