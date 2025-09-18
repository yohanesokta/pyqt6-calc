import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QLayoutItem

from utils.function_button import MathExecs, ButtonOperation

font_size = 16
fixed_size = 60

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator vGird")

        input_text = QTextEdit()
        controllers = MathExecs(input_text)
        input_text.setFontPointSize(font_size)

        gird = QGridLayout()
        gird.addWidget(input_text,0,0,3,0)


        gird.addWidget(ButtonOperation(9,controllers.push_number,fixed_size,font_size),1,0)
        gird.addWidget(ButtonOperation("AC",controllers.clearState,fixed_size,font_size),1,1)
        gird.addWidget(ButtonOperation("*",controllers.push_operator,fixed_size,font_size),1,2)

        gird.addWidget(ButtonOperation(5,controllers.push_number,fixed_size,font_size),2,0)
        gird.addWidget(ButtonOperation(6,controllers.push_number,fixed_size,font_size),2,1)
        gird.addWidget(ButtonOperation("/",controllers.push_operator,fixed_size,font_size),2,2)

        gird.addWidget(ButtonOperation(1,controllers.push_number,fixed_size,font_size),3,0)
        gird.addWidget(ButtonOperation(3,controllers.push_number,fixed_size,font_size),3,1)
        gird.addWidget(ButtonOperation("-",controllers.push_operator,fixed_size,font_size),3,2)

        gird.addWidget(ButtonOperation(0,controllers.push_number,fixed_size,font_size),4,0)
        gird.addWidget(ButtonOperation("=",controllers.push_operator,fixed_size,font_size),4,1)
        gird.addWidget(ButtonOperation("+",controllers.push_operator,fixed_size,font_size),4,2)

        gird.setVerticalSpacing(5)
        gird.setHorizontalSpacing(5)

        widget = QWidget()
        widget.setLayout(gird)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()