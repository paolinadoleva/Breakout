import os
import pygame
import math
import random


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


def calc_new_pos(rect, vector):
    (angle, z) = vector
    (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
    return rect.move(dx, dy)


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





def b():
    b = []
    y = []
    x = []
    # for new_x in range(0, 1025, 128):
    #     for new_y in range(0, 393, 64):
    #         block = Brick(new_x, new_y + 40, 1)
    #         b.append(block)
    b.append((random.randint(0, 500), random.randint(0, 500)))


    b.append((random.randint(0, 500), random.randint(0, 500)))
    for i in b:
        x.append(i[0])
        y.append(i[1])
        print(x)
        print(y)
b()
