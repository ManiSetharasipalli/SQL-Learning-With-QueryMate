from sqlalchemy import UniqueConstraint
from . import db
from flask_login import UserMixin


# Database Models
class User(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.userid)


class UserInteraction(db.Model):
    interactionId = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False)
    ConceptName = db.Column(db.String(100), nullable=False ,index=True)
    quiz_result = db.Column(db.Boolean)
    exercise_result = db.Column(db.Boolean)

    __table_args__ = (UniqueConstraint('userid', 'ConceptName', name='_user_concept_uc'),)


class MultipleChoiceQuestion(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), nullable=False)
    ConceptName = db.Column(db.String(100), nullable=False)


class MultipleChoiceAnswer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('multiple_choice_question.question_id'), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)


class Exercise(db.Model):
    ex_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    ConceptName = db.Column(db.String(100), nullable=False)
    hint = db.Column(db.String(200), nullable=False)