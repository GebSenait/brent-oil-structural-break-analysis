"""
Task-3: Flask application for Change Point Analysis dashboard API.
Serves Brent returns/prices, events (with optional category filter), and change point posterior summary.
"""
from flask import Flask
from flask_cors import CORS

from backend.routes.api import api

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(api)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
