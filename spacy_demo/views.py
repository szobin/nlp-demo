import logging
import aiohttp_jinja2
import spacy
from spacy import displacy
from aiohttp import web

log = logging.getLogger(__name__)
nlp = spacy.load('en_core_web_sm')


async def index(request):
    txt = 'London is the capital and most populous city of England and the United Kingdom. Standing on '\
          'the River Thames in the south east of the island of Great Britain, London has been a major '\
          'settlement for two millennia. It was founded by the Romans, who named it Londinium.'
    return aiohttp_jinja2.render_template('index.html', request, {'txt': txt})


async def nlp_display(request):
    txt = request.rel_url.query['txt']
    style = request.rel_url.query['style']
    doc = nlp(txt)
    svg = displacy.render(doc, style=style)
    return web.Response(body=svg)
