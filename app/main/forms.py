from flask_wtf import  FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required
class UpdatePostForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    category=SelectField('Category',choices=[('Medical','Medical'),('Memorial','Memorial'),('Education','Education'),('Sports','Sports'),('Emergency','Emergency')], validators=[Required()])
    description=StringField('Title', validators=[Required()])
    content=TextAreaField('Your Post.', validators=[Required()])
    submit=SubmitField('save')
class PostForm(FlaskForm):
    title=StringField('Title', validators=[Required()])
    description=StringField('Description', validators=[Required()])
    category=SelectField('Category',choices=[('Medical','Medical'),('Memorial','Memorial'),('Education','Education'),('Sports','Sports'),('Emergency','Emergency')], validators=[Required()])
    image = StringField('Image url',validators = [Required()])
    content=TextAreaField('Your Post', validators=[Required()])
    submit=SubmitField('Post')
class CommentForm(FlaskForm):
    comment=TextAreaField('Leave a comment',validators=[Required()])
    submit=SubmitField('Comment')
