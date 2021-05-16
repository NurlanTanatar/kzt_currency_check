from PyQt5 import QtCore, QtGui, QtWidgets
import time, calendar
from kzt_exchangerates import Rates

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.rates = Rates()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(240)
        sizePolicy.setVerticalStretch(240)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Kazakh, QtCore.QLocale.Kazakhstan))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(150, 310, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(31)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(230, 310, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(12)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(300, 310, 51, 22))
        self.spinBox_3.setMinimum(2000)
        self.spinBox_3.setMaximum(int(time.asctime()[-4:]))
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 290, 201, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 430, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -30, 491, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/1.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 410, 61, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/dollar.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 340, 201, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.makeRequest)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "История курса тенге"))
        self.label.setText(_translate("MainWindow", "День             Месяц         Год"))
        self.label_2.setText(_translate("MainWindow", "0 тнг."))
        self.pushButton.setText(_translate("MainWindow", "Сделать запрос"))

    def getResult(self, day, month, year):

        result = self.rates.get_exchange_rates(["USD"], from_kzt=True, date=f"{int(day)}.{int(month)}.{int(year)}")['rates']['USD']
                      
        return result
    
    def makeRequest(self):

        # Получаем текущие значения из выпадающих списках.
        day_value = self.spinBox.value()
        month_value = self.spinBox_2.value()
        year_value = self.spinBox_3.value()
        if day_value > calendar.monthrange(int(year_value), int(month_value))[1]:
            day_value = calendar.monthrange(int(year_value), int(month_value))[1]
        # Выполняем запрос к API с выбранными данными.
        if year_value >= int(time.strftime('%Y')) and \
        month_value >= int(time.strftime('%m')) and \
        day_value > int(time.strftime('%d')):
            self.label_2.setText('тут нет прогнозов)')
            self.label_2.adjustSize()
        else:
            result = self.getResult(day_value, month_value, year_value)
        
            # Заменяем текст для доллара.
            self.label_2.setText('%s тнг.' % result)
            self.label_2.adjustSize()
