# from flask_sqlalchemy import SQLAlchemy

from library import createApp

app = createApp()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/b")
def b():
    return "<p>BHello, World!</p>"

@app.get("/a")
def a():
    return "<p>A!</p>"

@app.post("/a")
def pa():
    return "<p> POST A!</p>"

@app.patch("/a")
def dpa():
    return "<p> patch A!</p>"

@app.delete("/a")
def ddpa():
    return "<p> delete A!</p>"