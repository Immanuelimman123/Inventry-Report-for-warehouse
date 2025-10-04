from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Product, Location, ProductMovement, InitialStock

main = Blueprint('main', __name__)

# ---------------------------
# Redirect home '/' to /products
# ---------------------------
@main.route('/')
def home():
    return redirect(url_for('main.products'))
    
# ============================
# --- Products CRUD ---
# ============================
@main.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@main.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = Product(
            product_id=request.form['id'],
            name=request.form['name'],
            quantity=request.form['quantity']
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('main.products'))
    return render_template('add_product.html')

@main.route('/products/edit/<string:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        db.session.commit()
        return redirect(url_for('main.products'))
    return render_template('edit_product.html', product=product)

# ============================
# --- Locations CRUD ---
# ============================
@main.route('/locations')
def locations():
    locations = Location.query.all()
    return render_template('locations.html', locations=locations)

@main.route('/locations/add', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        loc = Location(
            location_id=request.form['id'],
            name=request.form['name']
        )
        db.session.add(loc)
        db.session.commit()
        return redirect(url_for('main.locations'))
    return render_template('add_location.html')

@main.route('/locations/edit/<string:location_id>', methods=['GET', 'POST'])
def edit_location(location_id):
    loc = Location.query.get_or_404(location_id)
    if request.method == 'POST':
        loc.name = request.form['name']
        db.session.commit()
        return redirect(url_for('main.locations'))
    return render_template('edit_location.html', location=loc)

# ============================
# --- Product Movements CRUD ---
# ============================
@main.route('/movements')
def movements():
    movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).all()
    return render_template('movements.html', movements=movements)

@main.route('/movements/add', methods=['GET', 'POST'])
def add_movement():
    products = Product.query.all()
    locations = Location.query.all()
    if request.method == 'POST':
        move = ProductMovement(
            movement_id=request.form['id'],
            product_id=request.form['product'],
            from_location=request.form.get('from_location') or None,
            to_location=request.form.get('to_location') or None,
            qty=int(request.form['qty'])
        )
        db.session.add(move)
        db.session.commit()
        return redirect(url_for('main.movements'))
    return render_template('add_movement.html', products=products, locations=locations)

# ============================
# --- Inventory Report ---
# ============================
@main.route('/report')
def report():
    locations = Location.query.all()
    products = Product.query.all()
    
    report_data = []
    for loc in locations:
        for prod in products:
            # Get initial stock if you’ve defined it per product-location, else default to 0
            initial_stock = db.session.query(db.func.sum(InitialStock.qty))\
                .filter_by(location_id=loc.location_id, product_id=prod.product_id).scalar() or 0

            # Total qty moved into this location
            in_qty = db.session.query(db.func.sum(ProductMovement.qty))\
                .filter_by(to_location=loc.location_id, product_id=prod.product_id).scalar() or 0
            # Total qty moved out of this location
            out_qty = db.session.query(db.func.sum(ProductMovement.qty))\
                .filter_by(from_location=loc.location_id, product_id=prod.product_id).scalar() or 0

            # Calculate final stock balance
            balance = initial_stock + in_qty - out_qty

            report_data.append({
                'product': prod.name,
                'location': loc.name,
                'qty': balance
            })

    return render_template('report.html', report=report_data)

