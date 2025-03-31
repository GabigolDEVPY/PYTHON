import requests
from flask import jsonify

def retornar(valor, numero):
    result = (valor * numero)
    return result