from PyQt6.QtCore import QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton, QLabel, QListWidget, QCompleter, QHBoxLayout
from qfluentwidgets import (Action, Action, DropDownPushButton, DropDownToolButton, PushButton, PrimaryPushButton,
                            HyperlinkButton, setTheme, Theme, ToolButton, ToggleButton, RoundMenu,
                            SplitPushButton, SplitToolButton, PrimaryToolButton, PrimarySplitPushButton,
                            PrimarySplitToolButton, PrimaryDropDownPushButton, PrimaryDropDownToolButton,
                            TogglePushButton, ToggleToolButton, TransparentPushButton, TransparentToolButton,
                            TransparentToggleToolButton, TransparentTogglePushButton, TransparentDropDownToolButton,
                            TransparentDropDownPushButton, PillPushButton, PillToolButton, setCustomStyleSheet,
                            CustomStyleSheet, EditableComboBox, ComboBox)

from options import Options


class DeleteFile(QWidget):
	def __init__(self):
		super().__init__()

		self.opt = Options()
		self.deletefile_item = QListWidgetItem()
		self.label_delete = QLabel()
		self.combo_type = ComboBox()

		# Layout
		self.hbox_label_combo = QHBoxLayout()

		self.initUI()

	def initUI(self):
		# deletefile_item设置文本和字体
		self.deletefile_item.setText('删除指定类型文件')
		self.deletefile_item.setFont(QFont(self.opt.smiles_sans, self.opt.size_font))

		# label_delete_choose设置文本和字体
		self.label_delete.setText('删除类型 : ')
		self.label_delete.setGeometry(self.opt.x_label_delete, self.opt.y_label_delete, self.opt.weight_label_delete, self.opt.height_label_delete)
		self.label_delete.setFont(QFont(self.opt.smiles_sans, self.opt.size_font - 2))
		self.label_delete.hide()  # 隐藏

		# combo_type设置文本和字体 TODO:可以换成多选框
		type_list = ['txt', 'jpg', 'png', 'mp3', 'mp4', 'avi', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'pdf']
		self.combo_type.addItems(type_list)
		self.combo_type.setFont(QFont(self.opt.smiles_sans, self.opt.size_font - 2))
		self.combo_type.setCurrentIndex(-1)
		self.combo_type.setGeometry(self.opt.x_combo_type, self.opt.y_combo_type, self.opt.weight_combo_type, self.opt.height_combo_type)
		self.combo_type.hide()

		# Layout管理 TODO:应用层面重构
		# self.hbox_label_combo.addWidget(self.label_delete)
		# self.hbox_label_combo.addWidget(self.combo_type)


		# Connect管理

		self.returnItem()

	def showWidgets(self, flag):
		"""显示组件"""
		if flag:
			self.label_delete.show()
			self.combo_type.show()
		else:
			self.label_delete.hide()
			self.combo_type.hide()

	def returnItem(self):
		return {'deletefile_item': self.deletefile_item,
		        'label_delete': self.label_delete,
		        'combo_type': self.combo_type,
		        'hbox_label_combo': self.hbox_label_combo}
