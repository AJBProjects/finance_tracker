from databases import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDoubleValidator
from transaction_functions import *

def gui_signals(ui):
    ui.addTransactionButton.clicked.connect(lambda: insertTransactionTable(ui))
    ui.typeComboBox.currentTextChanged.connect(lambda: updateCategoryComboBox(ui))
    ui.removeTransactionButton.clicked.connect(lambda: removeTransactionTable(ui))
    # Validator for amount
    amount_validator = QDoubleValidator(0.0,1000000000.0,2)
    amount_validator.setNotation(QDoubleValidator.StandardNotation)
    ui.amountLineEdit.setValidator(amount_validator)


def refreshTransactionTable(ui):
    transactions = get_transactions()
    ui.displayTransactionsTable.setRowCount(len(transactions))
    ui.displayTransactionsTable.setColumnCount(6)
    ui.displayTransactionsTable.setHorizontalHeaderLabels(["ID", "Type", "Amount", "Category", "Date", "Description"])

    # Populate the QTableWidget with data from the database
    for row_idx, transaction in enumerate(transactions):
        for col_idx, value in enumerate(transaction):
            # Create a QTableWidgetItem for each piece of data
            item = QTableWidgetItem(str(value))  # Convert the value to string to display in the table
            ui.displayTransactionsTable.setItem(row_idx, col_idx, item)

def insertTransactionTable(ui):
    typeText = ui.typeComboBox.currentText()
    amount = ui.amountLineEdit.text()
    category = ui.categoryComboBox.currentText()
    date = ui.addTransactionDateEdit.date().toString("MM-dd-yyyy")
    description = ui.addTransactionDescriptionTextBox.toPlainText()
    add_transaction(typeText, amount, category, date, description)
    refreshTransactionTable(ui)
    loadRemoveTransactionComboBox(ui)

def removeTransactionTable(ui):
    id = ui.removeTransactionIDComboBox.currentText()
    id = int(id)
    remove_transaction(id)
    refreshTransactionTable(ui)
    loadRemoveTransactionComboBox(ui)
    
def updateCategoryComboBox(ui):
    typeText = ui.typeComboBox.currentText()
    ui.categoryComboBox.clear()

    if (typeText == "Income"):
        ui.categoryComboBox.addItems(["Salary/Wages", "Business", "Investments", "Gifts", "Other"])
    else:
        ui.categoryComboBox.addItems(["Groceries", "Transportation", "Entertainment", "Housing", "Health/Medical", "Clothing", "Savings/Investments", "Reccuring Payments", "Personal Care", "Other"])

def loadRemoveTransactionComboBox(ui):
    ids = get_transaction_IDs()
    ui.removeTransactionIDComboBox.clear()
    ui.removeTransactionIDComboBox.addItems(ids)

