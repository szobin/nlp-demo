import logging
import jinja2
import aiohttp_jinja2
from aiohttp import web
from spacy_demo.views import index, nlp_display


async def init_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('spacy_demo', 'templates'))
    app.router.add_get('/', index)
    app.router.add_get('/nlp/display', nlp_display)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()
    web.run_app(app, host='localhost', port=8080)


if __name__ == '__main__':
    main()
