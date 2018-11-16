from flask import render_template,request,redirect,url_for
from . import main
from ..models import Sources
from ..request import get_sources ,get_articles, search_article


# Views

@main.route('/')

def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources by category

    general_sources = get_sources('general')

    business_sources = get_sources('business')

    technology_sources = get_sources('technology')

    sports_sources = get_sources('sports')

    entertainment_sources = get_sources('entertainment')

    health_sources = get_sources('health')

    science_sources = get_sources('science')

    title = 'Amira\'s Post'

    search_article = request.args.get('article_query')


    if search_article:

        return redirect(url_for('main.search',article_name = search_article))

    else:

        return render_template('index.html', title = title, general = general_sources, business = business_sources, technology = technology_sources, sports = sports_sources, entertainment = entertainment_sources, health = health_sources, science = science_sources)

@main.route('/articles/<source>')

def articles(source):

    '''
    View articles for a specific source page function that returns the movie details page and its data
    '''

    articles = get_articles(source)

    return render_template('article.html', articles = articles)

@main.route('/search/<article_name>')

def search(article_name):

    '''
    View function to display the search results
    '''

    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    # title = f'search results for {article_name}'

    return render_template('search.html',articles = searched_articles)





# @main.route('/')
# def index ():
#     '''
#     view root page function that returns the index page and its data
#     '''
#     sources = get_sources ('business')
#     entertainment_sources = get_sources('entertainment')
#     technology_sources = get_sources('technology')
#     sports_sources = get_sources('sports')
#     title = "News Highlights"

#     return render_template ('index.html' ,title = title, sources =sources,entertainment_sources = entertainment_sources,technology_sources = technology_sources,sports_sources = sports_sources )

# @main.route('/sources/<id>')
# def articles(id):
# 	'''
# 	view articles page
# 	'''
# 	articles = get_articles(id)
# 	title = f'NH | {id}'

# 	return render_template('articles.html',title= title,articles = articles)


# # @main.route('/update/<id>')
# # def article(id):
# #     detz_articles = get_update(id)
# #     print(detz_articles)
# #     return render_template('news-update.html',detz = detz_articles)
