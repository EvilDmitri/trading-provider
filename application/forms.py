"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.ndb import model_form

from .models import ProviderModel


# class ClassicExampleForm(wtf.Form):
#     example_name = wtf.TextField('Name', validators=[validators.Required()])
#     example_description = wtf.TextAreaField('Description', validators=[validators.Required()])


# App Engine ndb model form example
ProviderForm = model_form(ProviderModel, wtf.Form, field_args={
    'trading_name': dict(validators=[validators.Required()]),
    'phone_number': dict(validators=[validators.Required()]),
    'post_code': dict(validators=[validators.Required()]),
})
