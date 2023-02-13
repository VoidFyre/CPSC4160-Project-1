import pygame
import view
import entities


def game_loop(surface):
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.exit()
        
        surface.fill(view.screenColor)

        pygame.draw.rect(surface, entities.p1Color, entities.player1)
        pygame.display.update()
