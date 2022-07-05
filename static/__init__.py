from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
import logging

from static.logger_config import custom_logger

migrate = Migrate()

logger = logging.getLogger('gunicorn.error')
logger = custom_logger(logger)
cors = CORS()


def create_app(test_config=None):
    app = Flask(__name__)
    
    from static.todoApp.model.todo_list_model import Todo
    cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

    from static.todoApp import todo_list

    app.register_blueprint(todo_list, url_prefix='/api/v1')

    return app
