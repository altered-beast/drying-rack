from flask import Flask, render_template, request,jsonify, json
# import sqlalchemy as db   this might be broken
# import sqlite3

# flask part

app = Flask(__name__)


@app.route('/')
def base():

    return render_template("main.html.j2",)


@app.route("/api", methods=["POST"])
def json_example():

    json = request.get_json()

    print(json)

    return "Thanks!", 200


@app.route("/load")
def load():
    dictionary = {'stat1':6, 'stat2':5}
    return jsonify(dictionary)




# database part
# https://tutorials.technology/tutorials/Using-python-SQLAlchemy-with-SQLlite3-tutorial.html
