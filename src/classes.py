import pygame
from src import help
import math



"""
----------------------------------------BALL----------------------------------------------
"""


class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = help.load_png('image.png')
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0

        # NEW
        self.rect.move_ip(self.area.centerx, self.area.centery)

    def update(self):
        newpos = help.calc_new_pos(self.rect, self.vector)
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
                z = 0



        else:
            # Deflate the rectangles so you can't catch a ball behind the bat
            player1.rect.inflate(-3, -3)

            # Do ball and bat collide?
            # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
            # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
            # bat, the ball reverses, and is still inside the bat, so bounces around inside.
            # This way, the ball can always escape and bounce away cleanly
            if self.rect.colliderect(player1.rect) == 1 and not self.hit:
                angle = -angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
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
        self.__hp = health
        self.rect.x = x
        self.rect.y = y
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0, 0]
        # self.rect.midtop = self.area.midtop

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

    def add_more(self):
        pass



 # Initialize players
    global player1
    player1 = Paddle()

    # Initialize brick
    global brick
    brick = Brick()
    brick1 = Brick(320,240)
