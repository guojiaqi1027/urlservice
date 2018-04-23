import json
from flask import Response

def jsonify(*args, **kwargs):
    return Response(jsonifyAsText(*args, **kwargs), mimetype="application/json")


def success_ret(**kwargs):
    return jsonify(success=1, **kwargs)


def failure_ret(**kwargs):
    return jsonify(success=0, **kwargs)


def jsonifyAsText(*args, **kwargs):
    return json.dumps(dict(*args, **kwargs))
