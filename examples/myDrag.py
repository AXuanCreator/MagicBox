from PyQt6.QtWidgets import QWidget, QCheckBox, QApplication, QFrame, QPushButton, QSlider, QLabel, QProgressBar, \
	QVBoxLayout, QCalendarWidget, QHBoxLayout, QLineEdit, QSplitter, QComboBox
from PyQt6.QtCore import Qt, QBasicTimer, QDate, QMimeData
from PyQt6.QtGui import QColor, QPixmap, QDrag


class ButtonAIDDragDrop(QPushButton):
	def __init__(self, tittle, parent):
		super().__init__(tittle, parent)

		self.setAcceptDrops(True)  # 允许部件的释放事件

	def dragEnterEvent(self, a0):
		"""
		定义接受的数据类型--纯文本
		在拖动的对象首次进入部件的区域时触发
		"""
		if a0.mimeData().hasFormat('text/plain'):
			a0.accept()
		else:
			a0.ignore()

	def dropEvent(self, a0):
		"""
		修改按钮文本
		在拖动的对象被释放时触发
		"""
		self.setText(a0.mimeData().text())


class DragDrop(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		edit = QLineEdit('', self)
		edit.setDragEnabled(True)
		edit.move(30, 65)

		button = ButtonAIDDragDrop('Button', self)
		button.move(190, 65)

		self.setWindowTitle('Drag and Drop')
		self.show()


class AIDButton(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)

	def mouseMoveEvent(self, e):
		print('Mouse Move Event')
		if e.buttons() != Qt.MouseButton.RightButton:
			return

		mimeData = QMimeData()

		drag = QDrag(self)  # 此部件允许拖动
		drag.setMimeData(mimeData)
		drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())  # 设置部件的热点，即鼠标位置。移动后鼠标与部件的相对位置不会发生改变

		dropAction = drag.exec(Qt.DropAction.MoveAction)

	def mousePressEvent(self, e):
		print('Mouse Press Event')

		super().mousePressEvent(e)

		if e.button() == Qt.MouseButton.LeftButton:
			print('press')


class DragDropButton(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setAcceptDrops(True)

		self.button = AIDButton('Button', self)
		self.button.move(100, 65)

		self.setWindowTitle('Click or Move')
		self.setGeometry(300, 300, 550, 450)
		self.show()

	def dragEnterEvent(self, a0):
		print('Drag Enter Event')
		print(a0)
		a0.accept()

	def dropEvent(self, e):
		print('Drop Event')
		print(e)
		position = e.position()
		self.button.move(position.toPoint())

		e.setDropAction(Qt.DropAction.MoveAction)
		e.accept()