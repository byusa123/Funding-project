from flask import render_template,url_for,abort,redirect,request
from . import main
from flask_login import login_user,login_required,current_user
# from .forms import RegistrationForm,LoginForm
from ..models import User,Post,Comment
from .. import db,photos
from .forms import UpdatePostForm,PostForm,CommentForm
# import requests

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ufund')
def fundraiser():
    postes=Post.query.all()
    medical=Post.query.filter_by(category='Medical').all()
    memorial=Post.query.filter_by(category='Memorial').all()
    education=Post.query.filter_by(category='Education').all()
    sports=Post.query.filter_by(category='Sports').all()
    emergency=Post.query.filter_by(category='Emergency').all()
    return render_template('funds.html',medical=medical,memorial=memorial,postes=postes,education=education,sports=sports,emergency=emergency)



@main.route('/comment/<int:post_id>',methods=['GET','POST'])
# @login_required
def comment(post_id):
    form=CommentForm()
    post=Post.query.get(post_id)
    all_comments=Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment=form.comment.data
        post_id=post_id
        # user_id=current_user._get_current_object().id
        new_comment=Comment(comment=comment,post_id=post_id)
        new_comment.save_c()
        return redirect(url_for('.comment',post_id=post_id))
    return render_template('comment.html',form=form,post=post,all_comments=all_comments)
@main.route ('/index/<int:post_id>delete',methods=['GET','POST'])
@login_required
def delete(post_id):
    current_post=Post.query.filter_by(id=post_id).first()
    # if current_post
    if current_post.user != current_user:
        abort(403)
    db.session.delete(current_post)
    db.session.commit()
    return redirect(url_for('.index'))
@main.route('/index/<int:id>/delet',methods=['GET','POST'])
@login_required
def delet(id):
    comment= Comment.query.filter_by(id = id).first()
    if comment is None:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('main.fund'))
    # return render_template('comment.html',current_post=current_post)
@main.route('/profile/<int:post_id>/',methods=['GET','POST'])
@login_required
def update_post(post_id):
    current_post= Post.query.filter_by(id = post_id).first()
    if current_post.user != current_user:
        abort(403)
    form=UpdatePostForm()
    if form.validate_on_submit():
        current_post.title=form.title.data
        current_post.category=form.category.data
        current_post.post=form.post.data
        # db.session.add(current_post)
        db.session.commit()
        return redirect(url_for('.index'))
    elif request.method=='GET':
        form.title.data=current_post.title
        form.category.data=current_post.category
        form.post.data=current_post.post
    return render_template('comment.html',form=form)


@main.route('/user/<name>/update/pic',methods=['GET','POST'])
@login_required
def update_pic(name):
    user=User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.image_pic_path=path
        db.session.commit()
        return redirect(url_for('main.index',name=name))
    return render_template('profile.html')
    
@main.route('/create',methods = ['GET','POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        Post.profile_pic_path = form.image.data 
        user_id = current_user
        new_fund = Post(title = form.title.data, category = form.category.data,description=form.description.data,content = form.content.data,user_id=current_user._get_current_object().id, profile_pic_path = form.image.data )
        new_fund.save_post()
    
        return redirect(url_for('.funds'))
    title = 'Add a post'
    return render_template('create.html',title = title,form = form)