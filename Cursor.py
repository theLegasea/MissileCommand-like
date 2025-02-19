import pygame

#create a class for the cursor
class Cursor:
    #initialize the cursor, drawing a circle shape at the center of the screen
    def __init__(self, screen):
        self.screen = screen
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.radius = 5
        self.color = "black"
        self.speed = 200

    #draw the cursor on the screen
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    #udpate the cursor position following the mouse
    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.x -= self.radius
        self.y -= self.radius

    def interact(self):
        if pygame.mouse.get_pressed()[0]:
            actionPos = pygame.mouse.get_pos()
            return actionPos