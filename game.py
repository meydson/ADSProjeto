import pygame, sys
from pygame.locals import *

#Tamanho da tela de jogo
largura = 900
altura = 506

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

    tiroNave = tiro(largura/2,altura - 70)

    #velocidade de execução - FPS
    relogio = pygame.time.Clock()

    while True:
        relogio.tick(60)
        #jogador.movimento()
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
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < -10:
                    jogador.listaDisparo.remove(x)

        #atualizando a tela
        pygame.display.update()

jogo_nave()