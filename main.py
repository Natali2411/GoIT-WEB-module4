import os
import threading
from dotenv import load_dotenv

load_dotenv()

from app import run_flask_app
from socket_server import run_server

FLASK_HOST = os.getenv("FLASK_HOST")
HOST = os.getenv("HOST")
SERVER_PORT = int(os.getenv("SERVER_PORT"))
FLASK_PORT = int(os.getenv("FLASK_PORT"))

server = threading.Thread(target=run_server, args=(HOST, SERVER_PORT))
flask_server = threading.Thread(target=run_flask_app, args=(FLASK_HOST, FLASK_PORT,))

server.start()
flask_server.start()
server.join()
flask_server.join()

