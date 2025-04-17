from flask import Blueprint, request, jsonify
from app.models import db, Product

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products])

@bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    product = Product(name=data['name'], description=data['description'], price=data['price'], stock=data['stock'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created'}), 201
