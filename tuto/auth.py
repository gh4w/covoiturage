import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from tuto.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/inscription', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = "le nom est obligatoire"
        elif not password:
            error = "le mot de passe est obligatoire"
        elif db.execute('select id from user where username = ?', (username,)).fetchone() is not None:
            error = "l'utilisateur {} existe déjà".format(username)

        if error is None:
            db.execute('insert into user(username, password) values(?, ?)', (username, generate_password_hash(password)))
            db.commit()
            return redirect(url_for('auth.login'))
        else:
            flash(error)
    else:
        return render_template("auth/register.html")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('select * from user where username = ?', (username, )).fetchone()

        if user is None:
            error = "nom d'utilisateur incorrect"
        elif not check_password_hash(user['password'], password):
            error = "mot de passe incorrect"

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            flash(error)

    return render_template("auth/login.html")

# nb: cette fonction sera appelée avant chaque requête, 
# même si la requête ne concerne pas ce blueprint.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('select * from user where id = ?', (user_id,)).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# décorateur d'une vue pour laquelle on veut que l'utilisateur soit loggué
def login_required(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        else:
            return view(**kwargs)

    return wrapped_view





