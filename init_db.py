# import sqlite3

# def init_db():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()

#     # Create tables
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS categories (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL UNIQUE
#     )
#     ''')

#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         category_id INTEGER,
#         price REAL,
#         quantity INTEGER,
#         description TEXT,
#         FOREIGN KEY (category_id) REFERENCES categories(id)
#     )
#     ''')

#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS sales (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         product_id INTEGER,
#         quantity INTEGER,
#         total_price REAL,
#         sold_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         FOREIGN KEY (product_id) REFERENCES products(id)
#     )
#     ''')

#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     init_db()





import sqlite3

# 1️⃣ Connect to your SQLite database file
conn = sqlite3.connect("database.db")

# 2️⃣ Create a cursor to run SQL commands
cursor = conn.cursor()

# 3️⃣ List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# 4️⃣ Check all rows in the 'categories' table
cursor.execute("SELECT * FROM categories;")
categories = cursor.fetchall()
print("Categories table rows:", categories)

# 5️⃣ Check all rows in the 'products' table
cursor.execute("SELECT * FROM products;")
products = cursor.fetchall()
print("Products table rows:", products)

# 6️⃣ Check all rows in the 'sales' table
cursor.execute("SELECT * FROM sales;")
sales = cursor.fetchall()
print("Sales table rows:", sales)

# 7️⃣ Close the connection
conn.close()