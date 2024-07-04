"""
Модуль для настройки яркости изображения с использованием PyQt5.

Этот модуль предоставляет класс FormBrightness, который позволяет пользователю вводить значение яркости,
проверять его корректность и передавать значение через сигнал.
"""


from PyQt5 import QtCore, QtWidgets


class FormBrightness(QtWidgets.QWidget):
    """
    Класс для создания окна настройки яркости изображения.

    Сигналы:
        BrightnessSignal (pyqtSignal): Сигнал, испускаемый при сохранении значения яркости.
    """
    BrightnessSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        """
        Инициализирует объект FormBrightness.
        """
        super().__init__()
        self.setupUi()

    def setupUi(self):
        """
        Инициализирует пользовательский интерфейс окна яркости.
        """
        self.setObjectName("FormBrightness")
        self.resize(487, 333)
        self.setStyleSheet("background-color: rgb(90, 90, 91);")

        self.text_brightness = QtWidgets.QLabel(self)
        self.text_brightness.setGeometry(QtCore.QRect(30, 50, 401, 71))
        self.text_brightness.setStyleSheet(
            "background-color: rgb(206, 203, 198); "
            "font: 87 italic 10pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.text_brightness.setObjectName("text_brightness")

        self.TextBrightnessUser = QtWidgets.QLineEdit(self)
        self.TextBrightnessUser.setGeometry(QtCore.QRect(30, 150, 401, 61))
        self.TextBrightnessUser.setStyleSheet(
            "background-color: rgba(206, 203, 198, 0.5); "
            "font: 87 italic 16pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.TextBrightnessUser.setObjectName("TextBrightnessUser")

        self.ButtonSave = QtWidgets.QPushButton(self)
        self.ButtonSave.setGeometry(QtCore.QRect(280, 270, 191, 41))
        self.ButtonSave.setStyleSheet(
            "QPushButton {"
            "    background-color: rgba(244, 227, 195, 0.5); "
            "    font: 87 italic 10pt 'Segoe UI Black';"
            "    color: rgb(61, 61, 61);"
            "    border-radius: 10px; "
            "}"
            "QPushButton:hover {"
            "    background-color: rgba(244, 227, 195, 0.7); "
            "    color: rgb(51, 51, 51); "
            "}"
            "QPushButton:pressed {"
            "    background-color: rgba(244, 227, 195, 0.9); "
            "    color: rgb(41, 41, 41); "
            "}"
        )
        self.ButtonSave.setObjectName("ButtonSave")
        self.ButtonSave.clicked.connect(self.save_brightness)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def show_error_message(self, message):
        """
        Отображает сообщение об ошибке.

        :param message: Текст сообщения об ошибке.
        :type message: str
        """
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Ошибка: ")
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    def save_brightness(self):
        """
        Сохраняет значение яркости, введенное пользователем, и испускает сигнал BrightnessSignal.
        """
        try:
            brightness_value = int(self.TextBrightnessUser.text())
            if 0 <= brightness_value <= 255:
                self.BrightnessSignal.emit(brightness_value)
                self.close()
            else:
                raise ValueError
        except ValueError:
            self.show_error_message("Данные должны быть числом в диапазоне от 0 до 255!")

    def retranslateUi(self):
        """
        Устанавливает текст для элементов интерфейса.
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FormBrightness", "Окно яркости"))
        self.text_brightness.setText(_translate("FormBrightness",
                                                "  Введите, на сколько хотите повысить\n  яркость изображения"))
        self.ButtonSave.setText(_translate("FormBrightness", "Сохранить"))
