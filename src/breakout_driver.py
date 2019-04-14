VERSION = "0.4"

import math, os, pygame, random
from src import bin_io
from pygame.locals import *

pygame.font.init()


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
----------------------------------screen backround----------------------------------------
"""


class Backround(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('back_ground_spec.jpg')
        self.rect = self.image.get_rect()
        screen = pygame.display.self.image()
        self.area = screen.get_rect()
        self.rect.move_ip(self.area.centerx, self.area.centery)


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

    def __init__(self, vector, paddle):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_png('ball.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0
        self.state = Ball.still
        self.x = self.area.centerx
        self.y = self.area.centery
        self.theta = math.pi / 2
        # NEW
        self.rect.move_ip(self.area.centerx, self.area.centery)
        self.player1 = paddle

    def set_bricks(self, bricks):
        self.brick_list = bricks

    def update(self):
        angle, z = self.vector
        if self.state == Ball.still:
            self.rect.midbottom = self.player1.rect.midtop
            angle = math.pi / 2
            self.vector = (angle, z)
        else:
            newpos = calcnewpos(self.rect, self.vector)
            self.rect = newpos

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
                self.player1.rect.inflate(-3, -3)

                # Do ball and bat collide?
                # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
                # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
                # bat, the ball reverses, and is still inside the bat, so bounces around inside.
                # This way, the ball can always escape and bounce away cleanly
                if self.rect.colliderect(self.player1.rect) == 1 and not self.hit:
                    x2 = self.player1.rect.centerx
                    x1 = self.rect.centerx
                    dx = x1 - x2
                    dx /= 80
                    angle = dx - (math.pi / 2)
                    self.hit = not self.hit
                elif self.hit:
                    self.hit = not self.hit
                for brick in self.brick_list:
                    if self.rect.colliderect(brick.rect) == 1 and not self.hit:
                        brick.hit()
                        if brick.rect.bottom > self.rect.centery > brick.rect.top:
                            angle = math.pi - angle
                        else:
                            angle = -angle
                        break

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
        self.x = 0
        self.Y = 1

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

    def hit(self):
        self.hp -= 1

    def is_dead(self):
        return self.hp <= 0

    def brick_gen(self):
        b = []
        self.x = 0
        self.y = 0
        # for new_x in range(0, 1025, 128):
        #     for new_y in range(0, 393, 64):
        #         block = Brick(new_x, new_y + 40, 1)
        #         b.append(block)
        b.append(Brick(random.randint(0, 500), random.randint(0, 500)))
        b.append(Brick(random.randint(0, 500), random.randint(0, 500)))
        for i in b:
            self.x = [0]
            self.y = [1]
        return b


def brick_gen():
    brick_list = []
    x = 0
    y = 0
    # for new_x in range(0, 1025, 128):
    #     for new_y in range(0, 393, 64):
    #         block = Brick(new_x, new_y + 40, 1)
    #         b.append(block)
    brick_list.append(Brick(random.randint(0, 500), random.randint(0, 500)))
    brick_list.append(Brick(random.randint(0, 500), random.randint(0, 500)))
    for i in brick_list:
        x = [0]
        y = [1]
    return brick_list




'''
----------------------------MAIN METHOD---------------------
'''


def main():
    from src.given import Fonts
    from src.given import Colors
    from src.given import draw_text_to_screen
    # Initialize screen

    pygame.init()
    screen = pygame.display.set_mode((1024, 720))
    pygame.display.set_caption('(bour, doleva)\'s Pong: v' + str(VERSION))

    global ball, score

    try:
        bl, player1, bricks, sc, lives, level = bin_io.read_file("../data/file")
        score = sc
        ball = bl
    except FileNotFoundError:
        ball = Ball((math.pi / 2, 10), Paddle())
        player1 = Paddle()
        lives = 3
        level = 1
        score = 0

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    brick_list = []

    ball.set_bricks(brick_list)

    # Initialize sprites
    playersprites = pygame.sprite.RenderPlain(player1)
    ballsprite = pygame.sprite.RenderPlain(ball)
    bricksprite = pygame.sprite.RenderPlain(brick_list)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # GAME STATES

    SAVE = "Save"
    LEVEL_SCREEN = "Level Up"
    GAME_OVER = "Game Over"
    PLAY = "Play"
    PAUSED = "Paused"
    MAIN_SCREEN = "Welcome To Breakout"
    EASY_SCREEN = "Easy"
    state = MAIN_SCREEN
    exit_requested = False

    # Initialize clock
    clock = pygame.time.Clock()
    '''
    ---------------------------------------------------------------------
    '''


    '''
    ----------------------------------------------------------------------
    '''

    # Event loop
    while not exit_requested:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        events = pygame.event.get()
        # global ball, player1, brick, score
        # try:
        #     ball, paddle, bricks, score, lives, level = bin_io.read_file("..//data//file")
        # except FileNotFoundError:
        #     ball = Ball((math.pi/2,10))
        #     player1 = Paddle()

        # for event in events:
        #     if event.type == pygame.QUIT:
        #         exit_requested = True
        # if exit_requested:
        #     continue

        for event in events:
            if event.type == pygame.QUIT:
                if state == PLAY:
                    bin_io.save_file("../data/file", ball, player1, brick_list, score, lives, level)
                exit_requested = True
        if exit_requested:
            continue

        if state == MAIN_SCREEN:

            draw_text_to_screen(screen, "Welcome", 250, 100, Colors.WHITE, Fonts.TITLE_FONT)
            draw_text_to_screen(screen, "Easy", 250, 300, Colors.WHITE, Fonts.TITLE_FONT)
            draw_text_to_screen(screen, "Hard", 250, 400, Colors.WHITE, Fonts.TITLE_FONT)

            # global click
            # mouse = pygame.mouse.get_pos()
            # click = pygame.mouse.get_pressed()
            #
            # for event in events:
            #     if event.type == pygame.MOUSEMOTION:
            #         if click[0] == 1:
            #             state = EASY_SCREEN
            # for event in events:
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         if mouse[0] == 250:
            #             if pygame.MOUSEBUTTONUP:
            #                 state = EASY_SCREEN

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = PLAY
                        screen.fill(Colors.BLACK)
                        brick_list.clear()
                        brick_list = brick_gen()
                        ball.set_bricks(brick_list)
                        bricksprite = pygame.sprite.RenderPlain(brick_list)

        elif state == EASY_SCREEN:

            draw_text_to_screen(screen, "Easy", 250, 300, Colors.WHITE, Fonts.TITLE_FONT)

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = PLAY
                        screen.fill(Colors.BLACK)
                        brick_list.clear()
                        brick_list = brick_gen()
                        ball.set_bricks(brick_list)
                        bricksprite = pygame.sprite.RenderPlain(brick_list)


        elif state == LEVEL_SCREEN:

            draw_text_to_screen(screen, "Level Up", 300, 400, Colors.WHITE, Fonts.TITLE_FONT)

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = PLAY
                        screen.fill(Colors.BLACK)
                        brick_list.clear()
                        brick_list = brick_gen()
                        ball.set_bricks(brick_list)
                        bricksprite = pygame.sprite.RenderPlain(brick_list)
                        level += 1

                        # player1.still()


        elif state == GAME_OVER:
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
                        brick_list.clear()
                        brick_list = brick_gen()
                        ball.set_bricks(brick_list)
                        bricksprite = pygame.sprite.RenderPlain(brick_list)
                        score = 0
                        level = 1
                        lives = 3

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
            screen.fill(Colors.BLACK)
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1.moveleft()
                    if event.key == pygame.K_RIGHT:
                        player1.moveright()
                    if event.key == pygame.K_SPACE:
                        ball.state = Ball.play
                    if event.key == pygame.K_ESCAPE:
                        state = PAUSED
                        screen.fill(Colors.BLACK)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player1.still()
            draw_text_to_screen(screen, "Score:" + str(score), 900, 0, Colors.WHITE, Fonts.TEXT_FONT)
            draw_text_to_screen(screen, "Lives: " + str(lives), 0, 0, Colors.WHITE, Fonts.TEXT_FONT)
            draw_text_to_screen(screen, "Level: " + str(level), 512, 0, Colors.WHITE, Fonts.TEXT_FONT)

            for brick in brick_list:
                if brick.is_dead():
                    brick_list.remove(brick)
                    bricksprite.remove(brick)
                    screen.fill((0, 0, 0))
                    score += 10

            if len(brick_list) == 0:
                ball.state = ball.still
                player1.state = player1.reinit()
                state = LEVEL_SCREEN

                # brick_list = brick_gen()
                # bricksprite = pygame.sprite.RenderPlain(brick_list)
                # level += 1

            # display game over if no lives

            if ball.rect.bottom >= screen.get_height():
                lives -= 1
                # Game Over

            if lives == 0:
                try:
                    os.remove('..//data//file')
                except FileNotFoundError:

                    lives = 3
                    state = GAME_OVER
                    screen.fill(Colors.BLACK)
                    player1.still()

            screen.blit(background, ball.rect, ball.rect)
            screen.blit(background, player1.rect, player1.rect)
            for brick in brick_list:
                screen.blit(background, brick.rect, brick.rect)
            ballsprite.update()
            playersprites.update()
            ballsprite.draw(screen)
            playersprites.draw(screen)
            bricksprite.draw(screen)
            ballsprite.update()
        pygame.display.flip()


'''---------------------------------------------------------------------------------------------------------------------

'''

if __name__ == '__main__':
    main()

    # print(click)
    # print(pygame.mouse.get_focused())
