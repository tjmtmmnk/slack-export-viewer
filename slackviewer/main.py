from slackviewer.app import app as application
from slackviewer.archive import extract_archive
from slackviewer.reader import Reader
from slackviewer.appconfig import set_env_params

import os

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

set_env_params()

path = extract_archive(os.environ.get("SEV_ARCHIVE"))
reader = Reader(path)
stack.channels = reader.compile_channels(os.environ.get("SEV_CHANNELS", None))
stack.groups = reader.compile_groups()
stack.dms = reader.compile_dm_messages()
stack.dm_users = reader.compile_dm_users()
stack.mpims = reader.compile_mpim_messages()
stack.mpim_users = reader.compile_mpim_users()

if __name__ == '__main__':
    if not application.is_test:
        application.run(
            host=os.environ.get("SEV_IP", '0.0.0.0'),
            port=os.environ.get("SEV_PORT", 5000)
        )