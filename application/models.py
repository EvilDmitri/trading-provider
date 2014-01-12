"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb


class ProviderModel(ndb.Model):
    """Provider Model"""
    trading_name = ndb.TextProperty(required=True)
    phone_number = ndb.StringProperty(required=True)
    post_code = ndb.StringProperty(required=True)

    timestamp = ndb.DateTimeProperty(auto_now_add=True)



