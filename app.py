from flask import Flask
from flask_cors import CORS
from routes.product_routes import product_bp
from utils.db import mongo
import config

app = Flask(__name__)
CORS(app)

# Database setup
app.config["MONGO_URI"] = config.MONGO_URI
mongo.init_app(app)

# Register routes
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
