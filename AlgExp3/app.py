from flask import Flask, jsonify, request
from logicalLayer import bag
from flask_cors import CORS  # 导入CORS库
import numpy as np
import sys


app = Flask(__name__)

CORS(app, supports_credentials=True)  # 配置全局路由

# 贪心法求分数背包问题
@app.route('/api3/bagMenu', methods=['POST'])
def bagMenu():
    # getJson = request.get_json()
    # C = getJson["bagCap"]
    # C = int(C)
    # eachWeight = getJson["eachWeight"]
    C = 50
    eachWeight = "10 20 30"
    weight = list(map(float, eachWeight.split()))
    # eachVal = getJson["eachVal"]
    eachVal = "60 100 120"
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
def searchMenu():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    w = int(getJson["bagCap"])
    i = int(getJson["bagNum"])
    eachWeight = getJson["eachWeight"]
    weight = list(map(int, eachWeight.split()))
    eachVal = getJson["eachVal"]
    value = list(map(int, eachVal.split()))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": Logical.backpack(i, w, weight, value)
    }
    return jsonify(res)


@app.route('/api3/Dynamic01', methods=['POST'])
def searchMenu():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    w = int(getJson["bagCap"])
    i = int(getJson["bagNum"])
    eachWeight = getJson["eachWeight"]
    weight = list(map(int, eachWeight.split()))
    eachVal = getJson["eachVal"]
    value = list(map(int, eachVal.split()))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": Logical.solve(i, w, weight, value)
    }
    return jsonify(res)

@app.route('/api3/ImproveDy', methods=['POST'])
def searchMenu():
    getJson = request.json  # 获取 JOSN 数据
    # 这里还要有一个随机数，每个都是平均的
    w = int(getJson["bagCap"])
    i = int(getJson["bagNum"])
    eachWeight = getJson["eachWeight"]
    weight = list(map(int, eachWeight.split()))
    eachVal = getJson["eachVal"]
    value = list(map(int, eachVal.split()))
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": Logical.solve2(i, w, weight, value)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run()
