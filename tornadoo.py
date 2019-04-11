"""Requirements:
tornado==6.0.2
hiredis==1.0.0
aioredis==1.2.0
django-environ==0.4.5
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
import aioredis
import environ

env = environ.Env()
env.read_env()


class MainHandler(RequestHandler):

    async def get(self):
        pool = await aioredis.create_pool(
                address=env('REDIS_URI'),
                password=env('REDIS_SECRET'),
                minsize=5, maxsize=10
            )
        await pool.execute('set', 'my_key', 'value')
        print(await pool.execute('get', 'my_key'))
        pool.close()
        await pool.wait_closed()
        self.write('Hello, world!')


async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


def make_app(**settings):
    return Application(
        [
            (r"/", MainHandler),
        ],
        **settings
    )


if __name__ == "__main__":
    app = make_app(debug=True)
    app.listen(port=8888, address='127.0.0.1')
    IOLoop.current().start()
