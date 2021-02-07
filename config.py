from os import getenv, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
env_file = path.join(basedir, ".env")

if path.exists(env_file):
    load_dotenv(env_file)


class Config(object):
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False