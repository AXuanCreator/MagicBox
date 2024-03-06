from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QGridLayout, QLabel, QPushButton, \
	QMainWindow


class SignalSlot(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		lcd = QLCDNumber(self)
		sld = QSlider(Qt.Orientation.Horizontal, self)

		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Signal and Slot')
		self.show()


class EscapeEvent(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Event Handler')
		self.show()

	def keyPressEvent(self, a0):
		if a0.key() == Qt.Key.Key_Escape.value:
			self.close()


class MouseEvent(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		x = 0
		y = 0

		self.text = f'x : {x} , y : {y}'

		self.lable = QLabel(self.text, self)
		grid.addWidget(self.lable, 0, 0, Qt.AlignmentFlag.AlignTop)

		self.setMouseTracking(True)
		self.setLayout(grid)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Mouse Event')
		self.show()

	def mouseMoveEvent(self, a0):
		x = int(a0.position().x())
		y = int(a0.position().y())

		text = f'x : {x} , y : {y}'
		self.lable.setText(text)


class WhichButton(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		btn1 = QPushButton('B1', self)
		btn1.move(30, 50)

		btn2 = QPushButton('B2', self)
		btn2.move(150, 50)

		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)

		self.statusBar()

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Which Button')
		self.show()

	def buttonClicked(self):
		sender = self.sender()  # sender用于获取发送信号的对象

		msg = f'{sender.text()} Was Pressed'
		self.statusBar().showMessage(msg)


class Communicate(QObject):
	closeApp = pyqtSignal()  # 创建信号


class TrigSignal(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.c = Communicate()
		self.c.closeApp.connect(self.close)  # 将信号连接close槽

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Emit Signal')
		self.show()

	def mousePressEvent(self, a0):
		self.c.closeApp.emit()  # 当[事件：鼠标点击]时，发出信号。槽接受信号


