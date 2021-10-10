from flask import Flask, render_template, request,jsonify, json
# import sqlite3
import asyncio

# flask part

app = Flask(__name__)


@app.route('/')
def base():

    return render_template("main.html.j2",)


@app.route("/api", methods=["POST"])
def json_example():

    json = request.get_json()

    print(json)


    return "saved"


@app.route("/load", methods=["GET"])
def load():


    dictionary = {'stat1':8, 'stat2':0}
    return jsonify(dictionary)






# database part
# https://tutorials.technology/tutorials/Using-python-SQLAlchemy-with-SQLlite3-tutorial.html
# have each page only be accesed by link have user character page (page that lists all their characters) require unique id
# have in eah sheet theuser who owns them
