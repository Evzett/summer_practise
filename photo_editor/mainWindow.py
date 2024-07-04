"""
mainWindow.py

Описание: модуль основного окна графического интерфейса

"""
from collections import deque

from PyQt5.QtGui import QIcon

from photo_editor import Picture
from photo_editor.Buttons import GalleryButton, CameraButton, BrightnessButton, CircleButton, NegativeButton

from PyQt5 import QtCore, QtGui, QtWidgets

from photo_editor.CameraWindow import CameraWindow
from photo_editor.FormBrightness import FormBrightness
from photo_editor.FormCircle import FormCircle


class MainWindow(QtWidgets.QMainWindow):
    """
    Класс основного окна графического интерфейса, с использованием библиотеки PyQt5


    Аттрибуты:

    camera_window (CameraWindow):
     окно с камерой

    windowCircle (FormCircle):
     окно, требующее ввести размеры круга

    windowBrightness (FormBrightness):
     окно, требующее ввести насколько необходимо увеличить яркость изображения

    history  (collections.deque):
        Двусторонняя очередь, содержащая историю изменений изображения для возможности отката (undo).

    future (collections.deque):
        Двусторонняя очередь, содержащая будущие изменения изображения для возможности повторения (redo).


    Методы:

    show_picture(): используется для связи с кнопкой "Выбрать фото из галереи", открывает изображение из галереи

    red_channel(): используется для связи с кнопкой "Красный канал", показывает красный канал изображения

    green_channel(): используется для связи с кнопкой "Зеленый канал", показывает зеленый канал изображения

    negative(): используется для связи с кнопкой "Показать негативное изображение", показывает негативное изображение

    blue_channel(): используется для связи с кнопкой "Синий канал", показывает синий канал изображения

    open_camera_window(): используется для связи с кнопкой "Сделать фото", открывает окно с камерой

    display_image(QImage, cv2_image): используется для отображения фото с камеры

    more_brightness(): используется для связи с кнопкой "Увеличить яркость", открывает окно с прибавлением яркости

    save_photo(): используется для связи с кнопкой "Сохранить фото", сохраняет изображение

    apply_brightness(amount): добавляет яркость на фото

    red_circle(): используется для связи с кнопкой "Нарисовать круг" , открывает окно с характеристиками круга

    apply_circle(data_list): рисует круг на изображении

    updateIcons(): обновляет иконки кнопок

    add_action_to_history(): добавляет действие в историю действий

    changeIconBack(): меняет иконку кнопки "Назад"

    changeIconForward(): меняет иконку кнопки "Вперед"

    undo(): используется для связи с кнопкой "Назад", отменяет действие

    forward(): используется для связи с кнопкой "Вперед", отменяет отмену действия
    """
    BackSignal = QtCore.pyqtSignal()
    ForwardSignal = QtCore.pyqtSignal()

    def __init__(self):
        """
        Инициализация объекта

        """
        super().__init__()
        self.camera_window = None
        self.windowCircle = None
        self.windowBrightness = None
        self.history = deque()
        self.future = deque()
        self.setupUi()
        self.picture_module = Picture()

    def setupUi(self):
        """
            Устанавливает и настраивает пользовательский интерфейс основного окна приложения.

            Функция выполняет следующие действия:
                - Задает размеры и стили основного окна.
                - Создает и настраивает центральный виджет с помощью сетки и вертикальных/горизонтальных компоновок.
                - Добавляет и настраивает кнопки с различными функциями, такими как:
                    - Переход к галерее изображений.
                    - Открытие окна камеры.
                    - Увеличение яркости.
                    - Применение негативного фильтра.
                    - Обработка цветовых каналов (красный, зеленый, синий).
                    - Добавляет текстовые метки для описания действий.
                    - Устанавливает обработчики событий для кнопок.

            """

        self.setObjectName("MainWindow")
        self.resize(1404, 889)
        self.setAutoFillBackground(False)
        self.setStyleSheet("\n"
                           "background-color: rgb(29, 29, 29);\n"
                           "\n"
                           "")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonGallery = GalleryButton(self.centralwidget)
        self.ButtonGallery.setMinimumSize(QtCore.QSize(111, 91))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonGallery.setFont(font)
        self.ButtonGallery.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ButtonGallery.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                         "    border: none;\n"
                                         "    outline: none;\n"

                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.ButtonGallery.setText("")
        self.ButtonGallery.setObjectName("ButtonGallery")
        self.verticalLayout.addWidget(self.ButtonGallery)
        self.ButtonGallery.clicked.connect(self.show_picture)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.TextAddPicture = QtWidgets.QLabel(self.centralwidget)
        self.TextAddPicture.setStyleSheet("background-color: rgba(48, 48, 48, 0);\n"
                                          "font: 63 10pt \"Cascadia Mono SemiBold\";\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "")
        self.TextAddPicture.setObjectName("TextAddPicture")
        self.horizontalLayout_5.addWidget(self.TextAddPicture)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.ButtonGallery_2 = CameraButton(self.centralwidget)
        self.ButtonGallery_2.setMinimumSize(QtCore.QSize(71, 81))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonGallery_2.setFont(font)
        self.ButtonGallery_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ButtonGallery_2.setStyleSheet("QPushButton {\n"
                                           "  background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                           "    border: none;\n"
                                           "    outline: none;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "")
        self.ButtonGallery_2.setText("")
        self.ButtonGallery_2.setObjectName("ButtonGallery_2")
        self.verticalLayout.addWidget(self.ButtonGallery_2)
        self.ButtonGallery_2.clicked.connect(self.open_camera_window)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.TextTakePhoto = QtWidgets.QLabel(self.centralwidget)
        self.TextTakePhoto.setStyleSheet("background-color: rgba(48, 48, 48, 0);\n"
                                         "font: 63 10pt \"Cascadia Mono SemiBold\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "")
        self.TextTakePhoto.setObjectName("TextTakePhoto")
        self.horizontalLayout_4.addWidget(self.TextTakePhoto)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonBack = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ButtonBack.setStyleSheet("QPushButton {\n"
                                      "  background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                      "    border: none;\n"
                                      "    outline: none;\n"
                                      " image: url(icons/pressed_icons8-up-left-32.png); /* Начальная иконка */\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.ButtonBack.setText("")
        self.ButtonBack.setObjectName("ButtonBack")
        self.horizontalLayout.addWidget(self.ButtonBack)
        self.ButtonBack.clicked.connect(self.undo)
        self.ButtonForward = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonForward.setFont(font)
        self.ButtonForward.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ButtonForward.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                         "    border: none;\n"
                                         "    outline: none;\n"
                                         " image: url(icons/pressed_icon_forward.png); /* Начальная иконка */\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.ButtonForward.setText("")
        self.ButtonForward.setObjectName("ButtonForward")
        self.horizontalLayout.addWidget(self.ButtonForward)
        self.ButtonForward.clicked.connect(self.forward)
        self.ButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonLoad.setFont(font)
        self.ButtonLoad.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ButtonLoad.setStyleSheet("QPushButton {\n"
                                      "   background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                      "    border: none;\n"
                                      "    outline: none;\n"
                                      " image: url(icons/icon_load); /* Начальная иконка */\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.ButtonLoad.setText("")
        self.ButtonLoad.setObjectName("ButtonLoad")
        self.horizontalLayout.addWidget(self.ButtonLoad)
        self.ButtonLoad.clicked.connect(self.save_photo)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.mainPicture = QtWidgets.QLabel(self.centralwidget)
        self.mainPicture.setMinimumSize(QtCore.QSize(800, 750))
        self.mainPicture.setMaximumSize(QtCore.QSize(10000000, 16777215))
        self.mainPicture.setStyleSheet("\n"
                                       "QLabel {\n"
                                       "background-color: rgb(121, 121, 121);\n"
                                       "                border: 20px solid rgba(0, 0, 0, 128); /* Полупрозрачная черная рамка */\n"
                                       "                background-color: transparent;\n"
                                       "            }")
        self.mainPicture.setText("")

        self.gridLayout_6.addWidget(self.mainPicture, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.ButtonBrightness = BrightnessButton(self.centralwidget)
        self.ButtonBrightness.setMinimumSize(QtCore.QSize(150, 70))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ButtonBrightness.setFont(font)
        self.ButtonBrightness.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ButtonBrightness.setStyleSheet("QPushButton {\n"
                                            "   background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                            "    border: none;\n"
                                            "    outline: none;\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.ButtonBrightness.setText("")
        self.ButtonBrightness.setObjectName("ButtonBrightness")
        self.verticalLayout_3.addWidget(self.ButtonBrightness)
        self.ButtonBrightness.clicked.connect(self.more_brightness)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem8)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 0, 1, 1)
        self.TextAddBrightness = QtWidgets.QLabel(self.centralwidget)
        self.TextAddBrightness.setStyleSheet("background-color: rgba(48, 48, 48, 0);\n"
                                             "font: 63 10pt \"Cascadia Mono SemiBold\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "")
        self.TextAddBrightness.setObjectName("TextAddBrightness")
        self.gridLayout_4.addWidget(self.TextAddBrightness, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 3, 1, 1)
        self.ButtonRedCircle = CircleButton(self.centralwidget)
        self.ButtonRedCircle.setMinimumSize(QtCore.QSize(130, 130))
        self.ButtonRedCircle.setMaximumSize(QtCore.QSize(150, 150))
        self.ButtonRedCircle.setStyleSheet("QPushButton {\n"
                                           "   background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                           "    border: none;\n"
                                           "    outline: none;\n"

                                           "}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "")
        self.ButtonRedCircle.setText("")
        self.ButtonRedCircle.setObjectName("ButtonRedCircle")
        self.ButtonRedCircle.clicked.connect(self.red_circle)
        self.gridLayout_2.addWidget(self.ButtonRedCircle, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem13, 0, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem14, 0, 0, 1, 1)
        self.TextDrawACircle = QtWidgets.QLabel(self.centralwidget)
        self.TextDrawACircle.setStyleSheet("background-color: rgba(48, 48, 48,0);\n"
                                           "font: 63 10pt \"Cascadia Mono SemiBold\";\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "")
        self.TextDrawACircle.setObjectName("TextDrawACircle")
        self.gridLayout_3.addWidget(self.TextDrawACircle, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ButtonNegative = NegativeButton(self.centralwidget)
        self.ButtonNegative.setMinimumSize(QtCore.QSize(180, 90))
        self.ButtonNegative.setStyleSheet("QPushButton {\n"
                                          "   background-color: rgba(48, 48, 48, 0); /* Полупрозрачный фон */\n"
                                          "    border: none;\n"
                                          "    outline: none;\n"
                                          "}\n"
                                          "")
        self.ButtonNegative.setText("")
        self.ButtonNegative.setObjectName("ButtonNegative")
        self.verticalLayout_5.addWidget(self.ButtonNegative)
        self.ButtonNegative.clicked.connect(self.negative)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.TextAShowNegative = QtWidgets.QLabel(self.centralwidget)
        self.TextAShowNegative.setStyleSheet("background-color: rgba(48, 48, 48,0);\n"
                                             "font: 63 10pt \"Cascadia Mono SemiBold\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "")
        self.TextAShowNegative.setObjectName("TextAShowNegative")
        self.horizontalLayout_3.addWidget(self.TextAShowNegative)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem18)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 0, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem20, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RedButton = QtWidgets.QPushButton(self.centralwidget)
        self.RedButton.setMinimumSize(QtCore.QSize(51, 31))
        self.RedButton.setMaximumSize(QtCore.QSize(90, 80))
        self.RedButton.setBaseSize(QtCore.QSize(51, 31))
        self.RedButton.setStyleSheet("QPushButton {\n"
                                     "    background-color: #F44336; /* Красный */\n"
                                     "    border: none;\n"
                                     "    color: white;\n"
                                     "    padding: 15px 32px;\n"
                                     "    text-align: center;\n"
                                     "    text-decoration: none;\n"
                                     "    display: inline-block;\n"
                                     "    font-size: 16px;\n"
                                     "    margin: 4px 2px;\n"
                                     "    cursor: pointer;\n"
                                     "    border-radius: 8px;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: #e53935; \n"
                                     "}\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: #B71C1C; \n"
                                     "}\n"
                                     "\n"
                                     "")
        self.RedButton.setText("")
        self.RedButton.setObjectName("RedButton")

        self.verticalLayout_2.addWidget(self.RedButton)
        self.RedButton.clicked.connect(self.red_channel)

        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem21)
        self.GreenButton = QtWidgets.QPushButton(self.centralwidget)
        self.GreenButton.setMinimumSize(QtCore.QSize(51, 31))
        self.GreenButton.setMaximumSize(QtCore.QSize(90, 80))
        self.GreenButton.setStyleSheet(" QPushButton {\n"
                                       "            background-color: #4CAF50; /* Зелёный */\n"
                                       "            border: none;\n"
                                       "            color: white;\n"
                                       "            padding: 15px 32px;\n"
                                       "            text-align: center;\n"
                                       "            text-decoration: none;\n"
                                       "            display: inline-block;\n"
                                       "            font-size: 16px;\n"
                                       "            margin: 4px 2px;\n"
                                       "            cursor: pointer;\n"
                                       "            border-radius: 8px;\n"
                                       "        }\n"
                                       "        QPushButton:hover {\n"
                                       "            background-color: #45a049;\n"
                                       "        }\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(57, 132, 59); /* Ещё темнее при нажатии */\n"
                                       "}\n"
                                       "")
        self.GreenButton.setText("")
        self.GreenButton.setObjectName("GreenButton")
        self.verticalLayout_2.addWidget(self.GreenButton)
        self.GreenButton.clicked.connect(self.green_channel)

        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem22)
        self.BlueButton = QtWidgets.QPushButton(self.centralwidget)
        self.BlueButton.setMinimumSize(QtCore.QSize(51, 31))
        self.BlueButton.setMaximumSize(QtCore.QSize(90, 80))
        self.BlueButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: #2196F3; /* Синий */\n"
                                      "    border: none;\n"
                                      "    color: white;\n"
                                      "    padding: 15px 32px;\n"
                                      "    text-align: center;\n"
                                      "    text-decoration: none;\n"
                                      "    display: inline-block;\n"
                                      "    font-size: 16px;\n"
                                      "    margin: 4px 2px;\n"
                                      "    cursor: pointer;\n"
                                      "    border-radius: 8px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #1976d2; /* Более темный синий при наведении */\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:rgb(20, 101, 176); /* Ещё темнее при нажатии */\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.BlueButton.setText("")
        self.BlueButton.setObjectName("BlueButton")
        self.verticalLayout_2.addWidget(self.BlueButton)
        self.BlueButton.clicked.connect(self.blue_channel)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem23, 0, 3, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem24, 0, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem25)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem26)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 1, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem27)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1404, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.BackSignal.connect(self.changeIconBack)
        self.ForwardSignal.connect(self.changeIconForward)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def show_picture(self):
        """
        Метод, связанный с кнопкой ButtonGallery ("Выбрать фото"),
        использует модуль модуль Picture для загрузки изображения из галереи
        :return:
        """
        path = self.picture_module.load_picture()
        if path:
            self.mainPicture.setPixmap(QtGui.QPixmap(self.picture_module.path))
            self.mainPicture.setScaledContents(True)
            self.mainPicture.setObjectName("mainPicture")
            self.add_action_to_history(self.picture_module.picture)

    def red_channel(self):
        """
        Метод, связанный  с кнопкой RedButton,
        использует модуль Picture для показа красного канала изображения
        :return:
        """
        if self.picture_module.picture is not None:
            self.picture_module.show_red()
            pixmap = self.picture_module.qt_picture
            self.mainPicture.setPixmap(pixmap)
            self.mainPicture.setScaledContents(True)
            self.mainPicture.setObjectName("mainPicture")
            self.add_action_to_history(self.picture_module.picture)

    def green_channel(self):
        """
        Метод, связанный с кнопкой GreenButton,
        использует модуль Picture для показа зеленого канала изображения
        :return:
        """
        if self.picture_module.picture is not None:
            self.picture_module.show_green()
            pixmap = self.picture_module.qt_picture
            self.mainPicture.setPixmap(pixmap)
            self.mainPicture.setScaledContents(True)
            self.mainPicture.setObjectName("mainPicture")
            self.add_action_to_history(self.picture_module.picture)

    def negative(self):
        """
        Метод, связанный с кнопкой ButtonNegative("Показать негативное изображение"),
        использует модуль Picture для показа негативного изображения
        :return:
        """
        self.ButtonNegative.setIcon(QIcon("icons/pressed_znacok.negativ_.png"))
        self.setIconSize(QtCore.QSize(180, 90))
        if self.picture_module.picture is not None:
            self.picture_module.show_negative()
            pixmap = self.picture_module.qt_picture
            self.mainPicture.setPixmap(pixmap)
            self.mainPicture.setScaledContents(True)
            self.mainPicture.setObjectName("mainPicture")
            self.add_action_to_history(self.picture_module.picture)

    def blue_channel(self):
        """
       Метод, связанный с кнопкой BlueButton,
       использует модуль Picture для показа синего канала изображения
       :return:
       """

        if self.picture_module.picture is not None:
            self.picture_module.show_blue()
            pixmap = self.picture_module.qt_picture
            self.mainPicture.setPixmap(pixmap)
            self.mainPicture.setScaledContents(True)
            self.mainPicture.setObjectName("mainPicture")
            self.add_action_to_history(self.picture_module.picture)

    def open_camera_window(self):
        """
       Метод, связанный с кнопкой ButtonGallery_2("Сделать фото"),
       использует модуль CameraWindow, открывает окно с камерой
       :return:
       """
        self.camera_window = CameraWindow()
        self.camera_window.image_captured.connect(self.display_image)
        self.camera_window.show()

    def display_image(self, image, image_cv2):
        """
        Метод, отображающий фото с камеры на главном окне, при нажатии кнопки "Сделать фото"
        на окне с камерой
        """
        self.mainPicture.setPixmap(image)
        self.mainPicture.setScaledContents(True)
        self.mainPicture.setObjectName("mainPicture")
        self.picture_module.picture = image_cv2
        self.picture_module.qt_picture = image
        self.add_action_to_history(self.picture_module.picture)

    def more_brightness(self):
        """
               Метод, связанный с кнопкой ButtonBrightness("Увеличить яркость"),
               использует модуль FormBrightness, меняет иконку кнопки, а также
               открывает окно яркости
               :return:
               """

        self.ButtonBrightness.setIcon(QIcon("icons/pressed_free-icon-brightness-12411189.png"))
        self.ButtonBrightness.setIconSize(QtCore.QSize(64, 64))
        if self.picture_module.picture is not None:
            self.windowBrightness = FormBrightness()
            self.windowBrightness.show()
            self.windowBrightness.BrightnessSignal.connect(self.apply_brightness)

    def save_photo(self):
        """
        Метод сохраняет фото, используяя модуль Picture
        :return:
        """
        self.picture_module.save_picture_dialog()

    def apply_brightness(self, amount: int):
        """
        Метод увеличивает яркость изображения, используя модуль Picture
        :param amount: число, на сколько необходимо увеличить яркость
        :return:
        """
        self.picture_module.brighten(amount)
        pixmap = self.picture_module.qt_picture
        self.mainPicture.setPixmap(pixmap)
        self.mainPicture.setScaledContents(True)
        self.mainPicture.setObjectName("mainPicture")
        self.add_action_to_history(self.picture_module.picture)

    def red_circle(self):
        """
        Метод, открывающий окно с характеристиками круга, связан с кнопкой ButtonRedCircle("Нарисовать красный круг")
        :return:
        """
        if self.picture_module.picture is not None:
            self.windowCircle = FormCircle()
            self.windowCircle.show()
            self.windowCircle.CircleSignal.connect(self.apply_circle)

    def apply_circle(self, data_list: list):
        """
        Метод, рисующий круг на изображении, использует модуль Picture
        :param data_list: координаты, радиус и ширина линии рисуемого круга
        :return:
        """
        x, y, radius, line_size = data_list
        self.picture_module.draw_circle(x, y, radius, line_size)
        pixmap = self.picture_module.qt_picture
        self.mainPicture.setPixmap(pixmap)
        self.mainPicture.setScaledContents(True)
        self.mainPicture.setObjectName("mainPicture")
        self.add_action_to_history(self.picture_module.picture)

    def updateIcons(self):
        """
        Метод, обновляющий иконки на кнопках "Отменить действие" и "Отменить отмену действия"
        :return:
        """
        self.BackSignal.emit()
        self.ForwardSignal.emit()

    def add_action_to_history(self, cv2_photo):
        """
        Метод, добавляющий изображение в cv2 формате в очередь прошлых действий
        :param cv2_photo: фото в формате cv2(многомерный список)
        :return:
        """
        self.history.append(cv2_photo)
        self.future.clear()
        self.updateIcons()

    def changeIconBack(self):
        """Меняет иконку кнопки "Отменить действие" """
        if len(self.history) > 1:
            self.ButtonBack.setIcon(QIcon("icons/icons8-up-left-32.png"))
            self.ButtonBack.setIconSize(QtCore.QSize(32, 16))
        else:
            self.ButtonBack.setIcon(QIcon("icons/pressed_icons8-up-left-32.png"))
            self.ButtonBack.setIconSize(QtCore.QSize(32, 16))

    def changeIconForward(self):
        """"Меняет иконку кнопки "Отменить отмену действия" """
        if self.future:
            self.ButtonForward.setIcon(QIcon("icons/icon_forward.png"))
            self.ButtonForward.setIconSize(QtCore.QSize(32, 16))
        else:
            self.ButtonForward.setIcon(QIcon("icons/pressed_icon_forward.png"))
            self.ButtonForward.setIconSize(QtCore.QSize(32, 16))

    def undo(self):
        """Метод, связанный с кнопкой ButtonBack("Отменить действие"), отменяет действие:)"""
        if len(self.history) > 1:
            self.future.append(self.history.pop())
            previous_action = self.history[-1]
            self.picture_module.picture = previous_action
            pixmap = Picture.convert_cv_qt(previous_action)
            self.mainPicture.setPixmap(pixmap)
            self.mainPicture.setScaledContents(True)
            self.updateIcons()

    def forward(self):
        """Метод, связанный с кнопкой ButtonForward("Отменить отмену действия"), отменяет отмену действия:)"""
        if self.future:
            next_action = self.future.pop()
            self.history.append(next_action)
            self.picture_module.picture = next_action
            pixmap = Picture.convert_cv_qt(next_action)
            self.mainPicture.setPixmap(pixmap)
            self.mainPicture.setScaledContents(True)
            self.updateIcons()

    def retranslateUi(self):
        """
        Устанавливает текст для элементов интерфейса.
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Редактор фото"))
        self.TextAddPicture.setText(_translate("MainWindow", "Выбрать фото"))
        self.TextTakePhoto.setText(_translate("MainWindow", "Сделать фото"))
        self.TextAddBrightness.setText(_translate("MainWindow", "Увеличить яркость"))
        self.TextDrawACircle.setText(_translate("MainWindow", "Нарисовать красный\n"
                                                              "круг"))
        self.TextAShowNegative.setText(_translate("MainWindow", "Показать негативное\n"
                                                                "изображение"))
