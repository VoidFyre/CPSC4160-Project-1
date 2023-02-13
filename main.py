import pygame
import view
import gameLoop

pygame.init()
pygame.display.set_caption("P O N G")
surface = pygame.display.set_mode(view.SCREEN_SIZE)

gameLoop.game_loop(surface)