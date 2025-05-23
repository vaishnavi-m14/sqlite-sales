import sqlite3

# Connect to or create the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create 'sales' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

# Insert sample data
sample_data = [
    ('Apple', 10, 0.50),
    ('Banana', 20, 0.25),
    ('Orange', 15, 0.30),
    ('Grapes', 8, 0.70),
    ('Apple', 5, 0.50),
    ('Banana', 10, 0.25),
    ('Orange', 5, 0.30)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

conn.commit()
conn.close()

print("✅ sales_data.db created with sales table and data.")
