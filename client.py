import webbrowser
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 600)
        
        #Isertion host ip
        self.label1 = QLabel("Enter your host IP:", self)
        self.label1.move(20, 30)
        self.text1 = QLineEdit(self)
        self.text1.move(20, 50)

       #Isertion Insertion Api key
        self.label3 = QLabel("Enter your api_key:", self)
        self.label3.move(20, 100)
        self.text3 = QLineEdit(self)
        self.text3.move(20, 120)

        #Isertion Insertion Hostname
        self.label4 = QLabel("Enter your Hostname:", self)
        self.label4.move(20, 160)
        self.text4 = QLineEdit(self)
        self.text4.move(20, 180)

        self.button = QPushButton("Send", self)
        self.button.move(10, 220)


        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text4.text()
        hostIp = self.text1.text()
        apiKey = self.text3.text()

        if hostname == "" or hostIp == "" or apiKey =="":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,hostIp,apiKey)
            print(res)
            if res:
                self.__processing(hostname,hostIp,apiKey)
                self.label4.setText("Answer%s" % (res["Hello"]))
                self.label4.adjustSize()
                self.show()
            
    def __query(self, hostname,hostIp,apiKey):
        url = "http://%s/ip/%s?key=%s" % (hostname,hostIp,apiKey)
        print(url)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
    
    def __processing(self, hostname,hostIp,apiKey):
        lat = self.__query(hostname,hostIp,apiKey)["lat"]
        long = self.__query(hostname,hostIp,apiKey)["long"]
        print(long,lat)

        url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (lat,long)
        webbrowser.open_new(url)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()