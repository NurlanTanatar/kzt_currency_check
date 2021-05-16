import sys
from PyQt5 import QtWidgets
from designqt5 import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = mywindow()
    win.show()
    sys.exit(app.exec_())