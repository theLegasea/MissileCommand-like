import pygame

# the playerFloor y position of the ground, slightly above the bottom of the screen
# on the ground, there are 3 bases, rendered as rectangles

class GroundObj:
    def __init__(self, screen):
        self.screen = screen
        self.playerFloor = screen.get_height() - 50
        self.base1 = pygame.Rect(50, self.playerFloor - 25, 50, 25)
        self.base2 = pygame.Rect(300, self.playerFloor - 25, 50, 25)
        self.base3 = pygame.Rect(550, self.playerFloor - 25, 50, 25)
        self.color = "slategray"
        self.shooting = False

    def draw(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.line(self.screen, "green", (0, self.playerFloor), (self.screen.get_width(), self.playerFloor))
        pygame.draw.rect(self.screen, self.color, self.base1)
        pygame.draw.rect(self.screen, self.color, self.base2)
        pygame.draw.rect(self.screen, self.color, self.base3)

        def calculate_line_end(start_x, start_y):
            dx = mouse_x - start_x
            dy = mouse_y - start_y
            length = (dx ** 2 + dy ** 2) ** 0.5
            # normalize
            if length > 0:
                dx = dx / length * 25
                dy = dy / length * 25
            return start_x + dx, start_y + dy
        for base in [self.base1, self.base2, self.base3]:
            start_pos = (base.x + base.width / 2, base.y)
            end_pos = calculate_line_end(*start_pos)
            pygame.draw.line(self.screen, "black", start_pos, end_pos)



    def checkCollision(self, enemy):
        if enemy.y + enemy.height >= self.playerFloor:
            return True
        return False

