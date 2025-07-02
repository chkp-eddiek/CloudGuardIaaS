from flask import Flask, request, jsonify
from src.api.endpoints import api_blueprint
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Register the API blueprint
app.register_blueprint(api_blueprint)

@app.route('/')
def home():
    return "Welcome to the GitHub POST API!"

if __name__ == '__main__':
    app.run(debug=True)