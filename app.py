from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"key": request.args.get("value")})

if __name__ == '__main__':
    app.run(debug=True)