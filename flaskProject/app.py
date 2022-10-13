from flask import Flask, jsonify, request
import logicalLayer

app = Flask(__name__)


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.after_request(after_request)


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
    data = logicalLayer.oneMinFib(getJson['n'])
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
    nameArr1 = logicalLayer.GetMaxFibonacciD()
    nameArr2 = logicalLayer.thirtyMinFib()
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
    app.run()
