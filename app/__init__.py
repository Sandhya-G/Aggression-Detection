from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
#imported at the bottom and not at the top of the script to avoid circular imports
from app import routes