from flask import Flask
from flask import render_template
import sqlalchemy as db
import sqlite3

# flask part

app = Flask(__name__)


@app.route('/')
def base():

    return render_template("main.html.j2",)




# database part
