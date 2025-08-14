import sys
sys.dont_write_bytecode = True
from flask import Flask
from vagas_route import vagas_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(vagas_bp)
    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5700, host="0.0.0.0")