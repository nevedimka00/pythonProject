import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton,QCheckBox,QRadioButton,QButtonGroup
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(500,200,700,500)
        # self.setWindowIcon(QIcon("gui_test/img.png"))
        # lable = QLabel("Hello",self)
        # lable.setFont(QFont("Arial",30))
        # lable.setGeometry(0,0,500,100)
        # lable.setStyleSheet("color:blue;"
        #                     "background-color:yellow;" 
        #                     "font-weight:bold;"
        #                     "font-style:italic;"
        #                     "text-decoration:underline;")
        # lable.setAlignment(Qt.AlignTop | Qt.AlignVCenter)
        # lable.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        # lable.setAlignment(Qt.AlignCenter)

        # image_lable = QLabel(self)
        # image_lable.setGeometry(0,0,500,300)
        # pixmap = QPixmap("gui_test/img.png")
        # image_lable.setPixmap(pixmap)
        # image_lable.setScaledContents(True)
        # image_lable.setGeometry((self.width()-image_lable.width())//2,
        #                         (self.height()-image_lable.height())//2,
        #                         image_lable.width(),
        #                         image_lable.height())
        # self.checkBox = QCheckBox("Do you like food?",self)
        # self.radio1 = QRadioButton("Visa",self)
        # self.radio2 = QRadioButton("Mastercard",self)
        # self.radio3 = QRadioButton("GiftCard",self)
        # self.radio4 = QRadioButton("In-Store",self)
        # self.radio5 = QRadioButton("Online",self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)

        # self.line_edit= QLineEdit(self)
        # self.button = QPushButton("Submit",self)
        self.initUI()


    def initUI(self):
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        # lable1 = QLabel("#1",self)
        # lable2 = QLabel("#2",self)
        # lable3 = QLabel("#3",self)
        # lable4 = QLabel("#4",self)
        # lable5 = QLabel("#5",self)
        # lable6 = QLabel("#6",self)

        # lable1.setStyleSheet("background-color:red;")
        # lable2.setStyleSheet("background-color:yellow;")
        # lable3.setStyleSheet("background-color:green;")
        # lable4.setStyleSheet("background-color:blue;")
        # lable5.setStyleSheet("background-color:purple;")
        # lable6.setStyleSheet("background-color:orange;")

        # vbox = QGridLayout()
        # vbox.addWidget(lable1,0,0)
        # vbox.addWidget(lable2,0,1)
        # vbox.addWidget(lable3,1,0)
        # vbox.addWidget(lable4,1,1)
        # vbox.addWidget(lable5,2,0)
        # vbox.addWidget(lable6,2,1)

        # central_widget.setLayout(vbox)

    #     self.button =  QPushButton("Click me",self)
    #     self.button.setGeometry(250,200,200,100)
    #     self.button.setStyleSheet("font-size:30px;")
    #     self.button.clicked.connect(self.on_click)
    #     self.lable = QLabel("This needs to be changed",self)
    #     self.lable.setGeometry(0,0,500,100)

    # def on_click(self):
    #     print("Button clicked")
    #     self.button.setText("Clicked!")
    #     self.button.setDisabled(True)
    #     self.lable.setText("This has been changed!!!")
    #     self.checkBox.setGeometry(10,0,500,50)
    #     self.checkBox.setStyleSheet("font-size:30px;"
    #                                 "font-family:Arial;")
    #     self.checkBox.setChecked(False)
    #     self.checkBox.stateChanged.connect(self.checkbox_changed)

    # def checkbox_changed(self,state):
    #     if state == Qt.Checked: 
    #         print("You like food")
    #     else: print("You do not like food")
    #      self.radio1.setGeometry(0,0,300,50)
    #      self.radio2.setGeometry(0,50,300,50)
    #      self.radio3.setGeometry(0,100,300,50)
    #      self.radio4.setGeometry(0,150,300,50)
    #      self.radio5.setGeometry(0,200,300,50)
    #      self.setStyleSheet("QRadioButton{"
    #                         "font-size:30px;"
    #                         "font-family:Arial;"
    #                         "padding:10px;"
    #                         "}")
    #      self.button_group1.addButton(self.radio1)
    #      self.button_group1.addButton(self.radio2)
    #      self.button_group1.addButton(self.radio3)
    #      self.button_group2.addButton(self.radio4)
    #      self.button_group2.addButton(self.radio5)

    #      self.radio1.toggled.connect(self.radio_button_changed)
    #      self.radio2.toggled.connect(self.radio_button_changed)
    #      self.radio3.toggled.connect(self.radio_button_changed)
    #      self.radio4.toggled.connect(self.radio_button_changed)
    #      self.radio5.toggled.connect(self.radio_button_changed)


    # def radio_button_changed(self):
    #     tmp_button = self.sender()
    #     if tmp_button.isChecked():
    #         print(f"{tmp_button.text()} is selected")

        self.line_edit.setGeometry(10,10,200,40)
        self.line_edit.setStyleSheet("font-size:20px;"
                                     "font-family:Arial;")
        self.button.setGeometry(220,10,100,40)
        self.button.setStyleSheet("font-size:20px;"
                                             "font-family:Arial;")

        self.line_edit.setPlaceholderText("Enter what you want")
        self.button.clicked.connect(self.submit)

    def submit(self):
        print(f"You have entered: {self.line_edit.text()}")


def main():
    app=QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()