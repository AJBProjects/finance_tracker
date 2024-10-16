import sqlite3

def connect_db():
    return sqlite3.connect('finances.db')

def create_tables():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS transactions(id INTEGER PRIMARY KEY AUTOINCREMENT, type TEXT, amount REAL, category TEXT, date TEXT, description TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS budget_goal(monthly REAL)")
    connection.close()

def get_transactions():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id, type, amount, category, date, description FROM transactions")
    transactions = cursor.fetchall()
    connection.close()
    return transactions

def get_transaction_IDs():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM transactions")
    ids = cursor.fetchall()
    connection.close()
    return [str(id_tuple[0]) for id_tuple in ids]