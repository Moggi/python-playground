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

ENV = environ.Env()
ENV.read_env()


class MainHandler(RequestHandler):

    async def get(self):
        try:
            pool = await aioredis.create_pool(
                address=self.settings.get('REDIS_URI'),
                password=self.settings.get('REDIS_SECRET'),
                minsize=2, maxsize=10, create_connection_timeout=5
            )
        # except asyncio.TimeoutError as e:
            # First time raises an asyncio.TimeOutError
            # raise HTTPError()
            # raise HTTPError(log_message='')
        except Exception as _e:
            # Subsequent times raises an OSError with errno = 65
            # message = 'No route to host'
            raise _e
        await pool.execute('set', 'my_key', 'value')
        print(await pool.execute('get', 'my_key'))
        pool.close()
        await pool.wait_closed()
        self.write('Hello, world!')


async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


def make_app(settings):
    return Application(
        [
            (r"/", MainHandler),
        ],
        **settings
    )


if __name__ == "__main__":
    SETTINGS = {
        'debug': True,
        'REDIS_URI': ENV('REDIS_URI'),
        'REDIS_SECRET': ENV('REDIS_SECRET'),
    }
    APP = make_app(SETTINGS)
    APP.listen(port=8888, address='127.0.0.1')
    IOLoop.current().start()
