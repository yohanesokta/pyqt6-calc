from PyQt6.QtWidgets import  QPushButton


#  ** How to use **
#  Ini biar ada tutorial bang jangan di sangka AI hehe ..
#  Controller nanti di buat dari class MathExecs
#  Bisa gunakan ButtonOperation Langsung dengan controllernya saling terhubung
#  Nanti kalau mau lihat hasil text print saja controller dari MathExecs


class ButtonOperation(QPushButton):
    def __init__(self,text,callback):
        super().__init__()
        self.setText(str(text))
        self.clicked.connect(lambda : callback(text))

#  ** How to use **
#  fungsi controler dari class MathExecs gunakan untuk push number dan eksekusi operator
#  psuh number dan push opertor di sini langsung mengeksekusi sesuai operasi matematika

class MathExecs:
    def __init__(self):
        self.listNumber:list = []
        self.operator = None
    def push_number(self, other):
        self.listNumber.append(other)
        print(self.__str__())
    def push_operator(self,operator):
        self.calculate()
        if (operator != "=" and str(self.listNumber[-1]) not in "-+/*"):
            self.listNumber.append(operator)
            self.operator = operator
        print(self.__str__())
    def calculate(self):
        if (self.operator != None and str(self.listNumber[-1]) not in "-+/*"):
            self.listNumber :list = str(eval(self.__str__())).split()
            self.operator = None
    def clearState(self):
        self.listNumber = []
        self.operator = None

    def __str__(self):
        return "".join([str(num) for num in self.listNumber])