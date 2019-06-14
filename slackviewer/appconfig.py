import os
from os.path import join, dirname

from dotenv import load_dotenv

from slackviewer.app import app as application


def set_env_params():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    application.debug = _env_to_bool("FLASK_DEBUG")
    application.no_sidebar = _env_to_bool("SEV_NO_SIDEBAR")
    application.no_external_references = _env_to_bool("SEV_NO_EXTERNAL_REFERENCES")


def _env_to_bool(env, default_bool=False):
    env_str = os.environ.get(env)
    ret_bool = default_bool
    if env_str:
        ret_bool = env_str == "True"

    return ret_bool
