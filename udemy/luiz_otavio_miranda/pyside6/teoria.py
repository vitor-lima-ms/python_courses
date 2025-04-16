# QWidget --> Widget genérico
# QLayout --> Um widget de layout que recebe outros widgets

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow

app = QApplication()

mainWindow = QMainWindow()
mainWindow.setWindowTitle('Minha janela')
# Status bar
statusBar = mainWindow.statusBar()
statusBar.showMessage('Mensagem da status bar')
# Menu bar
menuBar = mainWindow.menuBar()
firstMenu = menuBar.addMenu('Primeiro menu')
firstMenu.addAction('Primeira ação')

def slotExample():
    print('Exemplo de slot')
firstMenu.triggered.connect(slotExample) # Triggeered --> Signal; Função --> Slot


centralWidget = QWidget() # Widget genérico que serve como local para adição de novos widgets, mas precisa de um layout
mainWindow.setCentralWidget(centralWidget)

layout = QGridLayout() # Layout vertical. O layout é responsável por receber outros widgets

button = QPushButton('Texto do botão')
# button.setStyleSheet('font-size: 40px') # Praticamente um CSS
# button.show() # Adiciona o widget na hierarquia e exibe a janela

otherButton = QPushButton('Texto do outro botão')

thirdButton = QPushButton('Texto do terceiro botão')

layout.addWidget(button, 1, 1) # Linha, coluna
layout.addWidget(otherButton, 2, 2)
layout.addWidget(thirdButton, 3, 1, 1, 2) # Linha, coluna, rowspan, colspan
centralWidget.setLayout(layout)

mainWindow.show()
app.exec() # Executa o loop da aplicação