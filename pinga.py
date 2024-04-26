import pygame
import random

def coresaleatorias():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (random.randint(0,255),random.randint(0,255),random.randint(0,255))
# cria uma bola 
def novabola():

#iniciar o pygame (motor)
pygame.init()

# configuraçao da tela
tamanho = (300,600)

# cria a tela e define o tamanho
tela = pygame.display.set_mode(tamanho)

# define o titulo da tela 
pygame.display.set_caption("pinga")

#criar um relogio para controlar o FPS
relogio = pygame.time.Clock()

#criar um circulo para mostrar na tela
cor = (100,0,0)
posicao = [150,60]
raio = 50
sobeoudesce = 1
esquerdadireita = 1
velocidade = 0 
cor_tela = (255,255,255)
listabola = []
novabola



while True:
    # pega os eventos que estao acontecendo
    for evento in pygame.event.get():
        print(evento)

        # se o evento for de fechar atela
        if evento.type == pygame.QUIT:
            pygame.quit() #fecha o pygame
            exit() #fecha o programa

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.k_UP:
                velocidade =+ 1
            elif evento.key == pygame. k_DOW:
                velocidade -= 1
    
        

    #pinta a tela de branco
    tela.fill(cor_tela)

    #cria um circulo para mostrar na tela
    circulo = pygame.draw.circle(tela, cor, posicao, raio)

    posicao[1] += velocidade * sobeoudesce
    posicao[0] += velocidade* esquerdadireita
    
    #verificar se o circulo bateu na parede
    if posicao[1] >= 550:
        sobeoudesce = -1
        cor,cor_tela = coresaleatorias()
    elif posicao[1] < 50:
        sobeoudesce = 1 
        cor,cor_tela = coresaleatorias()

    if posicao[0] >= 250:
        esquerdaoudireita = -1
        cor,cor_tela = coresaleatorias()
    elif posicao[0] <= 50:
        esquerdadireita = 1
        cor,cor_tela = coresaleatorias 

    
        
    # movimenta o circulo para baixo
    
    posicao[1] += 5
    

    #atualiza a tela para exibir o que foi desenhado
    pygame.display.update()

    relogio.tick(45)