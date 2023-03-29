from webapp import create_app, db
from webapp.models.user import User
# ÷from webapp.models.comment import Comment
from webapp.models.post import Post, Comment, Tag
from webapp.models.roles import Roles

# env = os.environ.get('WEBAPP_ENV', 'dev')
# app = create_app('config.%sConfig' % env.capitalize())
app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Roles=Roles, Post=Post, Comment=Comment, Tag=Tag)


"""
    set debug=False in production mode
"""
if __name__ == '__main__':
    app.run(debug=1)