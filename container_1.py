from aiohttp import web
import requests

async def concatenate_and_send(request):
    
    params = request.rel_url.query

    if "name" not in params:
        return web.Response(
            text="poorly formulated request, missing 'name' parameter\n",
            status=400
        )

    try:
        name = params['name']
        new_name = name + 'two'
        
        r = requests.get(f"http://mongodb:4002/save-in-db?name={name}&new_name={new_name}")

        if r.status_code == 200:
            return web.Response(
                text="everything went well!\n",
                status=200
            )
        elif r.status_code == 400:
            return web.Response(
                text="Internal error sending data to container 2\n",
                status=500
            )
        else:
            return web.Response(
                text="Internal Error in container 2\n",
                status=500
            )

    except Exception as e:
        print(f'Internal Error: {e}')
        return web.Response(
            text="Internal Error in container 1\n",
            status=500
        )

app = web.Application()
app.add_routes([
    web.get('/concat-and-send', concatenate_and_send)
])

ip = '192.168.55.3'
port = 4001

web.run_app(app, host=ip, port=port)

"""
This server is listening for requests on port 4001 (/concat-and-send):
http://localhost:4001/concat-and-send?name=<name>
"""
