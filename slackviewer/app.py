import flask

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack
    
app = flask.Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/channel/<name>/")
def channel_name(name):
    messages = stack.channels[name]
    channels = list(stack.channels.keys())
    groups = list(stack.groups.keys())
    dm_users = list(stack.dm_users)
    mpim_users = list(stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/group/<name>/")
def group_name(name):
    messages = stack.groups[name]
    channels = list(stack.channels.keys())
    groups = list(stack.groups.keys())
    dm_users = list(stack.dm_users)
    mpim_users = list(stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/dm/<id>/")
def dm_id(id):
    messages = stack.dms[id]
    channels = list(stack.channels.keys())
    groups = list(stack.groups.keys())
    dm_users = list(stack.dm_users)
    mpim_users = list(stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 id=id.format(id=id),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/mpim/<name>/")
def mpim_name(name):
    messages = stack.mpims[name]
    channels = list(stack.channels.keys())
    groups = list(stack.groups.keys())
    dm_users = list(stack.dm_users)
    mpim_users = list(stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users,
                                 no_sidebar=app.no_sidebar,
                                 no_external_references=app.no_external_references)


@app.route("/")
def index():
    channels = list(stack.channels.keys())
    if "general" in channels:
        return channel_name("general")
    else:
        return channel_name(channels[0])
