import pygame
import random

def coresAleatorias():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Cria uma nova bola
def novaBola():
    # Cria um dicionário com as informações da bola
    cores = {
        1: (255, 0, 0),
        2: (0, 255, 0),
        3: (0, 0, 255),
        4: (255, 255, 0),
        5: (255, 0, 255),
        6: (0, 255, 255),
        7: (255, 165, 0),
        8: (0, 0, 0),
        9: (128, 128, 128),
        10: (128, 0, 0),
    }

    velocidade = random.randint(1, 10) # Velocidade aleatória
    cor = cores[velocidade] # Cor de acordo com a velocidade
    tamanho = random.randint(10, 30) # Tamanho aleatório
    vidas = random.randint(1, 10) # Vidas aleatórias

    # Retorna o dicionário com as informações da bola para ser adicionado na lista
    return {
        "posicao": [random.randint(200, 600), random.randint(200, 400)],
        "velocidade": velocidade,
        "cor": cor,
        "tamanho": tamanho,
        "vidas": vidas,
        "direcao": pygame.Vector2(1, 1)
    }


def verificaCliqueBolinhas(posicao,listaBolas):
    global pontuacao
    
    for bola in listaBolas:
        retanguloTemporario = pygame.draw.circle(
            tela,
            bola["cor"],
            bola["posicao"],
            bola["tamanho"],
        )

        recebeuCLICK = retanguloTemporario.collidepoint(posicao)

        del retanguloTemporario

        if recebeuCLICK:
            bola["vidas"] -= 1

        if bola["vidas"] <= 0:
            listaBolas.remove(bola)
            pontuacao += 1

pygame.init()
# Configurações da tela
tamanho = (800, 600)
# Cria a tela e define o tamanho
tela = pygame.display.set_mode(tamanho)
# Define o título da tela
pygame.display.set_caption("Pinga")

# Criar um relogio para controlar os FPS
relogio = pygame.time.Clock()

# Parametros do circulo
cor = (255, 0, 0)
posicao = [150, 60]
raio = 50
cor_tela = (255, 255, 255)

pontuacao = 0

# Lista de bolas
listaBolas = []

# Evento para o tempo
novaBolaEvent = pygame.USEREVENT + 1

# Cria o evento a cada 10 segundos
pygame.time.set_timer(novaBolaEvent,1000)

fonte = pygame.font.Font(None, 300)

# LOOP PRINCIPAL
while True:
    # Pega os eventos que estão acontecendo
    for evento in pygame.event.get():
        if evento.type == novaBolaEvent:
            # Adiciona uma nova bola na lista de bolas
            listaBolas.append(novaBola())

        # Se o evento for de fechar a tela
        if evento.type == pygame.QUIT:
            pygame.quit() # Fecha o Pygame
            exit() # Fecha o programa
            
        if evento.type == pygame.MOUSEBUTTONDOWN:  
            if evento.button == 1:
                verificaCliqueBolinhas(evento.pos, listaBolas) 
    #########################################

    # Pinta a tela
    tela.fill(cor_tela)

    texto = fonte.render(f"{pontuacao}",True,(0,0,0))
    texto_rect = texto.get_rect(center=(400,300))
    tela.blit(texto,texto_rect)                     

    # Processa a lista de bolas, desenhando e movendo
    for bola in listaBolas:
        # Desenhar a bola na tela
        circulo = pygame.draw.circle(
            tela, 
            bola["cor"], 
            bola["posicao"],
            bola["tamanho"]
        )
        
        # Movimenta a bola com a velocidade e direção
        bola["posicao"][0] += bola["velocidade"] * bola["direcao"].x
        bola["posicao"][1] += bola["velocidade"] * bola["direcao"].y

        # Verifica se a bola bateu no eixo X
        if bola["posicao"][0] >= tamanho[0] - bola["tamanho"]:
            # Reposiciona a bola para não sair da tela
            bola["posicao"][0] = tamanho[0] - bola["tamanho"]
            bola["direcao"].x = -1
        elif bola["posicao"][0] <= bola["tamanho"]:
            # Reposiciona a bola para não sair da tela
            bola["posicao"][0] = bola["tamanho"]
            bola["direcao"].x = 1

        # Verifica se a bola bateu no eixo Y
        if bola["posicao"][1] >= tamanho[1] - bola["tamanho"]:
            # Reposiciona a bola para não sair da tela
            bola["posicao"][1] = tamanho[1] - bola["tamanho"]
            bola["direcao"].y = -1
        elif bola["posicao"][1] <= bola["tamanho"]:
            # Reposiciona a bola para não sair da tela
            bola["posicao"][1] = bola["tamanho"]
            bola["direcao"].y = 1

    #########################################
    # Atualiza a tela para exibir o que foi desenhado
    pygame.display.update()

    # Controla a quantidade de FPS
    relogio.tick(60)