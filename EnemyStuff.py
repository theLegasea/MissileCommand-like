import random

import pygame

# enemies spawn at a random x position at the top of the screen
# they move downwards at a constant speed
# if they reach the PlayerFloor, removed from the screen

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.width = 10
        self.height = 10
        self.color = "red"
        self.x = random.randint(0, screen.get_width() - self.width)
        self.y = 0
        self.speed = 100

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self, dt):
        self.y += self.speed * dt

    def checkCollision(self, playerFloor):
        if self.y + self.height >= playerFloor:
            return True
        return False