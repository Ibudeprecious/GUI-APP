from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtWidgets import QPushButton, QLabel, QComboBox
from bs4 import BeautifulSoup
import requests


def convert(amount, from_, to_):
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
    from_cur = from_currency.currentText()
    to_cur = to_currency.currentText()
    price = convert(input, from_cur, to_cur)
    Output.setText(f'{input}{from_cur} is {price}{to_cur}')

bizapp = QApplication([])
window = QWidget()
window.setWindowTitle ('Currency Converter')

layout = QVBoxLayout()

textbox = QLineEdit()
layout.addWidget(textbox)

from_currency = QComboBox()
currencies = ['USD', 'EUR', 'GBP', 'JPY']
from_currency.addItems(currencies)
layout.addWidget(from_currency)

to_currency = QComboBox()
to_currency.addItems(currencies)
layout.addWidget(to_currency)

button = QPushButton('Convert')
layout.addWidget(button)
button.clicked.connect(curency)

Output = QLabel('')
layout.addWidget(Output)

window.setLayout(layout)
window.show()
bizapp.exec()