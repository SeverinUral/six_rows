#! /usr/bin/python3
# -*- coding utf-8 -*-
# (c) 2021 Fomenko A V


import sys

try:
    from PyQt5.QtWidgets import QApplication as QApp
    from PyQt5.QtWidgets import QMainWindow as QMW
except Exception as e:
    print(e)
    print("Install PyQt5.\nUse 'sudo apt install python3-pyqt5'",
          "for Debian-based systems\nor 'sudo pip3 install pyqt5'",
          "for other system.\n",
          "For console mode use key '-c'")
    sys.exit(-1)


from design import Ui_MainWindow as UMW
from six_rows import SixRows


class MyWindow(QMW, UMW):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_Code.clicked.connect(self.code)
        self.btn_Decode.clicked.connect(self.decode)
        self.btn_Swip.clicked.connect(self.swip)

    def code(self):
        self.texedit_Output.clear()
        sr = SixRows(self.texedit_Input.toPlainText())
        self.texedit_Output.setText(sr.coding())

    def decode(self):
        self.texedit_Output.clear()
        sr = SixRows(self.texedit_Input.toPlainText())
        self.texedit_Output.setText(sr.decoding())

    def swip(self):
        self.texedit_Input.setText(self.texedit_Output.toPlainText())
        self.texedit_Output.clear()


def console():
    choise = input("Coding or Decoding (C/D)? ")
    input_str = input("Input string: ")
    sr = SixRows(input_str)

    if choise.lower() == "c":
        print(sr.coding())
    elif choise.lower() == "d":
        print(sr.decoding())


def main():
    if len(sys.argv) > 1:
        print("Console mode")
        console()
    else:
        app = QApp(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
