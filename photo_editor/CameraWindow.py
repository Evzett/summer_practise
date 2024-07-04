"""
Модуль для работы с камерой и захвата изображений с использованием PyQt5 и OpenCV.

Этот модуль предоставляет класс CameraWindow, который позволяет подключаться к веб-камере,
отображать видеопоток в реальном времени, делать снимки и обрабатывать их.
"""

import os
import sys
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
import cv2
from photo_editor.Picture import Picture
import numpy as np


class CameraWindow(QWidget):
    """
    Класс для работы с камерой и захвата изображений.

    Сигналы:
        image_captured (pyqtSignal): Сигнал, испускаемый при захвате изображения.
    """
    image_captured = pyqtSignal(QPixmap, np.ndarray)

    def __init__(self):
        """
        Инициализирует объект CameraWindow и подключается к веб-камере.
        """
        super().__init__()
        self.initUI()
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            self.show_error_message("Не удалось подключиться к веб-камере.")
            return
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def initUI(self):
        """
        Инициализирует пользовательский интерфейс окна камеры.
        """
        self.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.setWindowTitle('Камера')
        self.setGeometry(100, 100, 800, 600)
        self.smile_label = QLabel('Улыбнитесь!!!', self)
        self.smile_label.setAlignment(Qt.AlignCenter)
        self.smile_label.setStyleSheet("font-size: 20px; font-weight: bold; color: rgb(255, 255, 255)")

        self.image_label = QLabel(self)
        self.image_label.resize(700, 500)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.capture_btn = QPushButton('Сделать фото', self)
        self.capture_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(244, 227, 195, 0.5); 
                font: 87 italic 16pt "Segoe UI Black";
                color: rgb(61, 61, 61);
                border-radius: 10px;  
            }
            QPushButton:hover {
                background-color: rgba(244, 227, 195, 0.7);  
                color: rgb(51, 51, 51);  
            }
            QPushButton:pressed {
                background-color: rgba(244, 227, 195, 0.9);  
                color: rgb(41, 41, 41); 
            }
        """)
        self.capture_btn.clicked.connect(self.capture_image)

        layout = QVBoxLayout()
        layout.addWidget(self.smile_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.capture_btn)
        self.setLayout(layout)

    def update_frame(self):
        """
        Обновляет кадр с камеры и отображает его в интерфейсе.

        """
        frame = Picture.get_frame(self.cap)
        if frame is not None:
            self.image_label.setPixmap(Picture.convert_cv_qt(frame))

    def capture_image(self):
        """
        Захватывает изображение с камеры, сохраняет его и испускает сигнал image_captured.
        """
        picture_instance = Picture()
        picture_instance.capture_and_store_image(self.cap)
        self.image_captured.emit(picture_instance.qt_picture, picture_instance.picture)
        self.close()

    def show_error_message(self, message):
        """
        Отображает сообщение об ошибке.

        :param message: Текст сообщения об ошибке.
        :type message: str
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def current_path(self, name):
        """
        Возвращает путь к файлу в родительском каталоге текущего скрипта.

        :param name: Имя файла.
        :type name: str
        :return: Путь к файлу.
        :rtype: str
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(current_directory)
        file_path = os.path.join(parent_directory, name)
        return file_path

    def closeEvent(self, event):
        """
        Обрабатывает событие закрытия окна и освобождает ресурсы камеры.

        :param event: Событие закрытия.
        :type event: QtCore.QEvent
        """
        self.cap.release()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    sys.exit(app.exec_())
