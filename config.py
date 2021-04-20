from flask import Flask
from flask_cors import CORS
from time_manager import TimeManager

# все необходимые константы

APP = Flask(__name__)
cors = CORS(APP, resources={r"/api/*": {"origins": "*"}})
USER_ID = -1

TIME = TimeManager()


def check_token(token):
    return token == 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHN'
