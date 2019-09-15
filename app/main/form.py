from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')