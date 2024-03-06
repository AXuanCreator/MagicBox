import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from qfluentwidgets.components.widgets.button import PushButton

from mainwindow import MainWindow


def main():
	app = QApplication(sys.argv)

	mw = MainWindow()

	sys.exit(app.exec())


if __name__ == '__main__':
	main()
