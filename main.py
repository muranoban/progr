import pygame
from pygame.locals import *
from obstaculos import Obstaculos
from personagem import Persona
from municao import Municao
import random


##inica o pygame e suas dependências

pygame.init()
pygame.font.init()
pygame.mixer.init()

##Definições da janela do game

screenDimension=(750,500)
pygame.display.set_caption("Galo Agiota 1.0")
screen=pygame.display.set_mode(screenDimension, 0, 32)
pygame.display.set_icon(screen)

##Define variáveis com valores de cor ou coordenada

azul=(108,194,236)
branco=(255,255,255)

# MUSICA DE FUNDO

pygame.mixer.music.load("data/ambiente.wav")
pygame.mixer.music.play(-1)

# SONS DE AÇÕES


# CHAMANDO OBJETO
objectGroup = pygame.sprite.Group()
obstaculosGroup=pygame.sprite.Group()
tiroGroup=pygame.sprite.Group()

#INSTANCIA DO OBJETO
personagem =Persona(objectGroup)


timer = 0
clock = pygame.time.Clock()

if __name__ == "__main__":
    gameLooping=True
    perdeu=False
    while gameLooping:
        #Limitador de FPS
        clock.tick(60)

        pygame.display.flip()
        screen.fill(branco)
        ##Eventos do game

        for event in pygame.event.get():
            ##Quando aperta o X ele exita o pygame
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    newTiro=Municao(objectGroup,tiroGroup)
                    newTiro.rect.center=personagem.rect.center



        #Lógica do game em sí

        if not perdeu:
            #Gera Os galo schaves
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newObstaculos = Obstaculos(objectGroup,obstaculosGroup)
            #Analisa se tem impacto
            collisions=pygame.sprite.spritecollide(personagem,obstaculosGroup, True, pygame.sprite.collide_mask)
            colliTiro=pygame.sprite.groupcollide(tiroGroup, obstaculosGroup, True, True,pygame.sprite.collide_mask)

            if collisions:
                perdeu = True

        objectGroup.draw(screen)

        ##mouse=pygame.mouse.get_pos()
        ##print(mouse)

        pygame.display.update()







