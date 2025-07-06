from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtWidgets import QPushButton, QLabel
from bs4 import BeautifulSoup
import requests


def convert(amount, from_='USD', to_='EUR'):
    url = f'https://www.x-rates.com/calculator/?from={from_}&to={to_}&amount={amount}'
    source_code = requests.get(url).text
    soup_source_code = BeautifulSoup(source_code, 'html.parser')
    find = soup_source_code.find('span', class_='ccOutputRslt')
    text = find.text.split(' ')[0]
    text = round(float(text), 2)
    return text
    # text = f'{amount} {from_} is equal to {text} {to_}'
    # print(text)

def curency():
    input = float(textbox.text())
    price = convert(input)
    Output.setText(f'{input}USD is {price}EUR')

bizapp = QApplication([])
window = QWidget()
window.setWindowTitle ('Convert from USD to EUR')

layout = QVBoxLayout()

textbox = QLineEdit()
layout.addWidget(textbox)

button = QPushButton('Convert to EUR')
layout.addWidget(button)
button.clicked.connect(curency)

Output = QLabel('')
layout.addWidget(Output)

window.setLayout(layout)
window.show()
bizapp.exec()