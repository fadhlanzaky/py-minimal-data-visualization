import os

class BaseConfig:
    """Base config"""
    ERROR_404_HELP = False
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    