import pygame
import view
import entities
import controller


def game_loop(surface):
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.exit()
        
        surface.fill(view.screenColor)

        controller.p1Move(entities.player1)
        controller.p2Move(entities.player2)

        entities.player1.clamp_ip(surface.get_rect())
        entities.player2.clamp_ip(surface.get_rect())

        pygame.draw.rect(surface, entities.p1Color, entities.player1)
        pygame.draw.rect(surface, entities.p2Color, entities.player2)
        pygame.display.update()
