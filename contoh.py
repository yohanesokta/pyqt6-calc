import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QVBoxLayout,QTextEdit
from utils.function_button import ButtonOperation,MathExecs

# Controller dari MathExecs untuk menyimpan sebuah nilai dari 1 - 9 dan operator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        textField = QTextEdit()

        numbers_controllers = MathExecs(textField)
        button0 = ButtonOperation(0,numbers_controllers.push_number)
        button1 = ButtonOperation(1,numbers_controllers.push_number)
        button2 = ButtonOperation(2,numbers_controllers.push_number)
        button3 = ButtonOperation(3,numbers_controllers.push_number)

        buttonTambah = ButtonOperation("+",numbers_controllers.push_operator)
        buttonKali = ButtonOperation("*",numbers_controllers.push_operator)
        buttonBagi = ButtonOperation("/",numbers_controllers.push_operator)
        buttonKurang = ButtonOperation("-",numbers_controllers.push_operator)
        buttonSamaDengan = ButtonOperation("=",numbers_controllers.push_operator)

        Hbox0 = QHBoxLayout()
        Hbox0.addWidget(textField)

        Hbox1 = QHBoxLayout()
        Hbox1.addWidget(button0)
        Hbox1.addWidget(button1)
        Hbox1.addWidget(button2)
        Hbox1.addWidget(button3)

        Hbox2 = QHBoxLayout()
        Hbox2.addWidget(buttonKali)
        Hbox2.addWidget(buttonBagi)
        Hbox2.addWidget(buttonTambah)
        Hbox2.addWidget(buttonKurang)
        Hbox2.addWidget(buttonSamaDengan)


        box = QVBoxLayout()
        box.addLayout(Hbox0)
        box.addLayout(Hbox1)
        box.addLayout(Hbox2)

        widget = QWidget()
        widget.setLayout(box)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()

# Belajar - belajar Nebak Tengah layar mu hehe.

panjang = 1920
lebar = 1080

window.setGeometry(panjang/2-150,lebar/2-200,300,400)
window.show()

app.exec()
