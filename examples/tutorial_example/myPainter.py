import random

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPainterPath
from PyQt6.QtCore import Qt


class DrawUnicode(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.text = "Лев Николаевич Толстой\nАнна Каренина"

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Drawing Unicode')
		self.show()

	def paintEvent(self, event):
		"""当窗口发生改变时，触发事件"""
		print(event)
		qp = QPainter()
		qp.begin(self)
		self.drawText(event, qp)
		qp.end()

	def drawText(self, event, qp):
		qp.setPen(QColor(168, 34, 3))
		qp.setFont(QFont('Decorative', 10))
		qp.drawText(event.rect(), Qt.AlignmentFlag.AlignCenter, self.text)


class DrawPoint(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setMinimumSize(50, 50)
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Points')
		self.show()

	def paintEvent(self, a0):
		print('Paint Event')
		qp = QPainter()
		qp.begin(self)
		self.drawPoints(qp)
		qp.end()

	def drawPoints(self, qp):
		qp.setPen(Qt.GlobalColor.red)
		size = self.size()

		for i in range(1000):
			x = random.randint(1, size.width() - 1)
			y = random.randint(1, size.height() - 1)
			qp.drawPoint(x, y)


class DrawColor(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 350, 100)
		self.setWindowTitle('Colors')
		self.show()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self, qp):
		col = QColor(0, 0, 0)
		col.setNamedColor('#d4d4d4')
		qp.setPen(col)  # 在drawRect时会用这个颜色来绘制边框

		qp.setBrush(QColor(200, 0, 0))
		qp.drawRect(10, 15, 90, 60)

		qp.setBrush(QColor(250, 80, 0, 160))
		qp.drawRect(130, 15, 90, 60)

		qp.setBrush(QColor(25, 0, 90, 200))
		qp.drawRect(250, 15, 90, 60)


class DrawPen(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 280, 270)
		self.setWindowTitle('Pen Styles')
		self.show()

	def paintEvent(self, a0):
		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
		qp.setPen(pen)
		qp.drawLine(20, 40, 250, 40)  # 起点坐标XY 终点坐标XY

		pen.setStyle(Qt.PenStyle.DashLine)
		qp.setPen(pen)
		qp.drawLine(20, 80, 250, 80)

		pen.setStyle(Qt.PenStyle.DashDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 120, 250, 120)

		pen.setStyle(Qt.PenStyle.DotLine)
		qp.setPen(pen)
		qp.drawLine(20, 160, 250, 160)

		pen.setStyle(Qt.PenStyle.DashDotDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 200, 250, 200)

		pen.setStyle(Qt.PenStyle.CustomDashLine)
		pen.setDashPattern([1, 4, 5, 4])  # 1px短横线，4px空格，5px长横线，4px空格...
		qp.setPen(pen)
		qp.drawLine(20, 240, 250, 240)


class DrawBrush(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 355, 280)
		self.setWindowTitle('Draw Brush')
		self.show()

	def paintEvent(self, a0):
		qp = QPainter()
		qp.begin(self)
		self.drawBrushes(qp)
		qp.end()

	def drawBrushes(self, qp):
		brush = QBrush(Qt.BrushStyle.SolidPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 15, 90, 60)

		brush.setStyle(Qt.BrushStyle.Dense1Pattern)
		qp.setBrush(brush)
		qp.drawRect(130, 15, 90, 60)

		brush.setStyle(Qt.BrushStyle.Dense2Pattern)
		qp.setBrush(brush)
		qp.drawRect(250, 15, 90, 60)

		brush.setStyle(Qt.BrushStyle.DiagCrossPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 105, 90, 60)

		brush.setStyle(Qt.BrushStyle.Dense5Pattern)
		qp.setBrush(brush)
		qp.drawRect(130, 105, 90, 60)

		brush.setStyle(Qt.BrushStyle.Dense6Pattern)
		qp.setBrush(brush)
		qp.drawRect(250, 105, 90, 60)

		brush.setStyle(Qt.BrushStyle.HorPattern)
		qp.setBrush(brush)
		qp.drawRect(10, 195, 90, 60)

		brush.setStyle(Qt.BrushStyle.VerPattern)
		qp.setBrush(brush)
		qp.drawRect(130, 195, 90, 60)

		brush.setStyle(Qt.BrushStyle.BDiagPattern)
		qp.setBrush(brush)
		qp.drawRect(250, 195, 90, 60)


class BezierCurve(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 380, 250)
		self.setWindowTitle('Bezier Curve')
		self.show()

	def paintEvent(self, a0):
		qp = QPainter()
		qp.begin(self)
		qp.setRenderHint(QPainter.RenderHint.Antialiasing)  # setRenderHint用于设置渲染提示，此处启用抗锯齿
		self.drawBezierCurve(qp)
		qp.end()

	def drawBezierCurve(self, qp):
		path = QPainterPath()
		path.moveTo(30, 30)  # 路径起始点
		path.cubicTo(30, 30, 200, 350, 350, 30)  # cubicTo接受四个点作为参数。起始点(30,30)，第一个控制点(30,30)，第二个控制点(200,350)，结束点(350,30)

		qp.drawPath(path)
