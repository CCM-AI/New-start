# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging

# Initialize Flask app and config
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Register routes
from routes.patient_routes import patient_bp
app.register_blueprint(patient_bp)

if __name__ == '__main__':
    app.run(debug=True)
