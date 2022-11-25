from flask import Flask, jsonify, request
from logicalLayer import search
from flask_cors import CORS  # 导入CORS库
import sys

app = Flask(__name__)

CORS(app, supports_credentials=True)  # 配置全局路由

@app.route('/api/fourMethod', methods=['POST'])
def fourMethod():
    # getJson = request.get_json()
    # print(getJson)
    # upDown = getJson["upDown"]
    # upDown = int(upDown)
    # s = getJson["arr"]
    # arr = s.split(',')
    # arr = [int(x) for x in arr]
    # item = getJson["item"]
    # item = int(item)
    upDown = 0
    arr = [0,1,2,3,4,5,6,7,8,9]
    item = 4
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

@app.route('/api/searchMenuUpDown', methods=['POST'])
def searchMenuUpDown():
    # getJson = request.get_json()
    # print(getJson)
    # s = getJson["arr"]
    # arr = s.split(',')
    # arr = [int(x) for x in arr]
    arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
    # arr = [5, 4, 3, 2, 1, 0, 2, 3, 4, 5]
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

if __name__ == '__main__':
    app.run()
