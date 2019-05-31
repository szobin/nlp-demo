import logging
import aiohttp_jinja2
import spacy
from spacy import displacy
from aiohttp import web

log = logging.getLogger(__name__)
nlp = spacy.load('en')


async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, {'txt': "Next week I'll be in Madrid."})


async def nlp_display(request):
    txt = request.rel_url.query['txt']
    style = request.rel_url.query['style']
    doc = nlp(txt)
    svg = displacy.render(doc, style=style, options={'distance': 90})
    return web.Response(body=svg)
