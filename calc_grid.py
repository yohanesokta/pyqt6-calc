import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, \
    QLayoutItem

from utils.function_button import MathExecs, ButtonOperation


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator vGird")

        input_text = QTextEdit()
        controllers = MathExecs(input_text)
        input_text.setFontPointSize(14)
        gird = QGridLayout()
        gird.addWidget(input_text,0,0,3,0)
        gird.addWidget(ButtonOperation(9,controllers.push_number),1,0)
        gird.addWidget(ButtonOperation("AC",controllers.clearState),1,1)
        gird.addWidget(ButtonOperation("*",controllers.push_operator),1,2)

        gird.addWidget(ButtonOperation(5,controllers.push_number),2,0)
        gird.addWidget(ButtonOperation(6,controllers.push_number),2,1)
        gird.addWidget(ButtonOperation("/",controllers.push_operator),2,2)

        gird.addWidget(ButtonOperation(1,controllers.push_number),3,0)
        gird.addWidget(ButtonOperation(3,controllers.push_number),3,1)
        gird.addWidget(ButtonOperation("-",controllers.push_operator),3,2)

        gird.addWidget(ButtonOperation(0,controllers.push_number),4,0)
        gird.addWidget(ButtonOperation("=",controllers.push_operator),4,1)
        gird.addWidget(ButtonOperation("+",controllers.push_operator),4,2)

        gird.setVerticalSpacing(5)
        gird.setHorizontalSpacing(5)

        widget = QWidget()
        widget.setLayout(gird)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()