from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, \
	QTextEdit, QLineEdit


class ACLabel(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		lbl1 = QLabel('A', self)
		lbl1.move(15, 10)

		lbl2 = QLabel('B', self)
		lbl2.move(35, 40)

		lbl3 = QLabel('C', self)
		lbl3.move(55, 70)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Absolute')
		self.show()


class HVBox(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		okButton = QPushButton('OK')
		cancelButton = QPushButton('NO')

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Buttons')
		self.show()


class GridLayout(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.setLayout(grid)

		names = ['Cls', 'Bck', '', 'Close',
		         '7', '8', '9', '/',
		         '4', '5', '6', '*',
		         '1', '2', '3', '-',
		         '0', '.', '=', '+']

		positions = [(i, j) for i in range(5) for j in range(4)]

		for position, name in zip(positions, names):
			if name == '':
				continue

			button = QPushButton(name)
			grid.addWidget(button, *position)

		self.move(300, 150)
		self.setWindowTitle('GridLayout')
		self.show()


class Reply(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		grid.setSpacing(10)
		self.setLayout(grid)

		lb1 = QLabel('Title', self)
		lb2 = QLabel('Author', self)
		lb3 = QLabel('Review', self)

		text1 = QLineEdit()
		text2 = QLineEdit()
		text3 = QTextEdit()

		grid.addWidget(lb1, 0, 0)
		grid.addWidget(lb2, 1, 0)
		grid.addWidget(lb3, 2, 0)

		grid.addWidget(text1, 0, 1)
		grid.addWidget(text2, 1, 1)
		grid.addWidget(text3, 2, 1, 5, 1)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Reply')
		self.show()
