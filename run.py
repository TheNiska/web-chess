from flask import Flask
from chess import main_bp

app = Flask(__name__)
app.secret_key = "vLi!4i9Wclwl8wL"
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
