import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def insert_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(record, indent=2))
    return jsonify(record)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('data')
    print(name)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        return jsonify(records)

@app.route('/', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(record, indent=2))
    return jsonify(record)

    
@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps({}, indent=2))
    return jsonify({})

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num**2})

if __name__ == '__main__':
    app.run(debug=True)