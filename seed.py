from app import create_app
from app.extensions import db
from app.models import User, Product, Transaction
from datetime import datetime, timezone
import random

app = create_app()

with app.app_context():
    # Clear existing data (opsional, hati-hati di production!)
    Transaction.query.delete()
    Product.query.delete()
    User.query.delete()

    # Tambah user
    users = [
        User(name="Alice", email="alice@example.com", password="alice123"),
        User(name="Bob", email="bob@example.com", password="bob123"),
        User(name="Charlie", email="charlie@example.com", password="charlie123")
    ]
    db.session.add_all(users)
    db.session.commit()

    # Tambah produk
    products = [
        Product(name="Sabun Organik", description="Sabun ramah lingkungan", price=15000, stock=100),
        Product(name="Kopi Lokal", description="Kopi dari petani lokal", price=40000, stock=50),
        Product(name="Totebag Daur Ulang", description="Tas ramah lingkungan dari bahan daur ulang", price=25000, stock=80)
    ]
    db.session.add_all(products)
    db.session.commit()

    # Tambah transaksi random
    transactions = [
        Transaction(
            user_id=random.choice(users).id,
            product_id=random.choice(products).id,
            quantity=2,
            total_price=2 * products[0].price,
            timestamp=datetime.now(timezone.utc)
        )
        for _ in range(5)
    ]
    db.session.add_all(transactions)
    db.session.commit()

    print("✅ Data seed berhasil ditambahkan!")
