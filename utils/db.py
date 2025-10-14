from flask_pymongo import PyMongo
from flask import current_app

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = current_app.config.get("MONGO_URI", "mongodb://localhost:27017/flask_crud")
    mongo.init_app(app)
    return mongo
