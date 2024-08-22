import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
import networkx as nx
import matplotlib.pyplot as plt

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def combinacao(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

def criar_grafo_comb(n, k):
    G = nx.DiGraph()
    for i in range(n + 1):
        G.add_node(i)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j - i <= k:
                G.add_edge(i, j)
    return G

def desenhar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=14, font_weight='bold')
    plt.show()

class CombCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculadora de Combinações Simples.')
        self.setGeometry(100, 100, 400, 200)


        fonte = QFont('Arial', 14)


        layout_principal = QVBoxLayout()

        layout_n = QHBoxLayout()
        self.label_n = QLabel('Digite o valor de n:')
        self.label_n.setFont(fonte)
        self.entry_n = QLineEdit()
        self.entry_n.setFont(fonte)
        layout_n.addWidget(self.label_n)
        layout_n.addWidget(self.entry_n)

        layout_k = QHBoxLayout()
        self.label_k = QLabel('Digite o valor de k:')
        self.label_k.setFont(fonte)
        self.entry_k = QLineEdit()
        self.entry_k.setFont(fonte)
        layout_k.addWidget(self.label_k)
        layout_k.addWidget(self.entry_k)

        self.botao_calcular = QPushButton('Calcular')
        self.botao_calcular.setFont(fonte)
        self.botao_calcular.clicked.connect(self.calcular_comb)

        self.botao_grafo = QPushButton('Mostrar Grafo')
        self.botao_grafo.setFont(fonte)
        self.botao_grafo.clicked.connect(self.mostrar_grafo)

        self.label_resultado = QLabel('Resultado:')
        self.label_resultado.setFont(fonte)

        # Adicionar layouts ao layout principal
        layout_principal.addLayout(layout_n)
        layout_principal.addLayout(layout_k)
        layout_principal.addWidget(self.botao_calcular)
        layout_principal.addWidget(self.botao_grafo)
        layout_principal.addWidget(self.label_resultado)

        self.setLayout(layout_principal)

    def calcular_comb(self):
        try:
            n = int(self.entry_n.text())
            k = int(self.entry_k.text())
            if n < 0 or k < 0:
                raise ValueError('Os valores de n e k devem ser não negativos.')
            if k > n:
                raise ValueError('k não pode ser maior que n.')
            resultado = combinacao(n, k)
            self.label_resultado.setText(f'Resultado: {resultado}')
        except ValueError as ve:
            self.mostrar_erro(str(ve))

    def mostrar_grafo(self):
        try:
            n = int(self.entry_n.text())
            k = int(self.entry_k.text())
            G = criar_grafo_comb(n, k)
            desenhar_grafo(G)
        except ValueError as ve:
            self.mostrar_erro(str(ve))

    def mostrar_erro(self, mensagem):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erro")
        msg.setInformativeText(mensagem)
        msg.setWindowTitle("Erro")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CombCalculator()
    ex.show()
    sys.exit(app.exec_())
