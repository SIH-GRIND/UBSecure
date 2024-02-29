# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'benchmark.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_benchmarking(object):
    def setupUi(self, benchmarking):
        benchmarking.setObjectName("benchmarking")
        benchmarking.resize(1242, 529)
        benchmarking.setMinimumSize(QtCore.QSize(1242, 529))
        benchmarking.setMaximumSize(QtCore.QSize(1242, 529))
        benchmarking.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.bluebar = QtWidgets.QLabel(benchmarking)
        self.bluebar.setGeometry(QtCore.QRect(0, 15, 1241, 45))
        self.bluebar.setStyleSheet("background-color: rgb(79, 135, 255);")
        self.bluebar.setText("")
        self.bluebar.setObjectName("bluebar")
        self.helpbutton = QtWidgets.QPushButton(benchmarking)
        self.helpbutton.setGeometry(QtCore.QRect(1100, 15, 121, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.helpbutton.setFont(font)
        self.helpbutton.setStyleSheet("background-color: rgb(79, 135, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.helpbutton.setObjectName("helpbutton")
        self.benchmarkingbuttton = QtWidgets.QPushButton(benchmarking)
        self.benchmarkingbuttton.setGeometry(QtCore.QRect(900, 15, 121, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.benchmarkingbuttton.setFont(font)
        self.benchmarkingbuttton.setStyleSheet("background-color: rgb(79, 135, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.benchmarkingbuttton.setObjectName("benchmarkingbuttton")
        self.hardeningbutton = QtWidgets.QPushButton(benchmarking)
        self.hardeningbutton.setGeometry(QtCore.QRect(500, 15, 121, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.hardeningbutton.setFont(font)
        self.hardeningbutton.setStyleSheet("background-color: rgb(79, 135, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.hardeningbutton.setObjectName("hardeningbutton")
        self.homebutton = QtWidgets.QPushButton(benchmarking)
        self.homebutton.setGeometry(QtCore.QRect(300, 15, 121, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.homebutton.setFont(font)
        self.homebutton.setStyleSheet("background-color: rgb(79, 135, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.homebutton.setObjectName("homebutton")
        self.titlelabel = QtWidgets.QLabel(benchmarking)
        self.titlelabel.setGeometry(QtCore.QRect(20, 15, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.titlelabel.setFont(font)
        self.titlelabel.setStyleSheet("background-color: rgb(79, 135, 255);\n"
"")
        self.titlelabel.setObjectName("titlelabel")
        self.lynuscandetails = QtWidgets.QLabel(benchmarking)
        self.lynuscandetails.setGeometry(QtCore.QRect(20, 70, 311, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lynuscandetails.setFont(font)
        self.lynuscandetails.setObjectName("lynuscandetails")
        self.hardeningindex = QtWidgets.QLabel(benchmarking)
        self.hardeningindex.setGeometry(QtCore.QRect(20, 120, 291, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.hardeningindex.setFont(font)
        self.hardeningindex.setObjectName("hardeningindex")
        self.testsperformed = QtWidgets.QLabel(benchmarking)
        self.testsperformed.setGeometry(QtCore.QRect(20, 170, 301, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.testsperformed.setFont(font)
        self.testsperformed.setObjectName("testsperformed")
        self.pluginsenabled = QtWidgets.QLabel(benchmarking)
        self.pluginsenabled.setGeometry(QtCore.QRect(20, 220, 291, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pluginsenabled.setFont(font)
        self.pluginsenabled.setObjectName("pluginsenabled")
        self.label_6 = QtWidgets.QLabel(benchmarking)
        self.label_6.setGeometry(QtCore.QRect(350, 120, 191, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(benchmarking)
        self.label_8.setGeometry(QtCore.QRect(350, 170, 211, 31))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(benchmarking)
        self.label_9.setGeometry(QtCore.QRect(350, 220, 201, 31))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.textBrowser = QtWidgets.QTextBrowser(benchmarking)
        self.textBrowser.setGeometry(QtCore.QRect(20, 340, 511, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(benchmarking)
        self.textBrowser_2.setGeometry(QtCore.QRect(630, 340, 511, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.warnings = QtWidgets.QLabel(benchmarking)
        self.warnings.setGeometry(QtCore.QRect(20, 270, 160, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.warnings.setFont(font)
        self.warnings.setObjectName("warnings")
        self.suggestions = QtWidgets.QLabel(benchmarking)
        self.suggestions.setGeometry(QtCore.QRect(630, 270, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.suggestions.setFont(font)
        self.suggestions.setObjectName("suggestions")
        self.hardeningbutton_2 = QtWidgets.QPushButton(benchmarking)
        self.hardeningbutton_2.setGeometry(QtCore.QRect(700, 15, 121, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.hardeningbutton_2.setFont(font)
        self.hardeningbutton_2.setStyleSheet("background-color: rgb(79, 135, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.hardeningbutton_2.setObjectName("hardeningbutton_2")

        self.retranslateUi(benchmarking)
        QtCore.QMetaObject.connectSlotsByName(benchmarking)

    def retranslateUi(self, benchmarking):
        _translate = QtCore.QCoreApplication.translate
        benchmarking.setWindowTitle(_translate("benchmarking", "Dialog"))
        self.helpbutton.setText(_translate("benchmarking", "Help"))
        self.benchmarkingbuttton.setText(_translate("benchmarking", "Benchmark"))
        self.hardeningbutton.setText(_translate("benchmarking", "Harden"))
        self.homebutton.setText(_translate("benchmarking", "Home"))
        self.titlelabel.setText(_translate("benchmarking", "Secura"))
        self.lynuscandetails.setText(_translate("benchmarking", "Benchmarking"))
        self.hardeningindex.setText(_translate("benchmarking", " Hardening index                    :"))
        self.testsperformed.setText(_translate("benchmarking", "Tests performed                      :"))
        self.pluginsenabled.setText(_translate("benchmarking", "Plugins enabled                      :"))
        self.warnings.setText(_translate("benchmarking", "Warnings  :"))
        self.suggestions.setText(_translate("benchmarking", "Suggestions  :"))
        self.hardeningbutton_2.setText(_translate("benchmarking", "Network"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    benchmarking = QtWidgets.QDialog()
    ui = Ui_benchmarking()
    ui.setupUi(benchmarking)
    benchmarking.show()
    sys.exit(app.exec_())
