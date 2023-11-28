import asyncio, os, json, time
from datetime import datetime
import logging
from aiohttp import web

logging.basicConfig(level=logging.INFO)


async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    logging.info('server started at http://127.0.0.1:9000...')
    return app


if __name__ == '__main__':
    web.run_app(init(), host='127.0.0.1', port=9000)
