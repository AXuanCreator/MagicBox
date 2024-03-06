from PyQt6.QtWidgets import QWidget, QCheckBox, QApplication, QFrame, QPushButton, QSlider, QLabel, QProgressBar, \
	QVBoxLayout, QCalendarWidget, QHBoxLayout, QLineEdit, QSplitter, QComboBox
from PyQt6.QtCore import Qt, QBasicTimer, QDate
from PyQt6.QtGui import QColor, QPixmap


class CheckBox(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		cb = QCheckBox('Show Title', self)
		cb.move(20, 20)
		cb.toggle()
		cb.stateChanged.connect(self.changeTitle)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('QCheckBox')
		self.show()

	def changeTitle(self, state):
		if state == Qt.CheckState.Checked.value:
			self.setWindowTitle('QCheckBox')
		else:
			self.setWindowTitle(' ')


class ToggleButton(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.col = QColor(0, 0, 0)

		redb = QPushButton('Red', self)
		redb.setCheckable(True)  # 将按钮设置为拥有选择/未选择两种状态
		redb.move(10, 10)

		redb.clicked[bool].connect(self.setColor)

		greenb = QPushButton('Green', self)
		greenb.setCheckable(True)
		greenb.move(10, 60)

		greenb.clicked[bool].connect(self.setColor)

		blueb = QPushButton('Blue', self)
		blueb.setCheckable(True)
		blueb.move(10, 110)

		blueb.clicked[bool].connect(self.setColor)

		self.square = QFrame(self)
		self.square.setGeometry(150, 20, 100, 100)
		self.square.setStyleSheet('QWidget { background-color: %s }' % self.col.name())

		self.setGeometry(300, 300, 300, 250)
		self.setWindowTitle('Toggle Button')
		self.show()

	def setColor(self, pressed):
		source = self.sender()  # 获取发出信号的对象

		if pressed:
			val = 255
		else:
			val = 0

		if source.text() == 'Red':
			self.col.setRed(val)
		elif source.text() == 'Green':
			self.col.setGreen(val)
		else:
			self.col.setBlue(val)

		self.square.setStyleSheet('QFrame { background-color: %s }' % self.col.name())


class Slider(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		sld = QSlider(Qt.Orientation.Horizontal, self)
		sld.setFocusPolicy(Qt.FocusPolicy.NoFocus)
		sld.setGeometry(30, 40, 200, 30)
		sld.valueChanged[int].connect(self.changeValue)

		self.label = QLabel(self)
		self.label.setPixmap(QPixmap('mute.png'))
		self.label.setGeometry(250, 40, 80, 30)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('QSlider')
		self.show()

	def changeValue(self, value):
		if value == 0:
			self.label.setPixmap(QPixmap('mute.png'))
		elif 0 < value < 30:
			self.label.setPixmap(QPixmap('min.png'))
		elif 30 < value < 80:
			self.label.setPixmap(QPixmap('med.png'))
		else:
			self.label.setPixmap(QPixmap('max.png'))


class ProgressBar(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.pbar = QProgressBar(self)
		self.pbar.setGeometry(30, 40, 200, 25)

		self.btn = QPushButton('Start', self)
		self.btn.move(40, 80)
		self.btn.clicked.connect(self.doAction)

		self.timer = QBasicTimer()
		self.step = 0

		self.setGeometry(300, 300, 280, 170)
		self.setWindowTitle('QProgressBar')
		self.show()

	def timerEvent(self, e):
		if self.step >= 100:
			self.timer.stop()
			self.btn.setText('Finished')

		self.step = self.step + 1
		self.pbar.setValue(self.step)

	def doAction(self):
		if self.timer.isActive():
			self.timer.stop()
			self.btn.setText('Start')
		else:
			self.timer.start(100, self)  # 启动计时器，并在每100毫秒触发timerEvent事件
			self.btn.setText('Stop')


class CalendarWidget(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		vbox = QVBoxLayout(self)

		cal = QCalendarWidget(self)
		cal.setGridVisible(True)
		cal.clicked[QDate].connect(self.showDate)

		vbox.addWidget(cal)

		self.lbl = QLabel(self)
		date = cal.selectedDate()
		self.lbl.setText(date.toString())

		vbox.addWidget(self.lbl)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Calendar')
		self.show()

	def showDate(self, date):
		self.lbl.setText(date.toString())


class Pixmap(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		hbox = QHBoxLayout(self)
		pixmap = QPixmap('sid.jpg')

		lbl = QLabel(self)
		lbl.setPixmap(pixmap)

		hbox.addWidget(lbl)
		self.setLayout(hbox)

		self.move(300, 200)
		self.setWindowTitle('Sid')
		self.show()


class LineEdit(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.lbl = QLabel(self)
		qle = QLineEdit(self)

		qle.move(60, 100)
		self.lbl.move(60, 40)

		qle.textChanged[str].connect(self.onChanged)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('QLineEdit')
		self.show()

	def onChanged(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()


class Spliter(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		hbox = QHBoxLayout(self)

		topleft = QFrame(self)
		topleft.setFrameShape(QFrame.Shape.StyledPanel)

		topright = QFrame(self)
		topright.setFrameShape(QFrame.Shape.StyledPanel)

		bottom = QFrame(self)
		bottom.setFrameShape(QFrame.Shape.StyledPanel)

		splitter1 = QSplitter(Qt.Orientation.Horizontal)
		splitter1.addWidget(topleft)
		splitter1.addWidget(topright)

		splitter2 = QSplitter(Qt.Orientation.Vertical)
		splitter2.addWidget(splitter1)
		splitter2.addWidget(bottom)

		hbox.addWidget(splitter2)

		splitter1.setToolTip('s1')
		splitter2.setToolTip('s2')

		self.setLayout(hbox)

		self.setGeometry(300, 300, 450, 400)
		self.setWindowTitle('QSplitter')
		self.show()


class ComboBox(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.lbl = QLabel('Choose', self)

		combo = QComboBox(self)

		combo.addItem('A')
		combo.addItem('B')
		combo.addItem('C')
		combo.addItem('D')

		combo.move(50, 50)
		self.lbl.move(50, 150)

		combo.textActivated[str].connect(self.onActivated)

		self.setGeometry(300, 300, 450, 400)
		self.setWindowTitle('QComboBox')
		self.show()

	def onActivated(self, text):
		self.lbl.setText(text)
		self.lbl.adjustSize()
