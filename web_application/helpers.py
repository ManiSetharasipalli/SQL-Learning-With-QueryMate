import re
from werkzeug.security import generate_password_hash
from . import db
from .models import UserInteraction, MultipleChoiceQuestion, MultipleChoiceAnswer, Exercise, User
from flask_login import current_user
from sqlalchemy import exc


def is_valid_email(email):
    # Regular expression for email validation
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None


MIN_PASSWORD_LENGTH = 8
MIN_LOWERCASE_CHARS = 2
MIN_SPECIAL_CHARS = 1


# Function to validate password complexity
def is_valid_password(password):
    # Check minimum length
    if len(password) < MIN_PASSWORD_LENGTH:
        return False

    # Check minimum lowercase characters
    if sum(1 for char in password if char.islower()) < MIN_LOWERCASE_CHARS:
        return False

    # Check for at least one special character
    special_chars_regex = r'[!@#$%^&*()-_=+{};:,<.>?]'
    if not re.search(special_chars_regex, password):
        return False

    # All checks passed
    return True


def passwords_match(password, confirm_password):
    return password == confirm_password


# For Adding User Interaction
def log_interaction(concept_name):
    if current_user.is_authenticated:
        try:
            interaction = UserInteraction(userid=current_user.userid, ConceptName=concept_name)
            db.session.add(interaction)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()


def get_concept_data(concept):
    log_interaction(concept)
    question = MultipleChoiceQuestion.query.filter_by(ConceptName=concept).first()
    if question:
        answers = MultipleChoiceAnswer.query.filter_by(question_id=question.question_id).all()
    else:
        answers = []
    exercise = Exercise.query.filter_by(ConceptName=concept).first()
    return question, answers, exercise


def check_multiple_choice_answer(que,ans):
    question=MultipleChoiceQuestion.query.filter_by(question=que).first()
    answer = MultipleChoiceAnswer.query.filter_by(answer=ans,question_id=question.question_id).first()

    if answer and answer.is_correct == 1:
        return True, answer.question_id
    return False, answer.question_id if answer else None


def update_user_interaction_for_quiz(concept_name, result):
    if current_user.is_authenticated:
        exist_interaction = UserInteraction.query.filter_by(ConceptName=concept_name, userid=current_user.userid).first()
        if exist_interaction:
            exist_interaction.quiz_result = result
            db.session.add(exist_interaction)
            db.session.commit()


def check_exercise_answer(question, answer):
    res = Exercise.query.filter_by(question=question).first()
    if res and res.answer.lower() == answer:
        return True, res.ConceptName
    return False, res.ConceptName if res else None


def update_user_interaction_for_exercise(concept_name, result):
    if current_user.is_authenticated:
        exist_interaction = UserInteraction.query.filter_by(ConceptName=concept_name, userid=current_user.userid).first()
        if exist_interaction:
            exist_interaction.exercise_result = result
            db.session.add(exist_interaction)
            db.session.commit()


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()


def create_user(username, email, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user




