import sys
from PyQt5.QtWidgets import *
from transaction_functions import *
from databases import *
from graphical_interface import *
from GUI_functions import *

class BudgetTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        gui_signals(self.ui)
        updateCategoryComboBox(self.ui)
        refreshTransactionTable(self.ui)
        loadRemoveTransactionComboBox(self.ui)
        

if __name__ == '__main__':
    create_tables()
    app = QApplication(sys.argv)
    window = BudgetTrackerApp()
    window.show()
    sys.exit(app.exec_())