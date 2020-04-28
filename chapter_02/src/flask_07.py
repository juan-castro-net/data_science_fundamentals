from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route("/get", methods=["GET"])
def show_get_data():
    name = request.args.get("name")
    age = request.args.get('age')  
    return "<p>Name: {} <br/> Age :{}</p>".format(name, age)

@app.route("/post", methods=["POST"])
def show_post_data():
    name = request.form.get('name')
    age = request.form.get('age')  
    return "<p>Name: {} <br/> Age :{}</p>".format(name, age)

if __name__ == '__main__':
    app.run()