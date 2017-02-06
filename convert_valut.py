from PyQt5.QtCore import QObject
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QDoubleSpinBox,
    QVBoxLayout
)


class Course(QObject):
    def get(self):
        return 58.86


class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.init_signals()
        self.initLayout()

    def init_signals(self):
        self.convertBtn.clicked.connect(self.on_click)
        self.clearBtn.clicked.connect(self.on_clear)
        self.srcAmount.valueChanged.connect(self.change_value)
        self.resultAmount.valueChanged.connect(self.change_value)

    def initUi(self):
        self.setWindowTitle('Конвертер валют RUB/USD 1.0')
        self.srcLabel = QLabel('Введите сумму в рублях (RUB)', self)
        self.resultLabel = QLabel('Или введите сумму в долларах (USD)', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999999)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.clearBtn = QPushButton('Сброс', self)
        self.convertBtn.setEnabled(False)

    def on_click(self):
        value = max(self.srcAmount.value(), self.resultAmount.value())
        if self.srcAmount.value() != 0:
            self.resultAmount.setValue(value/Course().get())
        else:
            self.srcAmount.setValue(value/Course().get())

    def on_clear(self):
        self.resultAmount.setValue(0)
        self.srcAmount.setValue(0)

    def change_value(self):
        if self.srcAmount.value() == 0 and self.resultAmount.value() != 0:
            self.convertBtn.setEnabled(True)
        elif self.srcAmount.value() > 0 and self.resultAmount.value() == 0:
            self.convertBtn.setEnabled(True)
        else:
            self.convertBtn.setEnabled(False)

    def initLayout(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)
        self.setCentralWidget(self.w)

    def press_event(self, key):
        if key.key() == Qt.Key_Enter: self.on_click()

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = Converter()
    converter.setWindowOpacity(0.95)  # Задали небольшую прозрачность главного экрана
    pal = converter.palette()
    pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                 QtGui.QColor("#98FF98"))  # задали background-color (Зеленая мята)
    converter.setPalette(pal)
    converter.resize(350, 150)
    converter.show()


    sys.exit(app.exec_())