#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from . import main
from .forms import PostForm, CommentForm
from flask_login import current_user
from .. import db
from datetime import datetime


@main.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    from ..models.post import Post
    form = PostForm()
    if current_user.id and form.validate_on_submit():
        content = form.body.data
        # user_id = current_user._get_current_object()
        # publish_date = datetime.utcnow()
        user_id = current_user.id

        post = Post(content)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    
        # query posts on home page
    posts = Post.query.order_by(Post.publish_date.desc()).all()

    """
        function to return Hello HBNB!
    """
    return render_template("index.html", form=form, posts=posts)


if __name__ == '__main__':
        main.run(host='0.0.0.0', port=5000)


# begin flask page rendering
# @main.teardown_appcontext
# def teardown_db(exception):
#     """
#     after each request, this method calls .close() (i.e. .remove()) on
#     the current SQLAlchemy Session
#     """
#     cursor.close()