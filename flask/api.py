from flask import Flask, jsonify, request, render_template
from logicalLayer import _init_

app = Flask(__name__)

# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)

# 五种方法结果展示接口
@app.route('/api/fiveMethodsShow', methods=['POST'])
def fiveMethodsShow():
    # num = request.get_json()
    # num = int(num)
    nameArr1 = _init_.FibonacciD(5)
    nameArr2 = _init_.FibonacciDImproment(5)
    # nameArr3 = _init_.Fibonacci_Recursion_tool(num)
    nameArr4 = _init_.FibonacciEquation(5)
    # nameArr5 = _init_.demofib_matrix(num)
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": {
            "nameArr":[
                nameArr1,
                nameArr2,
                # nameArr3,
                nameArr4,
                # nameArr5,
            ]
        }
    }
    return jsonify(res)


# 迭代法求系统环境最大斐波那契数位置接口
@app.route('/api/iterativeEnvMax', methods=['GET'])
def iterativeEnvMax():
    data = _init_.GetFibonacciD()
    res = {
        "status_code": 0,
        "status_msg": "success",
        "data": data
    }
    return jsonify(res)

# 递归法和迭代法30妙斐波那契值接口
@app.route('/api/recursiveIterationThirty', methods=['GET'])
def recursiveIterationThirty():
    nameArr1 = _init_.GetMaxFibonacciD()
    # nameArr2 = _init_.thirtyMinFib()
    res = {
    "status_code": 0,
    "status_msg": "success",
    "data": {
        "nameArr": [
            nameArr1,
            # nameArr2
        ]
        }
    }
    return jsonify(res)

# 近似公式结果展示接口
@app.route('/api/formula', methods=['GET'])
# def Error():
#     return render_template('Error.html')
def formula():
    # return render_template('Error.html')
    data = _init_.GetMaxFibonacci()
    print(data)
    res = {
    "status_code": 0,
    "status_msg": "success",
    "data": data
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run()