from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def categories():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    return render_template('categories.html', categories=categories)

@app.route('/add_categories', methods=['POST'])
def add_category():
    try:
        name = request.form['name']
        if not name:
           flash('Category name is required!')
           return redirect(url_for('categories'))

        conn = get_db_connection()
        conn.execute('INSERT INTO categories (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        flash(' thank you!Category added successfully!')
    except Exception as e:
        flash(f"Error: {str(e)}")
    return redirect(url_for('categories'))

@app.route('/products')
def products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    categories=conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    return render_template('products.html', products=products,categories=categories)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    category_id = request.form['category_id']
    price = request.form['price']
    quantity = request.form['quantity']
    description = request.form['description']

    if not name or not category_id or not price or not quantity :
        flash("product name cannot be empty")
        return redirect(url_for('products'))

    conn = get_db_connection()
    conn.execute('INSERT INTO products (name, category_id, price, quantity, description) VALUES (?, ?, ?, ?, ?)',
                 (name, category_id, price, quantity, description))
    conn.commit()
    conn.close()
    flash('Product added successfully!')
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    conn = get_db_connection()
    sales = conn.execute('SELECT * FROM sales').fetchall()
    conn.close()
    return render_template('sales.html', sales=sales)

@app.route('/add_sale', methods=['POST'])
def add_sale():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    total_price = request.form['total_price']

    if not product_id or not quantity or not total_price:
        flash('All fields are required!')
        return redirect(url_for('sales'))

    conn = get_db_connection()
    conn.execute('INSERT INTO sales (product_id, quantity, total_price) VALUES (?, ?, ?)',
                 (product_id, quantity, total_price))
    conn.commit()
    conn.close()
    flash('Sale recorded successfully!')
    return redirect(url_for('sales'))

if __name__ == '__main__':
    app.run(debug=True)