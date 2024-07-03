import cv2
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QFileDialog


class Picture:
    def __init__(self):

        self.qt_picture = None
        self.path = None
        self.picture = None
        self.width = None
        self.height = None

    def load_picture(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Выбрать фото",
            "",
            "Images (*.png *.jpeg *.jpg);;All Files (*)",
            options=options
        )
        if file_name:
            self.picture = cv2.imread(file_name)
            self.path = file_name

            return file_name
        return None


    def capture_picture(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, self.width)
        cap.set(4, self.height)

        while True:
            res, img = cap.read()
            key = cv2.waitKey(1)

            # Если нажата клавиша 's', сохраняем кадр и выходим из цикла
            if key == ord('s'):
                cv2.imwrite('screenshot.png', img)
                break

    def show_red(self):
        if self.picture is not None:
            red_picture = self.picture.copy()
            red_picture[:, :, 0] = 0
            red_picture[:, :, 1] = 0
            self.qt_picture = self.convert_cv_qt(red_picture)
            self.picture = red_picture


    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(convert_to_Qt_format)

    def show_green(self):
        if self.picture is not None:
            green_picture = self.picture.copy()
            green_picture[:, :, 0] = 0
            green_picture[:, :, 2] = 0
            self.qt_picture = self.convert_cv_qt(green_picture)
            self.picture = green_picture

    def show_blue(self):
        if self.picture is not None:
            blue_picture = self.picture.copy()
            blue_picture[:, :, 1] = 0
            blue_picture[:, :, 2] = 0
            self.qt_picture = self.convert_cv_qt(blue_picture)
            self.picture = blue_picture

    def show_negative(self):

        if self.picture is not None:
            negative_picture = cv2.bitwise_not(self.picture)
            self.qt_picture = self.convert_cv_qt(negative_picture)
            self.picture = negative_picture

    def brighten(self, amount):
        if self.picture is not None:
            contrast = 1.0
            bright_picture = cv2.convertScaleAbs(self.picture, alpha=contrast, beta=amount)
            self.qt_picture = self.convert_cv_qt(bright_picture)
            self.picture = bright_picture


    def draw_circle(self, x, y, radius, line_size):
        if self.picture is not None:
            coord = (x, y)
            color = (0, 0, 255)
            circle_picture = self.picture.copy()
            self.qt_picture = self.convert_cv_qt(cv2.circle(circle_picture, coord, radius, color, line_size))
            self.picture = circle_picture

