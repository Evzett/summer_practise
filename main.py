import sys

from PyQt5 import QtWidgets

from photo_editor.mainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())