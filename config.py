import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
        flask Config
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI')

class TestConfig(object):
    """
        Used to pseudo initialize mongo and flask env for unittesting
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI')
    TESTING = True

