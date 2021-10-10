# front end
# backend
import asyncio
from typing import Optional, List, Union

import motor
import motor.motor_asyncio
from beanie import Document, Indexed, init_beanie
from flask import Flask, json, jsonify, render_template, request
from pydantic import BaseModel

# flask part

app = Flask(__name__)


@app.route("/")
def base():

    return render_template(
        "main.html.j2",
    )


@app.route("/api", methods=["POST"])
def json_example():

    json = request.get_json()

    print(json)

    return "saved"


@app.route("/load", methods=["GET"])
def load():

    dictionary = {"stat1": 8, "stat2": 0}
    return jsonify(dictionary)


# database part
# have each page only be accesed by link have user character page (page that lists all their characters) require unique id
# have in eah sheet theuser who owns them


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class Category(BaseModel):
    pass


class character(Document):
    name: str
    description: str
    primarystats: List[Union[str, int, float]]
    # make this a unioun with ints
    secondarystats: List[Union[str, int, float]]

    class collection:
        name = "sussy"


async def init():
    # Crete Motor client
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://192.168.0.218:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client.test_database, document_models=[character])


loop = asyncio.get_event_loop()
loop.run_until_complete(init())

Cunt = character(
    name="Cunt",
    description="yee",
    primarystats=["19", "5"],
    secondarystats=["uwu", "owo"],
)


async def de():
    await Cunt.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(de())


# # umongo motor connection
# instance = MotorAsyncIOInstance(db)

# print(instance)


# @instance.register
# class Sheet(Document):
#     name = fields.StrField(required=True)
#     primarystats = fields.StrField(required=True)
#     secondarystats = fields.ListField()
#     birthday = fields.DateTimeField()


# async def death():
#     client_data = {
#         "name": "Cunt",
#         "birthday": "2001-09-22T00:00:00Z",
#         "primarystats": "19",
#     }
#     odwin = Sheet(**client_data)

#     await odwin.commit()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(death())
