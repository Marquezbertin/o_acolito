import random
import sys
from PIL import Image
import matplotlib.pyplot as plt

# Definição das Habilidades
class Habilidade:
    def __init__(self, nome, dano, custo):
        self.nome = nome
        self.dano = dano
        self.custo = custo

class Habilidades:
    def __init__(self):
        self.lista_habilidades = [
            Habilidade("Relâmpago da Força", 20, 15),
            Habilidade("Estrangulamento da Força", 25, 20)
        ]
    
    def mostrar_habilidades(self):
        print("Habilidades disponíveis:")
        for i, habilidade in enumerate(self.lista_habilidades):
            print(f"{i + 1}. {habilidade.nome} (Dano: {habilidade.dano}, Custo: {habilidade.custo} de poder da Força)")

# Definição do Jogador (Acolito)
class Acolito:
    def __init__(self, nome):
        self.nome = nome
        self.saude = 100
        self.poder_da_forca = 50
        self.habilidades = Habilidades()
    
    def atacar(self, inimigo):
        dano = random.randint(5, 15)
        print(f"{self.nome} ataca {inimigo.nome} e causa {dano} de dano.")
        inimigo.saude -= dano
    
    def usar_habilidade(self, inimigo):
        self.habilidades.mostrar_habilidades()
        escolha = int(input("Escolha uma habilidade: ").strip())
        habilidade = self.habilidades.lista_habilidades[escolha - 1]
        
        if self.poder_da_forca >= habilidade.custo:
            print(f"{self.nome} usa {habilidade.nome} e causa {habilidade.dano} de dano.")
            inimigo.saude -= habilidade.dano
            self.poder_da_forca -= habilidade.custo
        else:
            print("Poder da Força insuficiente.")
    
    def curar(self):
        quantidade_de_cura = random.randint(10, 20)
        self.saude += quantidade_de_cura
        print(f"{self.nome} se cura em {quantidade_de_cura}. Saúde atual: {self.saude}")
        self.poder_da_forca -= 5
        print(f"Poder da Força atual: {self.poder_da_forca}")

# Definição dos Inimigos
class Inimigo:
    def __init__(self, nome, saude, poder_de_ataque):
        self.nome = nome
        self.saude = saude
        self.poder_de_ataque = poder_de_ataque
    
    def atacar(self, jogador):
        dano = random.randint(5, self.poder_de_ataque)
        print(f"{self.nome} ataca {jogador.nome} e causa {dano} de dano.")
        jogador.saude -= dano

# Definição do Jogo
class Jogo:
    def __init__(self, jogador):
        self.jogador = jogador
        self.inimigos = [Inimigo("Aprendiz Sith", 50, 10), Inimigo("Jedi Sombrio", 70, 15)]
    
    def iniciar(self):
        introducao()
        apresentar_personagens()
        while self.jogador.saude > 0 and self.inimigos:
            self.encontrar_inimigo()
        
        if self.jogador.saude > 0:
            print("Você triunfou sobre todos os inimigos. Seu treinamento está completo.")
        else:
            print("Você foi derrotado. O lado sombrio te consome.")
    
    def encontrar_inimigo(self):
        cenario_1(self.jogador)
        if not self.inimigos:
            return
        
        inimigo = self.inimigos.pop(0)
        print(f"Você encontra um {inimigo.nome}. Prepare-se para a batalha!")
        
        while self.jogador.saude > 0 and inimigo.saude > 0:
            acao = input("Escolha uma ação: [atacar, curar, habilidade] ").strip().lower()
            if acao == "atacar":
                self.jogador.atacar(inimigo)
            elif acao == "curar":
                self.jogador.curar()
            elif acao == "habilidade":
                self.jogador.usar_habilidade(inimigo)
            else:
                print("Ação inválida.")
                continue
            
            if inimigo.saude > 0:
                inimigo.atacar(self.jogador)
        
        if self.jogador.saude > 0:
            print(f"Você derrotou o {inimigo.nome}!")
        else:
            print(f"Você foi derrotado pelo {inimigo.nome}.")

# Funções de Narração e Interação
def introducao():
    print("""
    Bem-vindo à saga O Acólito. 
    Você é um aprendiz do Lado Sombrio da Força, buscando poder e conhecimento.
    Sua jornada será perigosa e cheia de desafios.
    Faça suas escolhas com sabedoria.
    """)

def mostrar_imagem(path):
    try:
        img = Image.open(path)
        plt.imshow(img)
        plt.axis('off')  # Desativa os eixos para uma melhor visualização
        plt.show()
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

def apresentar_personagens():
    print("Apresentando os personagens principais:")
    
    print("Acolito")
    mostrar_imagem('imagens/acolito.jpeg')  # Substitua pelo caminho correto da imagem do Acolito
    
    print("Aprendiz Sith")
    mostrar_imagem('imagens/sith.jpeg')  # Substitua pelo caminho correto da imagem do Aprendiz Sith
    
    print("Jedi Sombrio")
    mostrar_imagem('imagens/sombrio.jpeg')  # Substitua pelo caminho correto da imagem do Jedi Sombrio

def cenario_1(jogador):
    print("""
    Você chega a uma antiga ruína Sith, onde sente uma presença sombria.
    Escolha o que fazer:
    1. Explorar a ruína
    2. Procurar por inimigos
    3. Meditar para aumentar seu poder
    """)
    escolha = input("Digite o número da sua escolha: ").strip()
    if escolha == "1":
        explorar_ruina(jogador)
    elif escolha == "2":
        procurar_inimigos()
    elif escolha == "3":
        meditar(jogador)
    else:
        print("Escolha inválida.")
        cenario_1(jogador)

def explorar_ruina(jogador):
    print("""
    Você encontra antigos textos Sith que aumentam seu conhecimento da Força.
    Seu poder aumentou!
    """)
    jogador.poder_da_forca += 10

def procurar_inimigos():
    print("""
    Você encontra um grupo de saqueadores que tentam te atacar.
    Prepare-se para lutar!
    """)

def meditar(jogador):
    print("""
    Você medita e sente a Força fluindo através de você.
    Sua saúde e poder aumentaram.
    """)
    jogador.saude += 20
    jogador.poder_da_forca += 15

# Execução do Jogo
if __name__ == "__main__":
    nome = input("Digite o nome do seu acólito: ")
    jogador = Acolito(nome)
    jogo = Jogo(jogador)
    jogo.iniciar()
