"""
Модуль для работы с изображениями с использованием OpenCV и PyQt5.

Этот модуль предоставляет класс Picture, который позволяет загружать,
сохранять и обрабатывать изображения, а также отображать их с использованием PyQt5.
"""

import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QFileDialog


class Picture:
    """
    Класс для работы с изображениями.

    Этот класс предоставляет методы для загрузки, сохранения и обработки изображений,
    а также для отображения изображений с использованием PyQt5.
    """

    def __init__(self):
        """
        Инициализирует объект Picture с атрибутами по умолчанию.
        """
        self.qt_picture = None
        self.path = None
        self.picture = None
        self.width = None
        self.height = None

    def load_picture(self):
        """
        Открывает диалоговое окно для загрузки изображения из файловой системы.

        :return: Путь к файлу, если изображение выбрано, иначе None.
        :rtype: str
        """
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

    def save_picture_dialog(self):
        """
        Открывает диалоговое окно для сохранения текущего изображения.
        """
        if self.picture is not None:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(
                None,
                "Сохранить изображение",
                "",
                "PNG Files (*.png);;JPEG Files (*.jpeg);;JPG Files (*.jpg);;All Files (*)",
                options=options
            )
            if file_name:
                if file_name.lower().endswith(('.png', '.jpeg', '.jpg')):
                    cv2.imwrite(file_name, self.picture)
                else:
                    # Если пользователь не указал расширение, добавим .png по умолчанию
                    cv2.imwrite(file_name + '.png', self.picture)

    def show_red(self):
        """
        Отображает изображение с выделенным красным цветом.
        """
        if self.picture is not None:
            red_picture = self.picture.copy()
            red_picture[:, :, 0] = 0
            red_picture[:, :, 1] = 0
            self.qt_picture = Picture.convert_cv_qt(red_picture)
            self.picture = red_picture

    @staticmethod
    def get_frame(cap):
        """
        Захватывает кадр с камеры.

        :param cap: Объект VideoCapture для захвата изображения с камеры.
        :type cap: cv2.VideoCapture
        :return: Захваченный кадр, если захват успешен, иначе None.
        :rtype: numpy.ndarray
        """
        ret, frame = cap.read()
        if ret:
            return frame
        return None

    @staticmethod
    def capture_image(cap):
        """
        Захватывает изображение с камеры.

        :param cap: Объект VideoCapture для захвата изображения с камеры.
        :type cap: cv2.VideoCapture
        :return: Кортеж, содержащий QPixmap для отображения изображения в PyQt5 и захваченный кадр.
        :rtype: tuple
        """
        ret, frame = cap.read()
        if ret:
            return Picture.convert_cv_qt(frame), frame
        return None, None

    def capture_and_store_image(self, cap):
        """
        Захватывает изображение с камеры и сохраняет его в атрибуты объекта.

        :param cap: Объект VideoCapture для захвата изображения с камеры.
        :type cap: cv2.VideoCapture
        """
        qt_image, frame = Picture.capture_image(cap)
        if qt_image is not None and frame is not None:
            self.qt_picture = qt_image
            self.picture = frame

    def save_picture(self, path):
        """
        Сохраняет текущее изображение по указанному пути.

        :param path: Путь для сохранения изображения.
        :type path: str
        """
        if self.picture is not None:
            cv2.imwrite(path, cv2.cvtColor(self.picture, cv2.COLOR_RGB2BGR))

    @staticmethod
    def convert_cv_qt(cv_img):
        """
        Конвертирует изображение OpenCV в QPixmap для отображения в PyQt5.

        :param cv_img: Изображение OpenCV.
        :type cv_img: numpy.ndarray
        :return: Изображение для отображения в PyQt5.
        :rtype: QPixmap
        """
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(convert_to_Qt_format)

    def show_green(self):
        """
        Отображает изображение с выделенным зеленым цветом.
        """
        if self.picture is not None:
            green_picture = self.picture.copy()
            green_picture[:, :, 0] = 0
            green_picture[:, :, 2] = 0
            self.qt_picture = Picture.convert_cv_qt(green_picture)
            self.picture = green_picture

    def show_blue(self):
        """
        Отображает изображение с выделенным синим цветом.
        """
        if self.picture is not None:
            blue_picture = self.picture.copy()
            blue_picture[:, :, 1] = 0
            blue_picture[:, :, 2] = 0
            self.qt_picture = Picture.convert_cv_qt(blue_picture)
            self.picture = blue_picture

    def show_negative(self):
        """
        Отображает негативное изображение.
        """
        if self.picture is not None:
            negative_picture = cv2.bitwise_not(self.picture)
            self.qt_picture = Picture.convert_cv_qt(negative_picture)
            self.picture = negative_picture

    def brighten(self, amount):
        """
        Увеличивает яркость изображения.

        :param amount: Величина увеличения яркости.
        :type amount: int
        """
        if self.picture is not None:
            contrast = 1.0
            bright_picture = cv2.convertScaleAbs(self.picture, alpha=contrast, beta=amount)
            self.qt_picture = Picture.convert_cv_qt(bright_picture)
            self.picture = bright_picture

    def draw_circle(self, x, y, radius, line_size):
        """
        Рисует круг на изображении.

        :param x: Координата x центра круга.
        :type x: int
        :param y: Координата y центра круга.
        :type y: int
        :param radius: Радиус круга.
        :type radius: int
        :param line_size: Толщина линии круга.
        :type line_size: int
        """
        if self.picture is not None:
            coord = (x, y)
            color = (0, 0, 255)
            circle_picture = self.picture.copy()
            self.qt_picture = Picture.convert_cv_qt(cv2.circle(circle_picture, coord, radius, color, line_size))
            self.picture = circle_picture
