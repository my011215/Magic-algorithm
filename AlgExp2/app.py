from flask import Flask
from flask_cors import CORS
import random

from flask import request, jsonify

import logical



app = Flask(__name__)
CORS(app, supports_credentials=True)  # 配置全局路由



# /api2/searchMenu
@app.route('/api2/searchMenu', method = ['POST'])
def searchMenu():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
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
@app.route('/api2/disorderArr', method = ['POST'])
def disorderArr():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    arr = logical.creatArr(int(getJson['arrLen']), 0)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'arr': arr
        }
    }
    return jsonify(res)


# /api2/judgementStatus
@app.route('/api2/judgementStatus', method = ['POST'])
def judgementStatus():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    status = logical.judgeArr(int(getJson['arrLen']))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            'status': status
        }
    }
    return jsonify(res)


# /api2/seqRet
@app.route('/api2/seqRet', method = ['POST'])
def seqRet():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    res, count = logical.sequentialSearch(getJson['arr'].split(","), int(getJson['item']))
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
@app.route('/api2/ThreeMethods', method = ['POST'])
def ThreeMethods():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数
    minItem0, count0 = logical.threeMethodFindKMin(getJson['arr'].split(","), int(getJson['k']), 0)
    minItem1, count1 = logical.threeMethodFindKMin(getJson['arr'].split(","), int(getJson['k']), 1)
    minItem2, count2 = logical.threeMethodFindKMin(getJson['arr'].split(","), int(getJson['k']), 2)
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

if __name__ == '__main__':
    app.run()


