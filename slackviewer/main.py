import webbrowser

from slackviewer.app import app as application
from slackviewer.archive import extract_archive
from slackviewer.reader import Reader

import os

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

application.debug = os.environ.get("FLASK_DEBUG", False)
application.no_sidebar = os.environ.get("SEV_NO_SIDEBAR", False)
application.no_external_references = os.environ.get("SEV_NO_EXTERNAL_REFERENCES", False)

path = extract_archive(os.environ.get("SEV_ARCHIVE"))
reader = Reader(path)
stack.channels = reader.compile_channels(os.environ.get("SEV_CHANNELS", None))
stack.groups = reader.compile_groups()
stack.dms = reader.compile_dm_messages()
stack.dm_users = reader.compile_dm_users()
stack.mpims = reader.compile_mpim_messages()
stack.mpim_users = reader.compile_mpim_users()

if __name__ == '__main__':
    application.run(
        host=os.environ.get("SEV_IP")
    )
