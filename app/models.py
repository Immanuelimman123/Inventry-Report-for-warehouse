from . import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"

class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Location {self.name}>"

class ProductMovement(db.Model):
    __tablename__ = 'product_movement'
    movement_id = db.Column(db.String, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    from_location = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=True)
    to_location = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=True)
    product_id = db.Column(db.String, db.ForeignKey('product.product_id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Movement {self.movement_id}: {self.product_id} {self.qty}>"

class InitialStock(db.Model):
    __tablename__ = 'initial_stock'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    location_id = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False, default=0)

    product = db.relationship('Product', backref='initial_stocks')
    location = db.relationship('Location', backref='initial_stocks')

    def __repr__(self):
        return f"<InitialStock {self.product.name} - {self.location.name}: {self.qty}>"

