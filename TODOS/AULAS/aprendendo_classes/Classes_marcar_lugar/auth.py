import sys 
sys.dont_write_bytecode = True
from functools import wraps
from flask import request, abort
from db import execute_comand 

def auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = (request.get_json())['nome']
        user_data = execute_comand("SELECT nome FROM users WHERE nome = %s", user)
        if not user_data:
            return abort(404)
        return f(*args, **kwargs)
    
    return decorated_function