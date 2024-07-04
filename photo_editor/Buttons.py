from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon


class Button(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_path = None
        self.hover_icon_path = None
        self.setIcon(QIcon(self.default_icon_path))

    def enterEvent(self, event):
        self.setIcon(QIcon(self.hover_icon_path))
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(QIcon(self.default_icon_path))
        super().leaveEvent(event)


class GalleryButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/icon_gallery_64.png"
        self.hover_icon_path = "icons/pressed_gallery_icon.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(64, 64))


class CameraButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/camera_icon.png"
        self.hover_icon_path = "icons/pressed_camera_icon.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(64, 64))

class BrightnessButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/icon-brightness.png"
        self.hover_icon_path = "icons/pressed-icon-brightness-12411189.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(64, 64))

class CircleButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/znacok.krug..png"
        self.hover_icon_path = "icons/pressed_znacok.krug_.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(130, 130))

class NegativeButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_icon_path = "icons/znacok.negativ..png"
        self.hover_icon_path = "icons/hover_znacok.negativ_.png"
        self.setIcon(QIcon(self.default_icon_path))
        self.setIconSize(QtCore.QSize(180, 90))


