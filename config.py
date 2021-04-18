from flask import Flask
from time_manager import TimeManager

WINDOWS_PATH = 'windows'

APP = Flask(__name__)
USER_ID = -1

TIME = TimeManager()


def check_token(token):
    return token == 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHN'
