from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles,get_updates
from ..models import Sources

# Views
@main.route('/')
def index ():
    '''
    view root page function that returns the index page and its data
    '''
    sources = get_sources ('business')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    title = "News Highlights"

    return render_template ('index.html' ,title = title, sources =sources,entertainment_sources = entertainment_sources,technology_sources = technology_sources,sports_sources = sports_sources )

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)


@main.route('/update/<id>')
def article(id):
    detz_articles = get_updates(id)
    print(detz_articles)
    return render_template('news-update.html',detz = detz_articles)
