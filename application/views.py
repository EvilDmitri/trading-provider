"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from forms import ProviderForm
from models import ProviderModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    form = ProviderForm()
    return render_template('home.html', form=form)
    #return redirect(url_for('list_providers'))


def list_providers():
    """List all providers"""
    providers = ProviderModel.query()
    form = ProviderForm()
    return render_template('list_providers.html', providers=providers, form=form)


def add_provider():
    provider = ProviderModel()
    form = ProviderForm()
    if form.validate_on_submit():
        provider.trading_name = form.data.get('trading_name')
        provider.phone_number = form.data.get('phone_number')
        provider.post_code = form.data.get('post_code')
        try:
            provider.put()
            provider_id = provider.key.id()
            flash(u'Provider %s successfully saved.' % provider_id, 'success')
            return redirect(url_for('list_providers'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_providers'))

    return render_template('add_provider.html', provider=provider, form=form)


def edit_provider(provider_id):
    provider = ProviderModel.get_by_id(provider_id)
    form = ProviderForm(obj=provider)
    if request.method == "POST":
        if form.validate_on_submit():
            provider.trading_name = form.data.get('trading_name')
            provider.phone_number = form.data.get('phone_number')
            provider.post_code = form.data.get('post_code')
            try:
                provider.put()
                provider_id = provider.key.id()
                flash(u'Provider %s successfully saved.' % provider_id, 'success')
                return redirect(url_for('list_providers'))
            except CapabilityDisabledError:
                flash(u'App Engine Datastore is currently in read-only mode.', 'info')
                return redirect(url_for('list_providers'))

    return render_template('edit_provider.html', provider=provider, form=form)


def delete_provider(provider_id):
    """Delete a provider object"""
    provider = ProviderModel.get_by_id(provider_id)
    try:
        provider.key.delete()
        flash(u'Provider %s successfully deleted.' % provider_id, 'success')
        return redirect(url_for('list_providers'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_providers'))


@cache.cached(timeout=60)
def cached_providers():
    """This view should be cached for 60 sec"""
    providers = ProviderModel.query()
    return render_template('list_providers_cached.html', providers=providers)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

