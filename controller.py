import pygame

speed = 5

def p1Move(player1):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move_ip(0, -speed)
    if keys[pygame.K_s]:
        player1.move_ip(0, speed)

def p2Move(player2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2.move_ip(0, -speed)
    if keys[pygame.K_DOWN]:
        player2.move_ip(0, speed)