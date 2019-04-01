from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


class MainHandler(RequestHandler):

    async def get(self):
        self.write("Hello, world")


async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body


def make_app(**settings):
    return Application(
        [
            (r"/", MainHandler),
        ],
        settings
    )


if __name__ == "__main__":
    app = make_app(debug=True)
    app.listen(port=8888, address='127.0.0.1')
    IOLoop.current().start()
