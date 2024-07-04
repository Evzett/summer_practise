"""
Модуль для создания кнопок с использованием PyQt5.

Этот модуль предоставляет классы для создания кнопок с различными иконками и состояниями
(по умолчанию и при наведении), а также специализированные кнопки для галереи, камеры,
регулировки яркости, рисования круга и негативного эффекта.
"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon

class Button(QtWidgets.QPushButton):
    """
    Класс для создания кнопки с иконками для состояний по умолчанию и при наведении.

    Атрибуты:
        default_icon_path (str): Путь к иконке по умолчанию.
        hover_icon_path (str): Путь к иконке при наведении.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект Button с заданными параметрами.
        """
        super().__init__(*args, **kwargs)
        self.default_icon_path = None
        self.hover_icon_path = None
        self.setIcon(QIcon(self.default_icon_path))

    def enterEvent(self, event):
        """
        Обрабатывает событие наведения курсора на кнопку.

        :param event: Событие наведения курсора.
        :type event: QtCore.QEvent
        """
        self.setIcon(QIcon(self.hover_icon_path))
        super().enterEvent(event)

    def leaveEvent(self, event):
        """
        Обрабатывает событие ухода курсора с кнопки.

        :param event: Событие ухода курсора.
        :type event: QtCore.QEvent
        """
        self.setIcon(QIcon(self.default_icon_path))
        super().leaveEvent(event)

class GalleryButton(Button):
    """
    Класс для создания кнопки галереи с иконками для состояний по умолчанию и при наведении.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект GalleryButton с заданными параметрами.

        """
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/icon_gallery_64.png"
        self.hover_icon_path = "icons/pressed_gallery_icon.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(64, 64))

class CameraButton(Button):
    """
    Класс для создания кнопки камеры с иконками для состояний по умолчанию и при наведении.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект CameraButton с заданными параметрами.


        """
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/camera_icon.png"
        self.hover_icon_path = "icons/pressed_camera_icon.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(64, 64))

class BrightnessButton(Button):
    """
    Класс для создания кнопки регулировки яркости с иконками для состояний по умолчанию и при наведении.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект BrightnessButton с заданными параметрами.

        """
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/icon-brightness.png"
        self.hover_icon_path = "icons/pressed-icon-brightness-12411189.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(64, 64))

class CircleButton(Button):
    """
    Класс для создания кнопки рисования круга с иконками для состояний по умолчанию и при наведении.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект CircleButton с заданными параметрами.

        """
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/znacok.krug..png"
        self.hover_icon_path = "icons/pressed_znacok.krug_.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(130, 130))

class NegativeButton(Button):
    """
    Класс для создания кнопки негативного эффекта с иконками для состояний по умолчанию и при наведении.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект NegativeButton с заданными параметрами.

        """
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/znacok.negativ..png"
        self.hover_icon_path = "icons/hover_znacok.negativ_.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(180, 90))
