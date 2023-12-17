import json
import os

from flask import Flask, render_template, request
from socket_client import socket_client

flask_app = Flask(__name__)

HOST = os.getenv("HOST")
SERVER_PORT = int(os.getenv("SERVER_PORT"))

def run_flask_app(host: str, port: int):
    print("Run Flask server")
    flask_app.run(host=host, port=port, debug=False)


@flask_app.route("/")
def index():
    return render_template("index.html")


@flask_app.route("/send_message", methods=["GET"])
def send_message():
    return render_template("message.html")


@flask_app.errorhandler(404)
def not_found(e):
    return render_template("error.html")


@flask_app.route("/message", methods=["POST"])
def post_message():
    username = request.form.get("username")
    message = request.form.get("message")
    data = {"username": username, "message": message}
    socket_client(HOST, SERVER_PORT, json.dumps(data))
    return render_template("success_msg.html", username=username, message=message)

