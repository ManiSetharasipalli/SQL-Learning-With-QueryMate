from flask import Flask, request, jsonify
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


db=SQLAlchemy()


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="Dreams2030ManiS"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:5555@localhost/sql_learning'
    db.init_app(app)
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    from .routes import routes
    from .auth import auth
    from .page_routes import pages
    from .models import  User,UserInteraction,MultipleChoiceQuestion,MultipleChoiceAnswer,Exercise
    from .chatbot import QueryMate
    create_tables(app)
    QM = QueryMate()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.post("/predict")
    def predict():
        text = request.get_json().get("message")
        response = QM.get_response(text)
        message = {"answer": response}
        return jsonify(message)

    app.register_blueprint(routes,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    app.register_blueprint(pages,url_prefix="/")
    return app


# Create database tables
def create_tables(app):
    with app.app_context():
        db.create_all()

