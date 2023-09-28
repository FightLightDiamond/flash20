# from flask_sqlalchemy import SQLAlchemy

from library import createApp

app = createApp()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=True, use_reloader=True)
