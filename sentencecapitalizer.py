from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtWidgets import QPushButton, QLabel

def sentence_maker():
    input = textbox.text()
    cap = input.capitalize()
    Output.setText(cap + '. Dont Mention 😂')

bizapp = QApplication([])
window = QWidget()
window.setWindowTitle ('Sentence Maker')

layout = QVBoxLayout()

textbox = QLineEdit()
layout.addWidget(textbox)

button = QPushButton('Correct the Text')
layout.addWidget(button)
button.clicked.connect(sentence_maker)

Output = QLabel('')
layout.addWidget(Output)

window.setLayout(layout)
window.show()
bizapp.exec()