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

if __name__ == '__main__':
    app.run()
