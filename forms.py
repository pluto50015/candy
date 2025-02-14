"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('お名前', validators=[DataRequired()])
    email = StringField('メールアドレス', validators=[DataRequired()])
    message = TextAreaField('メッセージ', validators=[DataRequired()])
    submit = SubmitField('送信')
"""
