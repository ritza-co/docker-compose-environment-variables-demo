import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'The host secret is {os.environ.get("SECRET_ENV")} '
