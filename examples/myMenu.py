from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu, QTextEdit
from PyQt6.QtGui import QIcon, QAction


class Menu(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		exitAct = QAction(QIcon('exit.png'), '&Exit', self)
		exitAct.setShortcut('Ctrl + T')
		exitAct.setStatusTip('Exit Application')
		exitAct.triggered.connect(QApplication.instance().quit)

		self.statusBar()  # 获取或创建一个状态栏用于存放菜单

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('$File')
		fileMenu.addAction(exitAct)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Simple Menu')
		self.show()


class SubMenu(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		menubar = self.menuBar()  # 获取menuBar对象
		fileMenu = menubar.addMenu('File')  # 返回菜单对象

		impMenu = QMenu('Import', self)
		impAct = QAction('Import mail', self)
		impMenu.addAction(impAct)

		newAct = QAction('New', self)

		fileMenu.addAction(newAct)  # 选项用addAction，对应QAction
		fileMenu.addMenu(impMenu)  # 子菜单用addMenu，对应QMenu

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('SubMenu')
		self.show()


class CheckMenu(QMainWindow):
	def __init__(self):
		super().__init__()

		self.statusbar = self.statusBar()
		self.initUI()

	def initUI(self):
		self.statusbar.showMessage('Ready')

		menubar = self.menuBar()
		viewMenu = menubar.addMenu('View')

		viewStatAct = QAction('View StatusBar', self, checkable=True)  # checkable用于设置一个可以勾选的菜单
		viewStatAct.setStatusTip('View Status')  # 状态栏提示
		viewStatAct.setChecked(True)  # 默认打勾
		viewStatAct.triggered.connect(self.toggleMenu)  # 信号连接

		viewMenu.addAction(viewStatAct)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('CheckMenu')
		self.show()

	def toggleMenu(self, state):
		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()


class ContextMenu(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Context Menu')
		self.show()

	def contextMenuEvent(self, event):
		cmenu = QMenu(self)

		newAct = cmenu.addAction('New')
		openAct = cmenu.addAction('Open')
		quitAct = cmenu.addAction('Quit')
		action = cmenu.exec(self.mapToGlobal(event.pos()))  # exec期待一个全局坐标，并返回这个坐标代表的选项，返回QAction类型

		if action == quitAct:
			QApplication.instance().quit()


class Toolbar(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(QApplication.instance().quit)

		self.toolbar = self.addToolBar('Exit')  # 创建工具栏
		self.toolbar.addAction(exitAct)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Toolbar')
		self.show()


class MainWin(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		exitAct = QAction(QIcon('exit24.png'),'Exit',self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.setStatusTip('Exit Application')
		exitAct.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')
		fileMenu.addAction(exitAct)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAct)

		self.setGeometry(300,300,350,250)
		self.setWindowTitle('Main Windows')
		self.show()