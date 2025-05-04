# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Question, Score
import uuid
from datetime import datetime
from sqlalchemy.orm import joinedload

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db.init_app(app)


# Oturum yönetimi için yardımcı fonksiyonlar
def create_new_user(username=None):
    """Yeni kullanıcı oluşturur"""
    if not username:
        username = f"guest_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    new_user = User(
        username=username,
        email=f"{username.replace(' ', '_')}@quiz.com"
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.id


@app.before_request
def before_request():
    # Eğer formdan isim gelmişse onu kullan
    if request.method == 'POST' and 'username' in request.form:
        username = request.form['username'].strip()
        if len(username) >= 3:
            session['username'] = username
            session['user_id'] = create_new_user(username)

    # Oturum kontrolü
    if 'user_id' not in session:
        session['user_id'] = create_new_user()
        session['new_session'] = True


@app.after_request
def after_request(response):
    if 'new_session' in session:
        session.pop('new_session')
    return response


@app.route('/reset_session_flags', methods=['POST'])
def reset_session_flags():
    session.clear()
    return '', 204


@app.route('/')
def index():
    return redirect(url_for('quiz'))


@app.route('/quiz', methods=['GET'])
def quiz():
    questions = Question.query.all()
    user_id = session.get('user_id')

    # Skor sorguları
    user_high_score = (db.session.query(Score)
                       .filter_by(user_id=user_id)
                       .order_by(Score.score.desc())
                       .first())

    overall_high_score = (db.session.query(Score, User)
                          .join(User)
                          .order_by(Score.score.desc())
                          .first())

    return render_template('quiz.html',
                           questions=questions,
                           user_high_score=user_high_score.score if user_high_score else 0,
                           overall_high_score=f"{overall_high_score.Score.score} ({overall_high_score.User.username})"
                           if overall_high_score else "0")


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if 'user_id' not in session:
        return redirect(url_for('quiz'))

    # Skor hesaplama
    score = sum(1 for question in Question.query.all()
                if request.form.get(f'question_{question.id}') == question.correct_option)

    # Skor kaydetme
    new_score = Score(score=score, user_id=session['user_id'])
    db.session.add(new_score)
    db.session.commit()

    # Skor bilgilerini getir
    user_high_score = (db.session.query(Score)
                       .filter_by(user_id=session['user_id'])
                       .order_by(Score.score.desc())
                       .first())

    overall_high_score = (db.session.query(Score, User)
                          .join(User)
                          .order_by(Score.score.desc())
                          .first())

    current_user = User.query.get(session['user_id'])

    return render_template('result.html',
                           score=score,
                           username=current_user.username,
                           user_high_score=f"{user_high_score.score} " if user_high_score else "0",
                           overall_high_score=f"{overall_high_score.Score.score} ({overall_high_score.User.username})"
                           if overall_high_score else "0")


@app.route('/dashboard')
def dashboard():
    # En iyi 10 skor
    top_scores = (db.session.query(Score, User)
                  .join(User)
                  .order_by(Score.score.desc())
                  .limit(10)
                  .all())

    # Mevcut kullanıcının skoru
    current_score = None
    if 'user_id' in session:
        current_score = (Score.query
                         .filter_by(user_id=session['user_id'])
                         .order_by(Score.score.desc())
                         .first())

    return render_template('dashboard.html',
                           top_scores=top_scores,
                           current_score=current_score)


@app.route('/reset_session')
def reset_session():
    session.clear()
    return redirect(url_for('quiz'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)