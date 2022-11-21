from flask import Flask, jsonify, request
import logicalLayer
from flask_cors import CORS  # 导入CORS库
import sys


app = Flask(__name__)

CORS(app, supports_credentials=True)  # 配置全局路由

# 递归法求系统环境最大斐波那契数位置接口
@app.route('/api/recursiveEnvMax', methods=['GET'])
def recursiveEnvMax():
    data = logicalLayer.maxNumFib()
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)


# 1分钟递归求系统最大支持数接口
@app.route('/api/oneMinuteRecursive', methods=['POST'])
def oneMinuteRecursive():
    getJson = request.json  # 获取 JOSN 数据
    data = logicalLayer.oneMinFib(int(getJson['n']))
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
    nameArr1 = logicalLayer.FibonacciD(n)
    nameArr2 = logicalLayer.FibonacciDImproment(n)
    nameArr3 = logicalLayer.demoFibonacci_Recursion_tool(n)
    nameArr4 = logicalLayer.FibonacciEquation(n)
    nameArr5 = logicalLayer.demofib_matrix(n)
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
    data = logicalLayer.GetFibonacciD()
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
    nameArr1 = logicalLayer.GetMaxFibonacciD()
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
    nameArr2 = logicalLayer.thirtyMinFib()
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
    data = logicalLayer.GetMaxFibonacci()
    print(data)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)  # 例如这里设置为十万
    app.run()
