import pygame
import view
import entities
import controller

clock = pygame.time.Clock()

ball = entities.Ball([255, 255, 255], 10, 10)
def game_loop(surface):
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        surface.fill(view.screenColor)

        controller.p1Move(entities.player1)
        controller.p2Move(entities.player2)

        entities.player1.clamp_ip(surface.get_rect())
        entities.player2.clamp_ip(surface.get_rect())
        ball.clamp_ip(surface.get_rect())

        if entities.ball.x>=790:
            entities.ballVelocity[0] = -entities.ballVelocity[0]
        if entities.ball.x<=0:
            entities.ballVelocity[0] = -entities.ballVelocity[0]
        if entities.ball.y>=590:
            entities.ballVelocity[1] = -entities.ballVelocity[1]
        if entities.ball.y<=0:
            entities.ballVelocity[1] = -entities.ballVelocity[1] 

        if entities.ball.collidedict(entities.player1) or entities.ball.collidedict(entities.player2):
            entities.bounceBall()

        pygame.draw.rect(surface, entities.p1Color, entities.player1)
        pygame.draw.rect(surface, entities.p2Color, entities.player2)
        pygame.draw.rect(surface, entities.ballColor, entities.ball)

        entities.updateBall()
        pygame.display.update()

        clock.tick(60)

