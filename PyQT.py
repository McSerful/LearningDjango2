from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from functools import partial

__version__ = '0.1'
__author__ = 'Iankovetc Sergei'



class PyCalcUi(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set some main windows' properties
        self.setWindowTitle('Calculator')
        self.setFixedSize(250, 250)

        # Set the central widget
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget()
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()

        self.display.setFixedHeight(40)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)

        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {
            'C': (0,0),
            '+/-': (0,1),
            '%': (0,2),
            '/': (0,3),
            '7': (1,0),
            '8': (1,1),
            '9': (1,2),
            'X': (1,3),
            '4': (2,0),
            '5': (2,1),
            '6': (2,2),
            '-': (2,3),
            '1': (3,0),
            '2': (3,1),
            '3': (3,2),
            '+': (3,3),
            '0': (4,0,1,2),
            '.': (4,2),
            '=': (4,3)
        }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(50, 35)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')


class PyCalcCtrl:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def buildExpression(self, sub_exp):
        expression = self.view.displayText() + sub_exp
        self.view.setDisplayText(expression)

    def connectSignals(self):
        for btnText, btn in self.view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self.buildExpression, btnText))

            self.view.buttons['C'].clicked.connect(self.view.clearDisplay)


def main():
    pycalc = QApplication(sys.argv)

    view = PyCalcUi()
    view.show()

    PyCalcCtrl(view=view)

    sys.exit(pycalc.exec())

if __name__ == '__main__':
    main()