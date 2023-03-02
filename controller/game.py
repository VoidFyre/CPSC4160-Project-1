from os.path import abspath
from model.paddle import Paddle
from model.ball import Ball

from view.menu import *


class Game():
    __instance = None  # class variable to hold the singleton instance

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Ping Pong game")

        self.winner = ""
        self.single_player = True
        self.running, self.playing, self.game_over = True, False, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.SPACE_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 700, 500
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))

        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        self.clock = pygame.time.Clock()

        self.main_menu = MainMenu(self)
        self.start = StartMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.paddleA = Paddle()
        self.paddleB = Paddle()
        self.ball = Ball()

        self.paddleA.rect.x = 30
        self.paddleA.rect.y = 200

        self.paddleB.rect.x = 660
        self.paddleB.rect.y = 200

        self.scoreA = 0
        self.scoreB = 0

        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)

        self.paddle_sound = pygame.mixer.Sound(abspath('resources/ping-contact.ogg'))
        # load the applause sound
        self.applause_sound = pygame.mixer.Sound(abspath('resources/small-applause.ogg'))

    def game_loop(self):
        while self.playing:

            self.check_events()

            winning_score = 11

            if self.scoreA >= winning_score:
                self.winner = "Player A"
                self.game_over = True
            elif self.scoreB >= winning_score:
                self.winner = "Player B"
                self.game_over = True

            if self.game_over:
                self.playing = False
                self.game_over = False
                self.reset_score()

                #reset ball position
                self.ball.reset_()

                self.display_gave_over_menu()

            # mechanics to move paddleA
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddleA.moveUp(5)
            if keys[pygame.K_s]:
                self.paddleA.moveDown(5)

            # mechanics to move paddleB
            if self.single_player:
                ball_center = self.ball.rect.y + self.ball.rect.height / 2
                paddle_center = self.paddleB.rect.y + self.paddleB.rect.height / 2
                if ball_center < paddle_center:
                    self.paddleB.moveUp(6)
                elif ball_center > paddle_center:
                    self.paddleB.moveDown(6)
            else:
                if keys[pygame.K_UP]:
                    self.paddleB.moveUp(5)
                if keys[pygame.K_DOWN]:
                    self.paddleB.moveDown(5)

            self.all_sprites_list.update()

            self.checkBallPosition()

            # if pygame.sprite.collide_mask(self.ball, self.paddleA) or pygame.sprite.collide_mask(self.ball, self.paddleB):
            #     self.ball.bounce()
            #     self.paddle_sound.play()

            self.checkCollision()

            # drawing a net and circle on the display
            self.window.fill((70,130,180))
            pygame.draw.line(self.window, (211, 211, 211), [349, 0], [349, 500], 1)

            pygame.draw.line(self.window, (155, 28, 49), [698, 0], [698, 500], 5)
            pygame.draw.line(self.window, (155, 28, 49), [2, 0], [2, 500], 5)

            # Get the center of the ball
            ball_center = self.ball.rect.center

            # Draw a circle in the center of the screen
            circle_radius = 60
            circle_center = (self.DISPLAY_W // 2, self.DISPLAY_H // 2)
            pygame.draw.circle(self.window, (211, 211, 211), circle_center, circle_radius)

            # Position the circle on the ball
            circle_center = ball_center

            self.all_sprites_list.draw(self.window)

            self.displayScore()

            # screen update
            pygame.display.flip()
            self.clock.tick(60)
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True

    def reset_score(self):
        self.scoreB, self.scoreA = 0, 0

    def reset_states(self):
        self.game_over = False

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY, self.SPACE_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)

        text_surface = font.render(text, True, (255, 20, 123))
        shadow = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        shadow_rect = text_surface.get_rect(center=(x + 2, y+ 2))
        self.display.blit(shadow, shadow_rect)
        self.display.blit(text_surface, text_rect)

    def display_gave_over_menu(self):

        font = pygame.font.Font(self.font_name, 20)
        text = font.render("Winner: " + self.winner, True, (255, 20, 123))
        self.window.blit(text,
                         (self.DISPLAY_W / 2 - text.get_width() / 2, self.DISPLAY_H / 2 - text.get_height()))

        text = font.render("Press space to continue or escape to return to main menu", 1, self.WHITE)
        self.window.blit(text,
                         (self.DISPLAY_W / 2 - text.get_width() / 2, self.DISPLAY_H / 2 + text.get_height()))

        pygame.display.update()

        self.reset_keys()

        game_over_loop = True
        while game_over_loop:
            self.check_events()
            if self.SPACE_KEY:
                self.playing = True
                game_over_loop = False
            if self.ESCAPE_KEY:
                game_over_loop = False
                self.curr_menu = self.main_menu
            self.reset_keys()

    def displayScore(self):
        font = pygame.font.Font(None, 40)
        text = font.render("A: " + str(self.scoreA), True, self.WHITE)
        self.window.blit(text, (150, 10))
        text = font.render("B: " + str(self.scoreB), True, self.WHITE)
        self.window.blit(text, (500, 10))
        text = font.render("Goal: 11", True, self.WHITE)
        self.window.blit(text, (300, 400))

    def checkCollision(self):
        if self.ball.rect.colliderect(self.paddleA.rect) or self.ball.rect.colliderect(self.paddleB.rect):
            self.ball.bounce()
            self.paddle_sound.play()

    def checkBallPosition(self):
        # mechanics to check position of the ball
        if self.ball.rect.x >= 690:
            self.scoreA += 1
            # play the applause sound
            self.applause_sound.play()
            self.ball.reset_()
        if self.ball.rect.x <= 0:
            self.scoreB += 1
            # play the applause sound
            self.applause_sound.play()
            self.ball.reset_(400, 200)
        if self.ball.rect.y > 480:
            self.ball.velocity[1] = -self.ball.velocity[1]
        if self.ball.rect.y < 1:
            self.ball.velocity[1] = -self.ball.velocity[1]