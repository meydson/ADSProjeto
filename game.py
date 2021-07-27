import pygame, sys
from pygame.locals import *

#Tamanho da tela de jogo
largura = 900
altura = 506

class naveInimigo(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        pygame.sprite.Sprite.__init__(self)
        #Definindo as imagens dos inimigos
        self.ImagemInimigo = pygame.image.load('imagens/inimigo.png')
        self.ImagemInimigo2 = pygame.image.load('imagens/inimigo1.png')

        #Lista das imagens dos inimigos
        #self.listaImagens = [self.ImagemInimigo, self.ImagemInimigo2]
        #self.posImagem = 0
        #self.imagemInimigo = self.listaImagens[self.posImagem]

        self.rect = self.ImagemInimigo.get_rect()

        self.listaDisparo = []
        self.velocidade = 20
        self.rect.top = p_y
        self.rect.left = p_x

        #Configurando o tempo para surgimento dos inimigos
        self.configTempo = 1

    def comportamento(self, tempo):
        if self.configTempo == tempo:
            self.posImagem += 1
            self.configTempo += 1
            print(tempo,self.configTempo)
            if self.posImagem > len(self.listaImagens) - 1 :
                self.posImagem = 0

    def colocar(self, superficie):
        #self.imagemInimigo = self.listaImagens[self.posImagem ]
        superficie.blit(self.ImagemInimigo, self.rect)

    def colocar2(self, superficie):
        superficie.blit(self.ImagemInimigo2, self.rect)

#criação das classes dos objetos do jogo
class tiro(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemTiro = pygame.image.load('imagens/tiro2.png')

        self.rect = self.ImagemTiro.get_rect()
        self.velocidadeTiro = 5
        self.rect.top = p_y
        self.rect.left = p_x

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeTiro

    def colocar(self, superficie):
        superficie.blit(self.ImagemTiro, self.rect)

class nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load('imagens/navejogador.png')

        #definindo a área  de colisão da imagem e seu posicionamento na tela
        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 70

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()

    def movimentoEsquerda(self):
        self.rect.left  -= self.velocidade
        self.__movimento()

    # função privada para delimitar as bordas da tela
    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 900:
                self.rect.right = 900

    #Função de disparo
    def disparar(self, x,  y):
        meuTiro = tiro(x, y)
        self.listaDisparo.append(meuTiro)

    def colocar(self, superficie):
        superficie.blit(self.ImagemNave, self.rect)

def jogo_nave():
    pygame.init()
    #definindo o tamanho da tela do jogo e o título
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo Meydson")

    #variáveis com as imagens do jogo
    jogador = nave()
    fundo = pygame.image.load('imagens/fundo.png')
    jogando = True

    #inimigo = naveInimigo(20,200)


    tiroNave = tiro(largura/2,altura - 70)

    #velocidade de execução - FPS
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(60)
        inimigoX = 20
        inimigoY = 200
        distancia = 200
        distanciay = 100

        inimigo = naveInimigo(inimigoX, inimigoY)
        inimigo1 = naveInimigo(inimigoX + distancia, inimigoY)
        inimigo2 = naveInimigo(inimigoX + distancia * 2, inimigoY)
        inimigo3 = naveInimigo(inimigoX + distancia * 3, inimigoY)
        inimigo4 = naveInimigo(inimigoX + distancia * 4, inimigoY)
        inimigo5 = naveInimigo(inimigoX + distanciay, inimigoY - (distancia-100))
        inimigo6 = naveInimigo(inimigoX + distanciay * 3, inimigoY - (distancia - 100))
        inimigo7 = naveInimigo(inimigoX + distanciay * 5, inimigoY - (distancia - 100))
        inimigo8 = naveInimigo(inimigoX + distanciay * 7, inimigoY - (distancia - 100))
        tempo = int(pygame.time.get_ticks()/1000)
        tiroNave.trajetoria()
        #estrutura de repetição para captar os eventos do jogo
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jogador.movimentoEsquerda()
                elif evento.key == K_RIGHT:
                    jogador.movimentoDireita()
                elif evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparar(x,y)

        #colocando os elementos do jogo da tela
        tela.blit(fundo,(0,0))
        jogador.colocar(tela)
        inimigo.colocar(tela)
        inimigo1.colocar2(tela)
        inimigo2.colocar(tela)
        inimigo3.colocar2(tela)
        inimigo4.colocar(tela)
        inimigo5.colocar2(tela)
        inimigo6.colocar(tela)
        inimigo7.colocar2(tela)
        inimigo8.colocar(tela)
        #inimigo.comportamento(tempo)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < -10:
                    jogador.listaDisparo.remove(x)

        #atualizando a tela
        pygame.display.update()

jogo_nave()