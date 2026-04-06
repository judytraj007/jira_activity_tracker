from flask import Flask, send_from_directory
from app.routes import bp

app = Flask(__name__, static_folder="frontend", static_url_path="")
app.register_blueprint(bp)


@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")


if __name__ == "__main__":
    app.run(debug=True)