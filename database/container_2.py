from aiohttp import web
from datetime import datetime
from pymongo import MongoClient
import requests

async def save_with_timestamp(request):
    params = request.rel_url.query

    for param in ["name", "new_name"]:
        if param not in params:

            return web.Response(
                text=f"poorly formulated request, missing {param} parameter\n",
                status=400
            )

    try:
        name = params['name']
        new_name = params["new_name"]

        client = MongoClient(port=27017)
        db = client.pokemon
        db.names.insert_one({'ts': datetime.now(), 'name': name})
        db.names.insert_one({'ts': datetime.now(), 'name': new_name})

        return web.Response(
            text="names saved correctly in database with the timestamp\n",
            status=200
        )

    except Exception as e:
        print(f'Internal Error: {e}\n')
        return web.Response(
            text="Internal Error",
            status=500
        )

app = web.Application()
app.add_routes([
    web.get('/save-in-db', save_with_timestamp)
])

ip = 'mongodb'
port = 4002

web.run_app(app, host=ip, port=port)

"""
This server is listening for requests on port 4002 (/save-in-db):
http://localhost:4002/save-in-db?name=<name>&new_name=<name_concatenated>
"""
