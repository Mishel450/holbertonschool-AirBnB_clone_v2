#!/usr/bin/python3
"""task-7"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_db(e):
    storage.close()


@app.route('/states', strict_slashes=False)
def st_lists():
    from models.state import State
    st_list = storage.all(State)
    return render_template('7-states_list.html', lista=st_list)

@app.route('/states/<id>', strict_slashes=False)
def st_lists_and_id(id):
    from models.state import State
    st_list = storage.all(State).values()
    the_id = "hola"
    for i in st_list:
        if i.id == id:
            the_id = id
            break
    return render_template('9-states.html', lista=i, id=the_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
