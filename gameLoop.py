import pygame
import view
import entities
import controller


def game_loop(surface):
    newBall = entities.Ball()
    clock = pygame.time.Clock()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        surface.fill(view.screenColor)

        controller.p1Move(entities.player1)
        controller.p2Move(entities.player2)

        entities.player1.clamp_ip(surface.get_rect())
        entities.player2.clamp_ip(surface.get_rect())

        newBall.clamp_ip(surface.get_rect())

        if newBall.x>=790:
            newBall.ballVelocity[0] = -newBall.ballVelocity[0]
        if newBall.x<=0:
            newBall.ballVelocity[0] = -newBall.ballVelocity[0]
        if newBall.y>=590:
            newBall.ballVelocity[1] = -newBall.ballVelocity[1]
        if newBall.y<=0:
            newBall.ballVelocity[1] = -newBall.ballVelocity[1]

        pygame.draw.rect(surface, entities.p1Color, entities.player1)
        pygame.draw.rect(surface, entities.p2Color, entities.player2)
        newBall.drawBall(surface)
        
        newBall.updateBall()
        pygame.display.update()

        print(newBall.x + newBall.y)

        clock.tick(60)

