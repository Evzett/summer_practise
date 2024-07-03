import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class FormBrightness(QtWidgets.QWidget):
    BrightnessSignal = QtCore.pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.setObjectName("FormBrightness")
        self.resize(487, 333)
        self.setStyleSheet("\n"
                           "background-color: rgb(90, 90, 91);")
        self.text_brightness = QtWidgets.QLabel(self)
        self.text_brightness.setGeometry(QtCore.QRect(30, 50, 401, 71))
        self.text_brightness.setStyleSheet("background-color: rgb(206, 203, 198); \n"
                                           "font: 87 italic 10pt \"Segoe UI Black\";\n"
                                           "color: rgb(61, 61, 61);\n"
                                           "border-radius: 10px; \n"
                                           "")
        self.text_brightness.setObjectName("text_brightness")
        self.TextBrightnessUser = QtWidgets.QLineEdit(self)
        self.TextBrightnessUser.setGeometry(QtCore.QRect(30, 150, 401, 61))
        self.TextBrightnessUser.setStyleSheet("background-color: rgba(206, 203, 198, 0.5); \n"
                                              "font: 87 italic 16pt \"Segoe UI Black\";\n"
                                              "color: rgb(61, 61, 61);\n"
                                              "border-radius: 10px; \n"
                                              "")
        self.TextBrightnessUser.setObjectName("TextBrightnessUser")
        self.ButtonSave = QtWidgets.QPushButton(self)
        self.ButtonSave.setGeometry(QtCore.QRect(280, 270, 191, 41))
        self.ButtonSave.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgba(244, 227, 195, 0.5); \n"
                                      "    font: 87 italic 10pt \"Segoe UI Black\";\n"
                                      "    color: rgb(61, 61, 61);\n"
                                      "    border-radius: 10px;  \n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgba(244, 227, 195, 0.7);  \n"
                                      "    color: rgb(51, 51, 51);  \n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgba(244, 227, 195, 0.9);  \n"
                                      "    color: rgb(41, 41, 41); \n"
                                      "}\n"
                                      "")
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonSave.clicked.connect(self.save_brightness)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def show_error_message(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Ошибка: ")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def save_brightness(self):
        try:
            if 0 <= int(self.TextBrightnessUser.text()) <= 255:
                self.BrightnessSignal.emit(int(self.TextBrightnessUser.text()))
                self.close()
            else:
                raise ValueError
        except ValueError:
            self.show_error_message("Данные должны быть числом\nв диапазоне от 0 до 255!")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FormBrightness", "Окно яркости"))
        self.text_brightness.setText(_translate("FormBrightness", "  Введите, на сколько хотите повысить\n"
                                                                  "  яркость изображения"))
        self.ButtonSave.setText(_translate("FormBrightness", "Сохранить"))
