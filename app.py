import socket

from flask import Flask

app = Flask(__name__)


@app.get("/")
def where_am_i():
    return f"Ciao! Sono deployato su {socket.gethostbyname(socket.gethostname())}\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
