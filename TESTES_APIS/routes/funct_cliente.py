from flask import Blueprint, jsonify, make_response

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route("/cliente/add=<user>", methods=["GET"])
def get_user(user):
    user = user
    return make_response(jsonify(user))