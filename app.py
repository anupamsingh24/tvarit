import flask
from flask import request, jsonify
from task1 import checkInRange

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/sum', methods=['POST'])
def sumOfNumbers():
    res = {}

    if 'numbers' in request.json:
        nums = request.json['numbers']
    else:
        error_msg = "No numbers passed in the request"
        res['error'] = error_msg
        res['status'] = 400
        return jsonify(res)

    if len(nums) < 3:
        error_msg = "Exactly 3 numbers are required"
        res['error'] = error_msg
        res['status'] = 400
        return jsonify(res)

    sum = 0
    if checkInRange(int(nums[0])):
        sum += int(nums[0])
    if checkInRange(int(nums[1])):
        sum += int(nums[1])
    if checkInRange(int(nums[2])):
        sum += int(nums[2])

    res['status'] = 200
    res['result'] = sum
    return jsonify(res)


app.run()