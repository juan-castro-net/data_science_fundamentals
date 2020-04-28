from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route("/", methods=["POST"])
def starting_url():
    json_data = request.json
    user = json_data["user"]
    email = json_data["email"]
    data = {"usuario":user,"correo":email}
    users.append(data)
    return {"data":data}

@app.route('/list', methods=["GET"])
def show_form_data():
    return jsonify(users)

if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=8080)
    app.run()