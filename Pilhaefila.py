from collections import deque

# Classe para o navegador com pilhas de avanço e retrocesso
class Navegador:
    def __init__(self):
        self.pilhaVoltar = []
        self.pilhaAvancar = []
        self.paginaAtual = None

    def acessarPagina(self, url):
        if self.paginaAtual:
            self.pilhaVoltar.append(self.paginaAtual)
        self.paginaAtual = url
        self.pilhaAvancar.clear()
        print(f"Acessando: {self.paginaAtual}")

    def voltar(self):
        if self.pilhaVoltar:
            self.pilhaAvancar.append(self.paginaAtual)
            self.paginaAtual = self.pilhaVoltar.pop()
            print(f"Voltando para: {self.paginaAtual}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if self.pilhaAvancar:
            self.pilhaVoltar.append(self.paginaAtual)
            self.paginaAtual = self.pilhaAvancar.pop()
            print(f"Avançando para: {self.paginaAtual}")
        else:
            print("Não há páginas para avançar.")

# Classe para controle de senhas no hospital
class SistemaSenhas:
    def __init__(self):
        self.fila_senhas = deque()
        self.proximaSenha = 1

    def gerarSenha(self):
        self.fila_senhas.append(self.proximaSenha)
        print(f"Senha gerada: {self.proximaSenha}")
        self.proximaSenha += 1

    def chamarProximo(self):
        if self.fila_senhas:
            senha_chamada = self.fila_senhas.popleft()
            print(f"Chamando senha: {senha_chamada}")
        else:
            print("Nenhuma senha na fila.")

if __name__ == "__main__":
    # Testando o navegador
    navegador = Navegador()
    navegador.acessarPagina("google.com")
    navegador.acessarPagina("mozilla.org")
    navegador.voltar()
    navegador.avancar()

    # Testando o sistema de senhas
    sistema = SistemaSenhas()
    sistema.gerarSenha()
    sistema.gerarSenha()
    sistema.chamarProximo()
    sistema.chamarProximo()
