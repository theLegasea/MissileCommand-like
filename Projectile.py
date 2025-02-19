import time

import pygame

# projectiles are shot from the tips of barrels from the bases
# projectiles move at a constant speed of 200 px per second
# when the projectile reaches the end point, it explodes into a circle (maybe 2 circle, red outside orange inside?

class Projectile:
    def __init__(self, screen, base):
        self.screen = screen
        self.x = base.x + base.width / 2
        self.y = base.y
        self.start_x = self.x
        self.start_y = self.y
        self.end_x, self.end_y = pygame.mouse.get_pos()
        self.radius = 5
        self.color = (255, 165, 0)
        self.speed = 200
        self.explosionDuration = 2
        self.isExploding = False
        self.explosionStart = None

    def draw(self):
        if self.isExploding:
            self.draw_explosion()
        else:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self, dt):
        if self.isExploding:
            if time.time() - self.explosionStart > self.explosionDuration:
                return True
            return False

        dx = self.end_x - self.x
        dy = self.end_y - self.y
        length = (dx ** 2 + dy ** 2) ** 0.5
        if length > 0:
            dx = dx / length * self.speed * dt
            dy = dy / length * self.speed * dt
        self.x += dx
        self.y += dy

        # distance to end
        distance_to_end = ((self.end_x - self.x) ** 2 + (self.end_y - self.y) ** 2) ** 0.5
        total_distance = ((self.end_x - self.start_x) ** 2 + (self.end_y - self.start_y) ** 2) ** 0.5
        if distance_to_end < 1:
            self.isExploding = True
            self.explosionStart = time.time()
            return False

        # color from distance
        t = distance_to_end / total_distance
        r = int(255)
        g = int(165 * t)
        b = 0
        self.color = (r, g, b)
        return False

    def draw_explosion(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.end_x, self.end_y), self.radius * 4.5)
        for i in range(int(self.radius * 4.5), int(self.radius * 2), -1):
            color = (255, int(165 * (i / (self.radius * 4.5))), 0)
            pygame.draw.circle(self.screen, color, (self.end_x, self.end_y), i)


    def checkCollision(self, enemy):
        if self.isExploding:
            distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
            if distance < self.radius * 4.5:
                return True
        return False