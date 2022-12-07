from flask import Flask, jsonify, request
import random
import numpy as np
from logicalLayer import init
from logicalLayer import search
from logicalLayer import bag
from flask_cors import CORS  # 导入CORS库
import sys


app = Flask(__name__)

CORS(app, supports_credentials=True)  # 配置全局路由

#实验一
# 递归法求系统环境最大斐波那契数位置接口
@app.route('/api/recursiveEnvMax', methods=['GET'])
def recursiveEnvMax():
    data = init.maxNumFib()
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)


# 1分钟递归求系统最大支持数接口
@app.route('/api/oneMinuteRecursive', methods=['POST'])
def oneMinuteRecursive():
    getJson = request.json  # 获取 JOSN 数据int(getJson['n']
    data = init.oneMinFib(int(getJson['n']))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)


# 五种方法结果展示接口
@app.route('/api/fiveMethodsShow', methods=['POST'])
def fiveMethodsShow():
    getJson = request.get_json()
    n = getJson["n"]
    print(getJson)
    # n = 4
    n = int(n)
    nameArr1 = init.FibonacciD(n)
    nameArr2 = init.FibonacciDImproment(n)
    nameArr3 = init.demoFibonacci_Recursion_tool(n)
    nameArr4 = init.FibonacciEquation(n)
    nameArr5 = init.demofib_matrix(n)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "nameArr": [
                nameArr1,
                nameArr2,
                nameArr3,
                nameArr4,
                nameArr5,
            ]
        }
    }
    print(res)
    return jsonify(res)


# 迭代法求系统环境最大斐波那契数位置接口
@app.route('/api/iterativeEnvMax', methods=['GET'])
def iterativeEnvMax():
    data = init.GetFibonacciD()
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)


# 递归法和迭代法30妙斐波那契值接口
@app.route('/api/recursiveIterationThirty', methods=['GET'])
def recursiveIterationThirty():
    print('接口1')
    nameArr1 = init.GetMaxFibonacciD()
    print(nameArr1)
    nameArr2 = 0
    print(nameArr2)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "nameArr": [
                nameArr1,
                nameArr2
            ]
        }
    }
    return jsonify(res)

# 递归法和迭代法30妙斐波那契值接口
@app.route('/api/recursiveIterationThirty2', methods=['GET'])
def recursiveIterationThirty2():
    print('接口2')
    nameArr1 = 0
    print(nameArr1)
    nameArr2 = init.thirtyMinFib()
    print(nameArr2)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "nameArr": [
                nameArr1,
                nameArr2
            ]
        }
    }
    return jsonify(res)


# 近似公式结果展示接口
@app.route('/api/formula', methods=['GET'])
def formula():
    data = init.GetMaxFibonacci()
    print(data)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)

#实验二
# /api2/searchMenu
@app.route('/api2/searchMenu', methods=['POST'])
def searchMenu():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    arr = search.creatArr(int(getJson['arrLen']), random.randint(0, 5))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'arr': arr
        }
    }
    return jsonify(res)


# /api2/disorderArr
@app.route('/api2/disorderArr', methods=['POST'])
def disorderArr():
    getJson = request.json  # 获取 JOSN 数据
    arr = search.creatArr(int(getJson['arrLen']), 0)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'arr': arr
        }
    }
    return jsonify(res)

@app.route('/api2/createMountainArr', methods=['POST'])
def createMountainArr():
    getJson = request.json  # 获取 JOSN 数据
    if int(getJson['pattern']) == 0:
        arr = search.creatArr(int(getJson['arrLen']), 3)
    else:
        arr = search.creatArr(int(getJson['arrLen']), 4)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'arr': arr
        }
    }
    return jsonify(res)


# /api2/judgementStatus
@app.route('/api2/judgementStatus', methods=['POST'])
def judgementStatus():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    arr = list(map(int, getJson['arr'].split(",")))
    status = search.judgeArr(arr)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'status': status
        }
    }
    return jsonify(res)


# /api2/seqRet
@app.route('/api2/seqRet', methods=['POST'])
def seqRet():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    arr = list(map(int, getJson['arr'].split(",")))

    res, count = search.sequentialSearch(arr, int(getJson['item']))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'haveOrNot': res,
            'compareTime': count
        }
    }
    return jsonify(res)


# /api2/ThreeMethods
@app.route('/api2/ThreeMethods', methods=['POST'])
def ThreeMethods():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    arr = list(map(int, getJson['arr'].split(",")))
    minItem0, count0 = search.threeMethodFindKMin(arr, int(getJson['k']), 0)
    minItem1, count1 = search.threeMethodFindKMin(arr, int(getJson['k']), 1)
    minItem2, count2 = search.threeMethodFindKMin(arr, int(getJson['k']), 2)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'method1': {
                'kNum': minItem0,
                'compareTime': count0
            },
            'method2': {
                'kNum': minItem1,
                'compareTime': count1
            },
            'method3': {
                'kNum': minItem2,
                'compareTime': count2
            }
        }
    }
    return jsonify(res)

@app.route('/api2/fourMethod', methods=['POST'])
def fourMethod():
    getJson = request.get_json()
    print(getJson)
    upDown = getJson["upDown"]
    upDown = int(upDown)
    s = getJson["arr"]
    arr = s.split(',')
    arr = [int(x) for x in arr]
    item = getJson["item"]
    item = int(item)
    # upDown = 0
    # arr = [4,5,11,13,4,-3,-7,-10,-14,-19]
    # item = 4
    if upDown == 0:
        arr = sorted(arr, reverse=False)
    elif upDown ==1:
        arr = sorted(arr, reverse=True)
    method1 = search.sequential_search(arr, item, upDown)
    method2 = search.binary_search(arr, item, upDown)
    method3 = search.three_search(arr, item, 0, len(arr), upDown)
    method4 = search.interpolation_search(arr, item, upDown)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
                "method1": method1,
                "method2": method2,
                "method3": method3,
                "method4": method4,
        }
    }
    return jsonify(res)

@app.route('/api2/searchMenuUpDown', methods=['POST'])
def searchMenuUpDown():
    getJson = request.get_json()
    print(getJson)
    s = getJson['arr']
    arr = s.split(',')
    arr = [int(x) for x in arr]
    print(arr)
    # arr = [10,1,-2,-12,-11,-6,-6,-3,0,10]
    # # arr = [5, 4, 3, 2, 1, 0, 2, 3, 4, 5]
    if arr[0] < arr[1]:
        pattern = 0
    else:
        pattern = 1
    if pattern == 0:
        method1 = search.get_binary_search_max(arr, 0, len(arr)-1)
        method2 = search.get_three_search_max(arr, 0, len(arr)-1)
    elif pattern == 1:
        method1 = search.get_binary_search_min(arr, 0, len(arr) - 1)
        method2 = search.get_three_search_min(arr, 0, len(arr)-1)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "method1": method1,
            "method2": method2,
        }
    }
    return jsonify(res)

# 贪心法求分数背包问题
@app.route('/api3/bagMenu', methods=['POST'])
def bagMenu():
    getJson = request.get_json()
    C = getJson["bagCap"]
    C = int(C)
    eachWeight = getJson["eachWeight"]
    # C = 50
    # eachWeight = "10 20 30"
    weight = list(map(float, eachWeight.split()))
    eachVal = getJson["eachVal"]
    # eachVal = "60 100 120"
    value = list(map(float, eachVal.split()))
    item = list(zip(weight, value))
    value = bag.fractional_backpack(item, C)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "weight": weight,
            "value": value
        }
    }
    return jsonify(res)

# 贪心发求0-1背包问题（贪重量）
@app.route('/api3/Greedy01', methods=['POST'])
def Greedy01():
    getJson = request.get_json()
    C = getJson["bagCap"]
    C = int(C)
    eachWeight = getJson["eachWeight"]
    # C = 50
    # eachWeight = "10 20 30"
    weight = list(map(float, eachWeight.split()))
    eachVal = getJson["eachVal"]
    # eachVal = "60 100 120"
    value = list(map(float, eachVal.split()))
    item0 = list(zip(weight, value))
    item = np.array(item0)
    idex_weight = bag.Weight(item)
    weight, value = bag.GreedyAlgo(item, C, idex_weight)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "weight": weight,
            "value": value
        }
    }
    return jsonify(res)

@app.route('/api3/Brute01', methods=['POST'])
def Brute01():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    w = int(getJson["bagCap"])
    i = int(getJson["bagNum"])-1
    weight = list(map(float, getJson["eachWeight"].split()))
    value = list(map(float, getJson["eachVal"].split()))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": bag.backpack(i, w, weight, value)
    }
    return jsonify(res)


@app.route('/api3/Dynamic01', methods=['POST'])
def Dynamic01():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    w = int(getJson["bagCap"])
    i = int(getJson["bagNum"]) - 1
    weight = list(map(int, getJson["eachWeight"].split()))
    value = list(map(int, getJson["eachVal"].split()))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": int(bag.solve(value, weight, w, i))
    }
    return jsonify(res)

@app.route('/api3/ImproveDy', methods=['POST'])
def ImproveDy():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    w = int(getJson["bagCap"])
    i = int(getJson["bagNum"]) - 1
    weight = list(map(int, getJson["eachWeight"].split()))
    value = list(map(int, getJson["eachVal"].split()))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": int(bag.solve2(value, weight, w, i))
    }
    return jsonify(res)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)  # 例如这里设置为十万
    app.run()
