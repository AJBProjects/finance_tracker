from databases import *

# This function sets the monthly budget value. Float must be input or false is returned
# Inputs budget into budget_goal table, if value already exists, replace it
def set_monthly_budget(budget): 
    if (isinstance(budget, float) or isinstance(budget, int)):
        float(budget)
    else:
        print("Only integers or floats accepted")
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * from budget_goal")
        budgetCheck = cursor.fetchone()
        if budgetCheck is not None:
            cursor.execute("DELETE FROM budget_goal")
        cursor.execute("INSERT INTO budget_goal (monthly) VALUES (?)", (budget,))
    except sqlite3.Error as error:
        print(f"Error: {error}")
    connection.commit()
    connection.close()

# This function adds a transaction to the transactions database. ID is autoincremented and doesn't need to be set.
def add_transaction(type, amount, category, date, description):
    connection = connect_db()
    cursor = connection.cursor()
    # add entry
    try:
        cursor.execute("INSERT INTO transactions (type, amount, category, date, description) VALUES (?,?,?,?,?)", (type, amount, category, date, description))
    except sqlite3.Error as error:
        print(f"Error: {error}")
    connection.commit()
    connection.close()

# Removes transaction from the database based on ID
def remove_transaction(id):
    connection = connect_db()
    cursor = connection.cursor()
    # Remove by ID
    try:
        cursor.execute("DELETE FROM transactions WHERE id = ?", (id,))
    except sqlite3.Error as error:
        print(f"Error: {error}")

    connection.commit()
    connection.close()