from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

def opener():
    global filenames, files
    filenames, _ = QFileDialog.getOpenFileNames (window)
    files = '\n'.join(filenames)
    message.setText(f'The following selected files will be deleted:\n\n{files}\n\nClick on "Destroy File" to proceed ')

def destroyer():
    for file in filenames:
        path = Path(file)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText (f'Successfully Destroyed')
app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')

layout = QVBoxLayout() #the main layout

description = QLabel('Use with Caution ⚠. Any file you upload here will be <font color="red">overwritten and permanently</font> destroyed')
layout.addWidget(description, alignment=Qt.AlignmentFlag.AlignCenter)

open_btn = QPushButton('Open File')
open_btn.setToolTip('Click to select the File you want to delete')
open_btn.setFixedWidth(300)
open_btn.clicked.connect(opener)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)

destroy_btn = QPushButton('Destroy File')
destroy_btn.setToolTip('Click to destroy the selected files')
destroy_btn.setFixedWidth(300)
destroy_btn.clicked.connect(destroyer)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)

message = QLabel('')
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)


window.setLayout(layout)
window.show()
app.exec()