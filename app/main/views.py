from flask import render_template
from . import main
from ..request import get_sources,get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources('general')
    sports_sources = get_sources('sports')
    health_sources = get_sources('health')
    technology_sources = get_sources('technology')


    title = 'welcome to news updates'
    return render_template('index.html', title=title, general=news_sources, sports=sports_sources, health=health_sources, technology = technology_sources)
@main.route('/articles/<id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = 'welcome to news updates'
    articles = get_articles(id)
    return render_template('articles.html',title=title,id = id, articles=articles)


