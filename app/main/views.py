# Views
@main.route('/')
def index ():
    '''
    view root page function that returns the index page and its data
    '''
    sources = get sources ('business')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    title = "News Highlights"

    return render_template ('index.html' ,title = title, sources =sources,entertainment_sources = entertainment_sources,technology_sources = technology_sources,sports_sources = sports_sources )