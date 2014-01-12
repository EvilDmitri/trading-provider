"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=views.home)

# Providers list page
app.add_url_rule('/providers', 'list_providers', view_func=views.list_providers, methods=['GET', 'POST'])

# Providers list page (cached)
app.add_url_rule('/providers/cached', 'cached_providers', view_func=views.cached_providers, methods=['GET'])

# Add a Provider
app.add_url_rule('/add', 'add_provider', view_func=views.add_provider, methods=['GET', 'POST'])

# Edit a provider
app.add_url_rule('/providers/<int:provider_id>/edit', 'edit_provider', view_func=views.edit_provider, methods=['GET', 'POST'])

# Delete a provider
app.add_url_rule('/providers/<int:provider_id>/delete', view_func=views.delete_provider, methods=['POST'])


## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

