from flask import Flask, render_template
import sqlalchemy as db
import sqlite3

# flask part

app = Flask(__name__)


@app.route('/')
def base():

    return render_template("main.html.j2",)




# database part
# https://tutorials.technology/tutorials/Using-python-SQLAlchemy-with-SQLlite3-tutorial.html
