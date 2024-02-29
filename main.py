# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'escutcheeon.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog,QApplication,QLineEdit
from PyQt5.QtGui import QFont
import sys
import subprocess as sp
import pysondb as ps
from hardener import hardener
from hardener import makeDB
from lynisInfo import sysinf
from lynisInfo import scaninf
from lynisInfo import suggestions
from lynisInfo import warnings
from lynisInfo import remove_ansi_escape_codes
import webbrowser

class Ui_openingpage(QDialog):
    def __init__(self):
        super(Ui_openingpage,self).__init__()
        loadUi("loginpage.ui",self)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.submitbutton.clicked.connect(self.getdetails)
    def getdetails(self):
        userid=self.lineEdit_2.text()
        password=self.lineEdit.text()
        widget1.setCurrentIndex(widget1.currentIndex()+1)
        
class Ui_home(QDialog):
    def __init__(self, d,s):
        super(Ui_home,self).__init__()
        loadUi("homescreen.ui",self)
        self.score = s
        self.details = d

        self.benchmarkingbuttton.clicked.connect(self.gotoBenchmarking)
        self.hardeningbutton.clicked.connect(self.gotoHardening)
        self.homebutton_2.clicked.connect(self.gotoAdvanced)
        self.progversioninput.setText(self.details[0])
        self.progversioninput.setFont(QFont('Segoe UI ',11))
        self.osinput.setText(self.details[1])
        self.osinput.setFont(QFont('Segoe UI ',11))
        self.osnameinput.setText(self.details[2])
        self.osnameinput.setFont(QFont('Segoe UI ',11))
        self.osversioninput.setText(self.details[3])
        self.osversioninput.setFont(QFont('Segoe UI ',11))
        self.kernelversioninput.setText(self.details[4])
        self.kernelversioninput.setFont(QFont('Segoe UI ',11))
        self.hardwareplatforminput.setText(self.details[5])
        self.hardwareplatforminput.setFont(QFont('Segoe UI ',11))
        self.hostnameinput.setText(self.details[6])
        self.hostnameinput.setFont(QFont('Segoe UI ',11))
        self.helpbutton.clicked.connect(self.gotoPage)
        self.lcdNumber.display(int(self.score))
    def gotoPage(self):
        webbrowser.open("https://sih-grind.github.io/Help-Page/")

    def gotoBenchmarking(self):
        widget1.setCurrentIndex(widget1.currentIndex()+1)
    def gotoHardening(self):
        widget1.setCurrentIndex(3)
    def gotoAdvanced(self):
        widget1.setCurrentIndex(4)
    def get_deets(self, d):
        self.details = d
    def show_deets(self):
        print(self.details)

class Ui_benchmarking(QDialog):
    def __init__(self, a, b, c):
        self.deets = a
        self.w = b
        self.s = c
        super(Ui_benchmarking,self).__init__()
        loadUi("benchmark.ui",self)
        self.homebutton.clicked.connect(self.gotoHome)
        self.hardeningbutton.clicked.connect(self.gotoHardening)
        self.hardeningbutton_2.clicked.connect(self.gotoAdvanced)
        self.label_6.setText(self.deets[0])
        self.label_6.setFont(QFont('Segoe UI Semilight',12))
        self.label_8.setText(self.deets[1])
        self.label_8.setFont(QFont('Segoe UI Semilight',12))
        self.label_9.setText(self.deets[2])
        self.label_9.setFont(QFont('Segoe UI Semilight',12))
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.append(str(self.w))
        self.textBrowser_2.setAcceptRichText(True)
        self.textBrowser_2.append(str(self.s))
        self.helpbutton.clicked.connect(self.gotoPage)
    def gotoPage(self):
        webbrowser.open("https://sih-grind.github.io/Help-Page/")
    def get_deets(self, d):
        self.deets = d
    def get_warnings(self,s):
        self.warnings = s
    def get_suggestions(self,s):
        self.suggestions = s
    def gotoHardening(self):
        widget1.setCurrentIndex(3)
    def gotoHome(self):
        widget1.setCurrentIndex(1)
    def gotoAdvanced(self):
        widget1.setCurrentIndex(4)
    def show_deets(self):
        print(self.deets)

class Ui_Hardening(QDialog):
    def __init__(self):
        self.db = ps.getDb('bool.json')
        self.dict={'Password Policies' : "" ,"Remove Unecessary Packages" : "" ,'UFW' : "" ,'fail2ban' : "" ,'USB Storage Access' : "" ,'TOR Service' : "" ,}
        super(Ui_Hardening,self).__init__()
        loadUi("harden.ui",self)
        self.homebutton.clicked.connect(self.gotoHome)
        self.hardeningbutton_2.clicked.connect(self.gotoAdvanced)
        self.savebutton.clicked.connect(self.Save)
        self.hardenbutton.clicked.connect(self.Harden)
        self.benchmarkingbuttton.clicked.connect(self.gotoBenchmarking)
        self.helpbutton.clicked.connect(self.gotoPage)
    def gotoPage(self):
        webbrowser.open("https://sih-grind.github.io/Help-Page/")
    def Harden(self):
        hard = hardener()
        hard.harden()
        remove_ansi_escape_codes()
    def gotoBenchmarking(self):
        widget1.setCurrentIndex(2)
    def gotoAdvanced(self):
        widget1.setCurrentIndex(4)
    def Save(self):
        #remove orphan packages
        #yes
        if self.rupyes.isChecked()==True:
            self.db.updateByQuery({'name':'rmpk'},{'bool':'True'})
        #no
        elif self.rupno.isChecked()==True:
            self.db.updateByQuery({'name':'rmpk'},{'bool':'None'})
        
        #password policies
        #weak
        if self.ppyes.isChecked()==True:
            self.db.updateByQuery({'name':'pwdp'},{'bool':'None'})
        #moderate
        elif self.ppno.isChecked()==True:
            self.db.updateByQuery({'name':'pwdp'},{'bool':'None'})
        #strong
        elif self.ppno_2.isChecked()==True:
            self.db.updateByQuery({'name':'pwdp'},{'bool':'True'})
        #ufw
        #enable
        if self.ufwyes.isChecked()==True:
            self.db.updateByQuery({'name':'ufwI'},{'bool':'True'})
            #self.db.updateByQuery({'name':'ufwE'},{'bool':'True'})
        #disable
        elif self.ufwno.isChecked()==True:
            self.db.updateByQuery({'name':'ufwI'},{'bool':'None'})
            self.db.updateByQuery({'name':'ufwE'},{'bool':'None'})
            self.db.updateByQuery({'name':'ufwD'},{'bool':'True'})
        
        #fail2ban
        #enable
        if self.fail2banyes.isChecked()==True:
            self.db.updateByQuery({'name':'f2bE'},{'bool':'True'})
        #disable
        elif self.fail2banno.isChecked()==True:
            self.db.updateByQuery({'name':'f2bD'},{'bool':'True'})
        
        #usb storage
        #enable
        if self.usbsayes.isChecked()==True:
            self.db.updateByQuery({'name':'usbE'},{'bool':'True'})
        #disable
        elif self.usbno.isChecked()==True:
            self.db.updateByQuery({'name':'usbE'},{'bool':'None'})

        #tor
        #enable
        if self.usbyes.isChecked()==True:
            self.db.updateByQuery({'name':'torD'},{'bool':'True'})
        #disable
        elif self.usbno_2.isChecked()==True:
            self.db.updateByQuery({'name':'torD'},{'bool':'None'})


    def gotoHome(self):
        widget1.setCurrentIndex(1)

class Ui_hardeningadvanced(QDialog):
    def __init__(self, rules):
        self.db = ps.getDb('bool.json')
        super(Ui_hardeningadvanced,self).__init__()
        loadUi("network.ui",self)
        self.homebutton.clicked.connect(self.gotoHome)
        self.textBrowser.setText(rules)
        self.textBrowser.setFont(QFont('Segoe UI Semilight',12))
        self.benchmarkingbuttton.clicked.connect(self.gotoBenchmarking)
        self.hardeningbutton.clicked.connect(self.gotoHardening)
        self.pushButton.clicked.connect(self.configAD)
        self.helpbutton.clicked.connect(self.gotoPage)
    def gotoPage(self):
        webbrowser.open("https://sih-grind.github.io/Help-Page/")
    def configAD(self):
        #ports
        if self.lineEdit.text():
            if self.radioButton.isChecked()==True:
                self.db.updateByQuery({'name':'ufwAP'},{'bool':'True','args':self.lineEdit.text()},)
            elif self.radioButton_2.isChecked()==True:
                self.db.updateByQuery({'name':'ufwBP'},{'bool':'True','args':self.lineEdit.text()})
        else:
            self.db.updateByQuery({'name':'ufwAP'},{'bool':'None', 'args':'None'})
            self.db.updateByQuery({'name':'ufwBP'},{'bool':'None', 'args':'None'})
        #block ips
        if self.lineEdit_2.text():
            self.db.updateByQuery({'name':'ufwBI'},{'bool':'True', 'args': self.lineEdit_2.text()})
        #whitelist ips
        if self.lineEdit_3.text():
            self.db.updateByQuery({'name':'ufwAI'},{'bool':'True', 'args': self.lineEdit_3.text()})
        if self.lineEdit_4.text():
            self.db.updateByQuery({'name':'ufwDel'},{'bool':'True', 'args': self.lineEdit_4.text()})
        #ssh ports
        ssh_ports=self.lineEdit_5.text()
        if ssh_ports:
            self.db.updateByQuery({'name':'sshp'},{'bool':'True', 'args': ssh_ports})
        #Permit Root Login
        #enable
        if self.radioButton_3.isChecked()==True:
            self.db.updateByQuery({'name':'sshRE'},{'bool':'True', 'args': 'None'})
        #disable
        elif self.radioButton_4.isChecked()==True:
            self.db.updateByQuery({'name':'sshRD'},{'bool':'True', 'args': 'None'})
        #Password Authentication
        #enable
        if self.radioButton_5.isChecked()==True:
            self.db.updateByQuery({'name':'sshPAE'},{'bool':'True', 'args': 'None'})
        #disable
        elif self.radioButton_6.isChecked()==True:
            self.db.updateByQuery({'name':'sshPAD'},{'bool':'True', 'args': 'None'})
        #X11 Forwarding
        #enable
        if self.radioButton_7.isChecked()==True:
            self.db.updateByQuery({'name':'sshXFE'},{'bool':'True', 'args': 'None'})
        #disable
        elif self.radioButton_8.isChecked()==True:
            self.db.updateByQuery({'name':'sshXFD'},{'bool':'True', 'args': 'None'})


    def gotoHome(self):
        widget1.setCurrentIndex(1)
    def gotoBenchmarking(self):
        widget1.setCurrentIndex(2)
    def gotoHardening(self):
        widget1.setCurrentIndex(3)






#hard = hardener()
remove_ansi_escape_codes()

first = sysinf()
second = scaninf()
third = warnings()
fourth = suggestions()

app = QApplication(sys.argv)
widget1=QtWidgets.QStackedWidget()
ui_openingpage=Ui_openingpage()
ui_home=Ui_home(first, second[0])
ui_benchmarking=Ui_benchmarking(second, third, fourth)
ui_hardening=Ui_Hardening()
process = sp.Popen([f'sudo -S ufw status numbered'], stdin = sp.PIPE, stdout=sp.PIPE, shell=True)
output, error = process.communicate("chai@1234".encode())
process.wait()
ui_hardeningadvanced=Ui_hardeningadvanced(output.decode())

widget1.addWidget(ui_openingpage)
widget1.addWidget(ui_home)
widget1.addWidget(ui_benchmarking)
widget1.addWidget(ui_hardening)
widget1.addWidget(ui_hardeningadvanced)

widget1.setFixedWidth(1242)
widget1.setFixedHeight(529)

makeDB()

widget1.show()



try:
    sys.exit(app.exec())
except Exception as e:
    print("An error occurred:", str(e))
