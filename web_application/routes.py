from flask import Blueprint, render_template, session, request, jsonify, render_template_string
from .helpers import *
from .models import MultipleChoiceQuestion, UserInteraction
import mysql.connector
from .query_editor import connection,execute_query,get_table_list

routes = Blueprint('routes',__name__)


@routes.route("/")
def home():
    username=session.get('username')
    return render_template("home.html",username=username)


@routes.route("/Quiz", methods=['POST'])
def quiz():
    que = request.form['question']
    ans = request.form['answer'].strip()
    is_correct, question_id = check_multiple_choice_answer(que,ans)
    result = 1 if is_correct else 0

    if current_user.is_authenticated:
        question = MultipleChoiceQuestion.query.filter_by(question_id=question_id).first()
        if question:
            update_user_interaction_for_quiz(question.ConceptName, result)

    return jsonify({'result': result})


@routes.route("/exercise", methods=['POST'])
def exercise():
    question = request.form['question']
    answer = request.form['answer'].lower()
    is_correct, concept_name = check_exercise_answer(question, answer)
    result = 1 if is_correct else 0

    if current_user.is_authenticated:
        update_user_interaction_for_exercise(concept_name, result)

    return jsonify({'result': result})


@routes.route("/query_editor", methods=['GET', 'POST'])
def display_data():
    try:
        if request.method == 'POST':
            sql_query = request.form['sql_query']
            cursor = execute_query(sql_query)

            if sql_query.strip().lower().startswith('select'):
                data = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                cursor.close()

                return render_template('query_results.html', column_names=column_names, data=data, database=get_table_list())
            else:
                connection.commit()
                success_message = f"Operation successful: {cursor.rowcount} rows affected."
                cursor.close()

                return render_template_string('''
                    <div class="alert alert-success">
                        <p style="padding:15px;color:green"><samp>{{ success_message }}</samp></p>
                    </div>
                ''', success_message=success_message)
        else:
            return render_template('query_editor.html', column_names="Output will be shown here", data=[], sql_query="", database=get_table_list())

    except mysql.connector.Error as err:
        return render_template_string('''
            <div class="alert alert-danger">
                <p style="padding:15px;color:red"><samp>{{ error_message }}</samp></p>
            </div>
        ''', error_message=err.msg)


@routes.route("/profile")
def userProfile():
    username = current_user.username
    user_email = current_user.email
    completed_concepts = UserInteraction.query.filter_by(userid=current_user.userid).all()
    return render_template("profile.html", username=username, user_email=user_email,
                           completed_concepts=completed_concepts)






