"""Class used to ensure that the form contains data."""
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class SearchForm(Form):

    """Define a flask form.

    Ensures that the form fields for search word and no. of results contains
    data.
    """

    search_word = StringField('search_word', validators=[DataRequired()])
    no_of_results = IntegerField('no_of_results', validators=[DataRequired()])
