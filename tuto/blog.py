from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort
from tuto.auth import login_required
from tuto.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    sql = (
    'select p.id, title, body, created, author_id, username '
    'from post p join user u '
    'on p.author_id = u.id '
    'order by created desc '
    )
    posts = db.execute(sql).fetchall()
    return render_template('blog/index.html', posts=posts)

def get_post(id, check_author=True):

    sql = (
    'select p.id, title, body, created, author_id, username '
    'from post p join user u '
    'on p.author_id = u.id '
    'where p.id = ?'
    )

    post = get_db().execute(sql, (id,)).fetchone()

    if post is None:
        abort(404, "le post d'id {} n'existe pas".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'le titre est obligatoire'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('insert into post (title, body, author_id) values (?, ?, ?)', (title, body, g.user['id']))
            db.commit()
            return redirect(url_for('blog.index'))
    else:
        return render_template('blog/create.html')

@bp.route('/<int:id>/update',  methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'le titre est obligatoire'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('update post set title = ?, body = ? where id = ?', (title, body, id))
            db.commit()
            return redirect(url_for('blog.index'))
    else:
        return render_template('blog/update.html', post=post)
        
@bp.route('/<int:id>/delete',  methods=('GET', 'POST'))
@login_required
def delete(id):
    post = get_post(id)
    db = get_db()
    db.execute('delete from post where id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

