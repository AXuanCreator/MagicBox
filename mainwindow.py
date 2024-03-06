from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QListWidget, QListWidgetItem
from qfluentwidgets import ListWidget, RoundMenu, Action
from qfluentwidgets import FluentIcon as FIF

from options import Options
from delete_specified_type_file import DeleteFile


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# 实例
		self.opt = Options()  # 设置文件
		self.df = DeleteFile()

		# 组件返回赋值，注意这里的返回值是一个字典
		self.delete_widgets = self.df.returnItem()

		# Mainwindow原生组件
		self.hBoxLayout_listview = QHBoxLayout(self)
		self.listWidget_main = ListWidget(self)
		self.statusBar()

		self.initUI()

	def initUI(self):
		"""所有初始化程序"""
		self.setGeometry(100, 100, self.opt.weight_mainwindows, self.opt.height_mainwindows)
		self.setWindowTitle('Magic Box')

		# 添加组件
		self.__addWidget()

		# 设置列表，并将其加入到水平布局中
		self.__setListView()
		# self.hBoxLayout_listview.setContentsMargins(0, 0, 0, 0)  # 设置外边距，紧密贴合窗口
		# self.hBoxLayout_listview.addWidget(self.listWidget_main)

		#### 连接
		# 点击第一个item时
		self.listWidget_main.itemClicked.connect(self.__connect_listview)

		self.show()

	def __connect_listview(self, item):
		"""选择item"""
		if item.text() == '删除指定类型文件':
			self.df.showWidgets(True)
		else:
			self.df.showWidgets(False)

	def __setListView(self):
		"""列表，用于向ListWidge添加Item"""
		self.listWidget_main.setGeometry(0, 0, self.opt.weight_listview_main, self.opt.height_listview_main)
		self.listWidget_main.addItem(self.delete_widgets['deletefile_item'])
		self.listWidget_main.addItem(QListWidgetItem('TEST'))

	def __addWidget(self):
		"""用于添加组件至Mainwindows"""
		self.delete_widgets['label_delete'].setParent(self)  # 删除指定类型文件的标签
		self.delete_widgets['combo_type'].setParent(self)  # 删除指定类型文件的下拉框




if __name__ == '__main__':
	print('ERROR')
