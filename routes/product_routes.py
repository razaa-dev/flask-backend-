from flask import Blueprint, jsonify, request
from models.product_model import (
    get_all_products,
    get_product_by_id,
    add_product,
    update_product,
    delete_product,
)

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = get_all_products()
    for p in products:
        p["_id"] = str(p["_id"])  # convert ObjectId to string
    return jsonify(products)

@product_bp.route("/products/<id>", methods=["GET"])
def get_product(id):
    product = get_product_by_id(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product["_id"] = str(product["_id"])
    return jsonify(product)

@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("price"):
        return jsonify({"error": "Missing fields"}), 400
    result = add_product(data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

@product_bp.route("/products/<id>", methods=["PUT"])
def update_product_route(id):
    data = request.get_json()
    result = update_product(id, data)
    return jsonify({"updated_count": result.modified_count})

@product_bp.route("/products/<id>", methods=["DELETE"])
def delete_product_route(id):
    result = delete_product(id)
    return jsonify({"deleted_count": result.deleted_count})
