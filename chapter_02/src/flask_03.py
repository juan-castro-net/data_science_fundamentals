from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/width/<float:width>')
def show_width(width):
    # show the width, the width is a float
    return 'Width %f' % width

@app.route('/code/<uuid:id>')
def show_code(id):
    # show the code, the code is a uuid
    return 'Code %s' % id

if __name__ == '__main__':
    app.run()