from qtpy.Qtwidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

class JanelaContador(QWdget):

    def __innit__(self):
        super().__innit__()

        self.contador = 0 

        self.setWindowTitle("contador de cliques")
        self.resize(400, 250)

        self.texto = QLabel("cliques: 0")
        self.texto.setStyleSheet("font-size: 24px")

        self.QPushButton("clique aqui")
        self.botao.setStyleSheet("""
        font-size: 18px;
        padding: 15px;
        """)

        # quando botao for clicado, executar o metodo contar.
        self.botao.clicked.connect(self.contar)

        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.botao)

        self.setLayout(layout)

    def contar(self):
        self.contador += 1
        self.texto.setText(f"cliques: {self.contador}")


app = QApplication([])

janela = JanelaContador()
janela.show()

app.exec()



