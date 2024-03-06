from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QFrame, QColorDialog, \
	QVBoxLayout, QSizePolicy, QLabel, QFontDialog, QMainWindow, QFileDialog, QTextEdit
from PyQt6.QtGui import QColor, QIcon, QAction
from pathlib import Path


class InputDialog(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.btn = QPushButton('Dialog', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)

		self.le = QLineEdit(self)
		self.le.move(130, 22)

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Input Dialog')
		self.show()

	def showDialog(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter Your Name : ')

		if ok:
			self.le.setText(str(text))


class ColorDialog(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		col = QColor(0, 0, 0)

		self.btn = QPushButton('Dialog', self)
		self.btn.move(20, 20)

		self.btn.clicked.connect(self.showDialog)

		self.frm = QFrame(self)
		self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
		self.frm.setGeometry(130, 22, 200, 200)

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Color Dialog')
		self.show()

	def showDialog(self):
		col = QColorDialog.getColor()

		if col.isValid():
			self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


class FontDialog(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		vbox = QVBoxLayout()

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
		btn.move(20, 20)

		vbox.addWidget(btn)

		btn.clicked.connect(self.showDialog)

		self.lbl = QLabel('Knowledge Only Matters', self)
		self.lbl.move(130, 20)

		vbox.addWidget(self.lbl)
		self.setLayout(vbox)

		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle('Font Dialog')
		self.show()

	def showDialog(self):
		font, ok = QFontDialog.getFont()

		if ok:
			self.lbl.setFont(font)


class FileDialog(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open New File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		filemenu = menubar.addMenu('&File')
		filemenu.addAction(openFile)


		self.statusBar().showMessage('HelloWorld')

		self.setGeometry(300, 300, 550, 450)
		self.setWindowTitle('File Dialog')
		self.show()

	def showDialog(self):
		home_dir = str(Path.home())
		fname = QFileDialog.getOpenFileName(self, 'Open File', home_dir)

		if fname[0]:
			f = open(fname[0], 'r')

			with f:
				data = f.read()
				self.textEdit.setText(f'The File Open In : [{fname[0]}]')
				self.textEdit.setText(data)
