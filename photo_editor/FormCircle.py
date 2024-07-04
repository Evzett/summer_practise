"""
Модуль для настройки параметров круга с использованием PyQt5.

Этот модуль предоставляет класс FormCircle, который позволяет пользователю вводить координаты, радиус и ширину линии круга.
"""

from PyQt5 import QtCore, QtWidgets


class ZeroCoordsException(Exception):
    """
    Исключение для проверки нулевых координат или недопустимых значений радиуса и ширины линии.
    """
    pass


class FormCircle(QtWidgets.QWidget):
    """
    Класс для создания окна настройки параметров круга.

    Сигналы:
        CircleSignal (pyqtSignal): Сигнал, испускаемый при сохранении параметров круга.
    """
    CircleSignal = QtCore.pyqtSignal(list)

    def __init__(self):
        """
        Инициализирует объект FormCircle.
        """
        super().__init__()
        self.setupUi()

    def setupUi(self):
        """
        Инициализирует пользовательский интерфейс окна настроек круга.
        """
        self.setObjectName("FormCircle")
        self.resize(566, 428)
        self.setStyleSheet("background-color: rgb(90, 90, 91);")

        self.text_draw_a_circle = QtWidgets.QLabel(self)
        self.text_draw_a_circle.setGeometry(QtCore.QRect(30, 50, 401, 71))
        self.text_draw_a_circle.setStyleSheet(
            "background-color: rgb(206, 203, 198); "
            "font: 87 italic 10pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.text_draw_a_circle.setObjectName("text_draw_a_circle")

        self.ButtonSaveCircle = QtWidgets.QPushButton(self)
        self.ButtonSaveCircle.setGeometry(QtCore.QRect(360, 360, 191, 41))
        self.ButtonSaveCircle.setStyleSheet(
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
        self.ButtonSaveCircle.setObjectName("ButtonSaveCircle")
        self.ButtonSaveCircle.clicked.connect(self.save_circle)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(90, 150, 375, 205))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.text_x_coord = QtWidgets.QLabel(self.widget)
        self.text_x_coord.setMinimumSize(QtCore.QSize(69, 45))
        self.text_x_coord.setMaximumSize(QtCore.QSize(69, 45))
        self.text_x_coord.setStyleSheet(
            "background-color: rgb(206, 203, 198); "
            "font: 87 italic 10pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.text_x_coord.setObjectName("text_x_coord")
        self.verticalLayout_2.addWidget(self.text_x_coord)

        self.text_y_coord = QtWidgets.QLabel(self.widget)
        self.text_y_coord.setMinimumSize(QtCore.QSize(69, 45))
        self.text_y_coord.setMaximumSize(QtCore.QSize(69, 45))
        self.text_y_coord.setStyleSheet(
            "background-color: rgb(206, 203, 198); "
            "font: 87 italic 10pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.text_y_coord.setObjectName("text_y_coord")
        self.verticalLayout_2.addWidget(self.text_y_coord)

        self.text_radius = QtWidgets.QLabel(self.widget)
        self.text_radius.setMinimumSize(QtCore.QSize(69, 45))
        self.text_radius.setMaximumSize(QtCore.QSize(69, 45))
        self.text_radius.setStyleSheet(
            "background-color: rgb(206, 203, 198); "
            "font: 87 italic 10pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.text_radius.setObjectName("text_radius")
        self.verticalLayout_2.addWidget(self.text_radius)

        self.text_line_size = QtWidgets.QLabel(self.widget)
        self.text_line_size.setMinimumSize(QtCore.QSize(69, 45))
        self.text_line_size.setMaximumSize(QtCore.QSize(69, 45))
        self.text_line_size.setStyleSheet(
            "background-color: rgb(206, 203, 198); "
            "font: 87 italic 10pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.text_line_size.setObjectName("text_line_size")
        self.verticalLayout_2.addWidget(self.text_line_size)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.TextUserX = QtWidgets.QLineEdit(self.widget)
        self.TextUserX.setMinimumSize(QtCore.QSize(189, 45))
        self.TextUserX.setMaximumSize(QtCore.QSize(189, 45))
        self.TextUserX.setStyleSheet(
            "background-color: rgba(206, 203, 198, 0.5); "
            "font: 87 italic 16pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.TextUserX.setObjectName("TextUserX")
        self.verticalLayout.addWidget(self.TextUserX)

        self.TextUserY = QtWidgets.QLineEdit(self.widget)
        self.TextUserY.setMinimumSize(QtCore.QSize(0, 45))
        self.TextUserY.setMaximumSize(QtCore.QSize(189, 45))
        self.TextUserY.setStyleSheet(
            "background-color: rgba(206, 203, 198, 0.5); "
            "font: 87 italic 16pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.TextUserY.setObjectName("TextUserY")
        self.verticalLayout.addWidget(self.TextUserY)

        self.TextUserR = QtWidgets.QLineEdit(self.widget)
        self.TextUserR.setMinimumSize(QtCore.QSize(0, 45))
        self.TextUserR.setMaximumSize(QtCore.QSize(189, 45))
        self.TextUserR.setStyleSheet(
            "background-color: rgba(206, 203, 198, 0.5); "
            "font: 87 italic 16pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.TextUserR.setObjectName("TextUserR")
        self.verticalLayout.addWidget(self.TextUserR)

        self.TextUserL = QtWidgets.QLineEdit(self.widget)
        self.TextUserL.setMinimumSize(QtCore.QSize(0, 45))
        self.TextUserL.setMaximumSize(QtCore.QSize(189, 45))
        self.TextUserL.setStyleSheet(
            "background-color: rgba(206, 203, 198, 0.5); "
            "font: 87 italic 16pt 'Segoe UI Black';"
            "color: rgb(61, 61, 61);"
            "border-radius: 10px;"
        )
        self.TextUserL.setObjectName("TextUserL")
        self.verticalLayout.addWidget(self.TextUserL)

        self.horizontalLayout.addLayout(self.verticalLayout)

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

    def save_circle(self):
        """
        Проверяет корректность введённых данных и отправляет сигнал с параметрами круга.
        """
        try:
            if (int(self.TextUserX.text()) >= 0 and int(self.TextUserY.text()) >= 0 and int(self.TextUserR.text()) >= 1
                    and int(self.TextUserL.text()) >= 1):
                list_data = [int(self.TextUserX.text()), int(self.TextUserY.text()), int(self.TextUserR.text()),
                             int(self.TextUserL.text())]
                self.CircleSignal.emit(list_data)
                self.close()
            else:
                raise ZeroCoordsException
        except ValueError:
            self.show_error_message("Проверьте данные. Все данные должны быть целыми числами.")
        except ZeroCoordsException:
            self.show_error_message(
                "Координаты должны быть целыми неотрицательными числами, а радиус и ширина линии должны "
                "быть >= 1")

    def retranslateUi(self):
        """
        Устанавливает текст для элементов интерфейса.
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FormCircle", "FormCircle"))
        self.text_draw_a_circle.setText(_translate("FormCircle", "Введите координаты и размер круга,\n"
                                                                 "где r - радиус круга, L - ширина линии"))
        self.ButtonSaveCircle.setText(_translate("FormCircle", "Сохранить"))
        self.text_x_coord.setText(_translate("FormCircle", "   x:"))
        self.text_y_coord.setText(_translate("FormCircle", "   y:"))
        self.text_radius.setText(_translate("FormCircle", "   r:"))
        self.text_line_size.setText(_translate("FormCircle", "   L:"))
