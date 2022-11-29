from flask import Flask
from flask_cors import CORS
import random

from flask import request, jsonify

from logical import init



app = Flask(__name__)
CORS(app, supports_credentials=True)  # 配置全局路由



# /api2/searchMenu
@app.route('/api2/searchMenu', methods=['POST'])
def searchMenu():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    arr = logical.creatArr(int(getJson['arrLen']), random.randint(0, 5))
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
    arr = logical.creatArr(int(getJson['arrLen']), 0)
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
        arr = logical.creatArr(int(getJson['arrLen']), 3)
    else:
        arr = logical.creatArr(int(getJson['arrLen']), 4)
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
    status = logical.judgeArr(arr)
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

    res, count = logical.sequentialSearch(arr, int(getJson['item']))
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
    minItem0, count0 = logical.threeMethodFindKMin(arr, int(getJson['k']), 0)
    minItem1, count1 = logical.threeMethodFindKMin(arr, int(getJson['k']), 1)
    minItem2, count2 = logical.threeMethodFindKMin(arr, int(getJson['k']), 2)
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
    method1 = init.sequential_search(arr, item, upDown)
    method2 = init.binary_search(arr, item, upDown)
    method3 = init.three_search(arr, item, 0, len(arr), upDown)
    method4 = init.interpolation_search(arr, item, upDown)
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
        method1 = init.get_binary_search_max(arr, 0, len(arr)-1)
        method2 = init.get_three_search_max(arr, 0, len(arr)-1)
    elif pattern == 1:
        method1 = init.get_binary_search_min(arr, 0, len(arr) - 1)
        method2 = init.get_three_search_min(arr, 0, len(arr)-1)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "method1": method1,
            "method2": method2,
        }
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run()


