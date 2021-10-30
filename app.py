# front end
# backend
import asyncio
from datetime import datetime
from typing import List, Optional, Union
import json

import motor
import motor.motor_asyncio
from beanie import Document, Indexed, init_beanie
from pydantic import BaseModel
from quart import Quart, jsonify, request, render_template


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

app = Quart(__name__)


class character(Document):
    name: str = "new character"
    description: Optional[str]
    primary_stats: List[Union[str, int]] = [0, 0]
    secondary_stats: List[Union[str, int]] = [0, 0]
    dt_created: str = dt_string


client = None
database = None


@app.before_first_request
async def setup():
    global client, database
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://192.168.0.218:27017")
    await init_beanie(database=client.test_database, document_models=[character])


@app.route("/")
async def base():

    return await render_template(
        "main.html.j2",
    )


@app.route("/api/init_char", methods=["GET"])
async def init_char():
    new_char = character()
    await new_char.save()
    char_id = str(new_char.id)
    return char_id


@app.route("/api/save", methods=["POST"])
async def json_example():

    web_json = await request.get_json()

    working_char = character(
        primary_stats=web_json["primarystats"],
        secondary_stats=[21, 7],
        name="toot too",
        description="semen",
        dt_created=dt_string,
    )

    await working_char.save()

    return "saved"


@app.route("/api/load", methods=["POST"])
async def load():
    print(await request.get_json())
    web_json = await request.get_json()
    char_id = web_json["id"]

    payload = await character.get(char_id)

    return payload.json()


# database part
# have each page only be accesed by link have user character page (page that lists all their characters) require unique id
# have in eah sheet theuser who owns them


app.run()
