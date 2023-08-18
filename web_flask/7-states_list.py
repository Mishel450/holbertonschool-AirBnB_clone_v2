#!/usr/bin/python3
"""task-7"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_db(e):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def st_lists():
    from models.state import State
    st_list = storage.all(State)
    return render_template('7-states_list.html', lista=st_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
