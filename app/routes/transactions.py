from flask import Blueprint, request, jsonify
from app.models import db, Transaction, Product, User

bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@bp.route('/', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([{
        'id': t.id,
        'user_id': t.user_id,
        'product_id': t.product_id,
        'quantity': t.quantity,
        'total_price': t.total_price,
        'timestamp': t.timestamp.isoformat()
    } for t in transactions])

@bp.route('/', methods=['POST'])
def create_transaction():
    data = request.json
    product = Product.query.get(data['product_id'])

    if product and product.stock >= data['quantity']:
        total = product.price * data['quantity']
        transaction = Transaction(
            user_id=data['user_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            total_price=total
        )
        product.stock -= data['quantity']
        db.session.add(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction successful'}), 201
    return jsonify({'message': 'Insufficient stock'}), 400
