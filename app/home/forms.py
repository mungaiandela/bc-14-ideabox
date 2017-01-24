from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, TextField, validators
from wtforms.validators import DataRequired
from ..models import User, Data


class IdeaboxForm(FlaskForm):
    name = TextField('enter title here', validators=[DataRequired()])
    description = TextField('Enter your new idea',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')


class IdeaboxComments(FlaskForm):
    comment = TextField(
        'Enter your new idea', validators=[DataRequired()])
    submit = SubmitField('Submit')
