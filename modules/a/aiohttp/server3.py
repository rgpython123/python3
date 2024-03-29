from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous3")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, host='127.0.0.1', port=8083)
