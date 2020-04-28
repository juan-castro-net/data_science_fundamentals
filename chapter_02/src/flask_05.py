from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def get_current_user():
    return jsonify(username="Maria",
                   email="maria@gmail.com",
                   id="1298")

@app.route('/json_from_tuple')
def show_tuple():
    return jsonify(1,2,3)

@app.route('/json_from_list')
def show_list():
    return jsonify([1,2,3])

if __name__ == '__main__':
    app.run()