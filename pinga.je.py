import pygame

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
posicao = [150,300]
raio = 50



while True:
    # pega os eventos que estao acontecendo
    for evento in pygame.event.get():
        print(evento)

        # se o evento for de fechar atela
        if evento.type == pygame.QUIT:
            pygame.quit() #fecha o pygame
            exit() #fecha o programa
    
        

    #pinta a tela de branco
    tela.fill((255,255,255))

    #cria um circulo para mostrar na tela
    circulo = pygame.draw.circle(tela, cor, posicao, raio)

   
  

    # movimenta o circulo para baixo
    
    posicao[1] += 5
    

    

    #se o circulo sair da tela
    if posicao[1] > 650:
        posicao[1] = -50
   
       
    #atualiza a tela para exibir o que foi desenhado
    pygame.display.update()

    relogio.tick(45)