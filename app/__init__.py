from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow React frontend to communicate with the backend

from app import routes
