import json
from math import atanh
from flask import Blueprint, make_response, jsonify, request
from vagas_functs import Vagas
from auth import auth


vagas_bp = Blueprint("vagas", __name__)

@vagas_bp.route("/vagas", methods=["GET"])
def return_home():
    return make_response(jsonify(Vagas.listar_lugares()))


@vagas_bp.route("/marcar", methods=["POST"])
@auth
def marcar():
    data = request.get_json()
    result = Vagas.marcar_lugar(data)
    if result == 0:
        return jsonify("Não foi possível marcar vaga, já está em uso")
    return data

@vagas_bp.route("/desmarcar", methods=["PUT"])
@auth
def desmarcar():
    data = request.get_json()
    result = Vagas.desmarcar_lugar(data)
    if result == 0:
        return jsonify("Não foi desmarcaar vaga, já está em uso")
    return data