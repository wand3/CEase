from flask_wtf import FlaskForm as Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(Form):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PostForm(Form):
    body = TextAreaField('What\'s on ypur mind', validators=[DataRequired()])
    submit = SubmitField('Post')