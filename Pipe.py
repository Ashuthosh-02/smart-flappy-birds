import pygame
import random
#pipe_img=pygame.image.load("pipes.png")

class pipe():
    def __init__(self):
        self.x=800
        self.y=random.randint(300,600)
    def move(self):

        self.x-=10


