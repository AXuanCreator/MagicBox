import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox


class Bubble(QWidget):
	def __init__(self):
		super().__init__()
		self.exit = Exit()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))

		self.setToolTip('This is a <b>QWidget</b> widget')

		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>PushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(50, 50)

		# self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('BubbleTips')
		self.show()


class Exit(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(100, 100)

		# self.setGeometry(300,300,350,250)
		self.setWindowTitle('Exit')
		self.show()


class ExitPro(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 350, 200)
		self.setWindowTitle('MessageBox')
		self.show()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message',
		                             'Are You Need To Quit?',
		                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

		if reply == QMessageBox.StandardButton.Yes:
			event.accept()
		else:
			event.ignore()


class Center(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.resize(350, 250)
		self.center()

		self.setWindowTitle('Center Box')
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = self.screen().availableGeometry().center()

		qr.moveCenter(cp)
		self.move(qr.topLeft())

