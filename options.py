from PyQt6.QtGui import QFont


class Options():
	def __init__(self):
		# [./mainwindow.py] Mainwindow
		self.weight_mainwindows = 1000
		self.height_mainwindows = 700

		# [./mainwindow.py] ListView
		self.weight_listview_main = 200
		self.height_listview_main = self.height_mainwindows

		# Font
		self.smiles_sans = '得意黑'
		self.size_font = 18

		# [./delete_sepcified_type_file.py] label-delete
		self.x_label_delete = 600
		self.y_label_delete = 20
		self.weight_label_delete = 100
		self.height_label_delete = 30

		# [./delete_sepcified_type_file.py] combo_type
		self.x_combo_type = self.x_label_delete + 100
		self.y_combo_type = self.y_label_delete - 17
		self.weight_combo_type = 200
		self.height_combo_type = 60
