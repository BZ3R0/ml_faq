# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__, instance_relative_config=True)

# Config
app.config.from_object('chatbot.config')

# Flask-SQLAlchemy
db = SQLAlchemy(app)

# Automatically create tables
from .model import aprendizado
db.create_all()

# Blueprints
from .views.bot import mod_bot
app.register_blueprint(mod_bot)
