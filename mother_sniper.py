import pygame 
import random

def novoobjeto():

    tipo = random.choice(["chave","machado","pedra"])
    tamanho = random.randint(1, 5) 
    vidas = random.randint(1, 10) 
    return {
        "posicao": [random.randint(200, 600), random.randint(200, 400)],
        "tipo": tipo,
        "tamanho": tamanho,
        "vidas": vidas,
        "direcao": pygame.Vector2(1, 1)
    }
pygame.init()

tamanho = (600,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("mother sniper")
relogio = pygame.time.Clock()

cor = (255, 0, 0)
posicao = [150, 60]
raio = 50
cor_tela = (255, 255, 255)

list_objeto = []

while True:
    for evento in pygame.event.get():
        if evento.type == novoobjeto:
            list_objeto.append(novoobjeto)

        if evento.type == pygame.QUIT:
            pygame.quit() 
            exit() 

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                novoobjeto(evento.pos, list_objeto)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogoAcabou = False
                list_objeto = []
                list_objeto.append(novoobjeto())
                pontuacao = 0



    listaplanofundo = []
    
    for index in range (1, 5):
        imagem = pygame.image.load(f"assets2/fundo2/png/{index}.png")
        imagem = pygame.transform.scale(imagem,tamanho).convert_alpha()
        listaplanofundo.append(imagem)

    listaimagesmachado =[]
    listaimageschave = []
    listaimagenspedra = []

    for index in range(1,41):
        imagem = pygame.image.load("f"assets2/icones/09{index}.png"")
        imagem = pygame.transform.scale(imagem,(30,30)).convert_alpha()
        listaimagesmachado.append(imagem)

    for index in range(1,41):
        imagem = pygame.image.load(f"assets/icons/34{index}.png")
        imagem = pygame.transform.scale(imagem,(30,30)).convert_alpha()
        listaimageschave.append(imagem)

    for index in range(1,41):
        imagem = pygame.image.load(f"assets/icons/14{index}.png")
        imagem = pygame.transform.scale(imagem,(30,30)).convert_alpha()
        listaimagenspedra.append(imagem)


    tela.blit(listaplanofundo[0],(0,0))
    tela.blit(listaplanofundo[1],(0,0))
    tela.blit(listaplanofundo[2],(0,0))
    tela.blit(listaplanofundo[3],(0,0))
    tela.blit(listaplanofundo[4],(0,0))
    tela.blit(listaplanofundo[5],(0,0))
   
   
    for objeto in list_objeto:
            
            circulo = pygame.draw.circle(
                tela, 
                (255,255,255),
                objeto["posicao"],
                objeto["tamanho"]
            )

            listaimagens =[]
            if objeto["tipo"] =="machado " :listaimagens =  listaimagesmachado
            elif objeto["tipo"] =="chave" :listaimagens =  listaimageschave
            elif objeto["tipo"] =="pedra " :listaimagens =  listaimagenspedra
            
   
    

    tela.fill(cor_tela)

    pygame.display.update()


