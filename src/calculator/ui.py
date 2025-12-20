from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from .logic import evaluate, InvalidExpressionError

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400) # x, y, width, height

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Display widget
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFixedHeight(50)
        self.main_layout.addWidget(self.display)
        self.display.setStyleSheet("font-size: 24px;") # Make text larger

        self.current_expression = ""
        self.display.setText("0")

        # Buttons layout
        self.buttons_layout = QGridLayout()
        self.main_layout.addLayout(self.buttons_layout)

        self.buttons = {
            "7": (0, 0), "8": (0, 1), "9": (0, 2), "/": (0, 3),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "*": (1, 3),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), "-": (2, 3),
            "0": (3, 0), ".": (3, 1), "=": (3, 2), "+": (3, 3),
            "C": (4, 0, 1, 4) # C button spans 1 row, 4 columns
        }

        for btn_text, pos in self.buttons.items():
            button = QPushButton(btn_text)
            button.setFixedSize(60, 60) # Set a fixed size for buttons
            button.setStyleSheet("font-size: 18px;")
            if len(pos) == 4:
                self.buttons_layout.addWidget(button, pos[0], pos[1], pos[2], pos[3])
            else:
                self.buttons_layout.addWidget(button, pos[0], pos[1])
            button.clicked.connect(lambda _, text=btn_text: self._button_clicked(text))

    def _button_clicked(self, text):
        if text == "C":
            self.current_expression = ""
            self.display.setText("0")
        elif text == "=":
            try:
                result = evaluate(self.current_expression)
                self.display.setText(str(result))
                self.current_expression = str(result) # Carry over result for further operations
            except (InvalidExpressionError, ZeroDivisionError) as e:
                self.display.setText(f"Error: {e}")
                self.current_expression = "" # Clear expression on error
            except Exception:
                self.display.setText("Error")
                self.current_expression = ""
        else:
            if self.display.text() == "0" and text not in ["+", "-", "*", "/", "."]:
                self.current_expression = text
            else:
                self.current_expression += text
            self.display.setText(self.current_expression)



