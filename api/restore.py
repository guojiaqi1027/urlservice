from flask import Blueprint, request
from action import restore as restore_action
from utils.response import success_ret, failure_ret

restore = Blueprint("restore", __name__, url_prefix="/restore")

@restore.route("/", methods=["POST", "GET"])
def restore_url():
    url = request.values.get("url", "")
    try:
        url = restore_action.get_url_restore(url)
        return success_ret(url=url)
    except Exception as e:
        return failure_ret(msg="Invalid URL")

