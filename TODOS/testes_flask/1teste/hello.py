from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")  # Renderiza o HTML

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
