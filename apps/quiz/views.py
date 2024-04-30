from apps.quiz.forms import UserForm
from apps.app import db
from apps.quiz.models import User
from flask import Blueprint, render_template, redirect, url_for



quiz = Blueprint(
    "quiz",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@quiz.route("/")
def index():
    return render_template("quiz/index.html")


@quiz.route("/users/new", methods=["GET", "POST"])
def create_user() :
    form = UserForm()

    if form.validate_on_submit() :
        user = User(
            username=form.username.data,
            password=form.password.data,
            textword=form.textword.data,
            answer=form.answer.data,
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("quiz.users"))
    return render_template("quiz/create.html", form=form)

@quiz.route("/users")
def users():
    users = User.query.all()
    return render_template("quiz/index.html", users=users)

@quiz.route("/users/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    form = UserForm()

    user = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        user.username = form.username.data
        user.password=form.password.data
        user.textword=form.textword.data
        user.answer=form.answer.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("quiz.users"))
    
    return render_template("quiz/edit_users.html", user=user, form=form)

@quiz.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("quiz.users"))

@quiz.route("/users/<user_id>/start", methods=["GET"])
def start_quiz(user_id):
    user=User.query.filter_by(id=user_id).first()
    return render_template("quiz/start.html", user=user)