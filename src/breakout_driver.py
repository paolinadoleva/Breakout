VERSION = "0.4"

import math, os, pygame
from pygame.locals import *


def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('../img', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image
    except pygame.error:
        print('Cannot load image:', fullname)


def calcnewpos(rect, vector):
    (angle, z) = vector
    (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
    return rect.move(dx, dy)


"""
----------------------------------------BALL----------------------------------------------
"""


class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    still = 0
    play = 1

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('image.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0
        self.state = Ball.still

        # NEW
        self.rect.move_ip(self.area.centerx, self.area.centery)

    def update(self):

        if self.state == Ball.still:
            self.rect.midbottom = player1.rect.midtop
        else:
            newpos = calcnewpos(self.rect, self.vector)
            self.rect = newpos
            (angle, z) = self.vector

            if not self.area.contains(newpos):
                tl = not self.area.collidepoint(newpos.topleft)
                tr = not self.area.collidepoint(newpos.topright)
                bl = not self.area.collidepoint(newpos.bottomleft)
                br = not self.area.collidepoint(newpos.bottomright)
                bm = self.area.midbottom
                # brick_1 = (pygame.sprite.spritecollide(self.rect, not self.rect, True))
                if (tr and tl) or (br and bl):
                    angle = -angle
                if (tl and bl) or (tr and br):
                    angle = math.pi - angle
                if bm and not tl and not tr:
                    self.state = Ball.still

            else:
                # Deflate the rectangles so you can't catch a ball behind the bat
                player1.rect.inflate(-3, -3)

                # Do ball and bat collide?
                # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
                # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
                # bat, the ball reverses, and is still inside the bat, so bounces around inside.
                # This way, the ball can always escape and bounce away cleanly
                if self.rect.colliderect(player1.rect) == 1 and not self.hit:
                    x2 = player1.rect.centerx
                    x1 = self.rect.centerx
                    dx = x1 - x2
                    dx /= 80
                    angle = dx - (math.pi / 2)
                    self.hit = not self.hit
                elif self.hit:
                    self.hit = not self.hit
                for brick in brick_list:
                    if self.rect.colliderect(brick.rect) == 1 and not self.hit:
                        brick.hit()
                        if brick.rect.bottom > self.rect.centery > brick.rect.top:
                            angle = math.pi - angle
                        else:
                            angle = -angle

            self.vector = (angle, z)


"""
-----------------------------------------PADDLE-----------------------------------------------
"""


class Paddle(pygame.sprite.Sprite):
    """Movable tennis 'bat' with which one hits the ball
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    X = 0
    Y = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('paddle.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0, 0]
        self.rect.midbottom = self.area.midbottom

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveleft(self):
        self.movepos[Paddle.X] = self.movepos[Paddle.X] - self.speed
        self.state = "moveleft"

    def moveright(self):
        self.movepos[Paddle.X] = self.movepos[Paddle.X] + self.speed
        self.state = "moveright"

    def still(self):
        self.movepos = [0, 0]
        self.state = "still"


"""
------------------------------BRICK---------------------------------------------
"""


class Brick(Paddle):

    def __init__(self, x=0, y=0, health=1):
        Paddle.__init__(self)
        self.image = load_png('basic_block.png')
        self.rect = self.image.get_rect()
        self.hp = health
        self.rect.x = x
        self.rect.y = y
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0, 0]
        # self.rect.midtop = self.area.midtop

    def hit(self):
        self.hp -= 1

    def is_dead(self):
        return self.hp <= 0

    # def count_hits(self):
    #
    #     while(self.__hp > 0):
    #         if(self.):
    #             self.__hp -= 1
    #
    #     else:
    #         pass

    # def update(self):
    #     newpos = self.rect.move(self.movepos)
    #     if self.area.contains(newpos):
    #         self.rect = newpos
    #     pygame.event.pump()

    # def add_more(self):
    #     pass


'''
----------------------------MAIN METHOD---------------------
'''


def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((1024, 720))
    pygame.display.set_caption('(bour, doleva)\'s Pong: v' + str(VERSION))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialize players
    global player1
    player1 = Paddle()

    # Initialize brick
    global brick_list
    brick_list = []

    # 1025,128 vs 393,64
    for new_x in range(0, 1025, 128):
        for new_y in range(0, 393, 64):
            block = Brick(new_x, new_y)
            brick_list.append(block)

    # Initialize ball
    speed = 13
    ball = Ball((math.pi / 2, speed))

    # Initialize sprites
    playersprites = pygame.sprite.RenderPlain(player1)
    ballsprite = pygame.sprite.RenderPlain(ball)
    bricksprite = pygame.sprite.RenderPlain(brick_list)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # GAME STATES
    lives = 3
    GAME_OVER = "Game Over"
    PLAY = "Play"
    PAUSED = "Paused"
    state = GAME_OVER
    exit_requested = False

    # Initialize clock
    clock = pygame.time.Clock()

    # Event loop
    while not exit_requested:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                exit_requested = True
        if exit_requested:
            continue

        if state == GAME_OVER:
            # Game Over Out
            x = (screen.get_width() / 2) - 100
            y = (screen.get_height() / 2) - 30

            draw_text_to_screen(screen, "Game Over", x, y, Colors.WHITE, Fonts.TITLE_FONT)


            # Game Over Input
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = PLAY
                        screen.fill(Colors.BLACK)

        elif state == PAUSED:
            # Game Over Out
            x = (screen.get_width() / 2) - 100
            y = (screen.get_height() / 2) - 30

            draw_text_to_screen(screen, "Paused", x, y, Colors.WHITE, Fonts.TITLE_FONT)

            # Game Over Input
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Unpause
                        state = PLAY
                        screen.fill(Colors.BLACK)

        else:
            screen.fill(pygame.Colors.BLACK)
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1.moveleft()
                    if event.key == pygame.K_RIGHT:
                        player1.moveright()
                    if event.key == pygame.K_ESCAPE:
                        state = PAUSED
                        screen.fill(pygame.Colors.BLACK)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player1.still()

            draw_text_to_screen(screen, "Lives: " + str(lives), 0, 0, Colors.WHITE, Fonts.TEXT_FONT)

            if ball.rect.bottom >= screen.get_height():
                lives -= 1
                # Game Over
                if lives == 0:
                    lives = 3
                    state = GAME_OVER
                    screen.fill(Colors.BLACK)


        for brick in brick_list:
            if brick.is_dead():
                brick_list.remove(brick)
                bricksprite.remove(brick)
                screen.fill((0, 0, 0))

        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        ballsprite.update()
        playersprites.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)



        pygame.display.flip()

'''---------------------------------------------------------------------------------------------------------------------

'''



if __name__ == '__main__':
    main()
