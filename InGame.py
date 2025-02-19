import pygame

import Cursor
import EnemyStuff
import GroundObj
import GuiStuff
import Projectile

# 640 by 480 reso
# 3 bases on the ground - QWE shoots
# player moves cursor with keypad?


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0
projectiles = []
enemies = []

cursor = Cursor.Cursor(screen)
groundObj = GroundObj.GroundObj(screen)
gui = GuiStuff.GuiStuff(screen)
enemy = EnemyStuff.Enemy(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                projectiles.append(Projectile.Projectile(screen, groundObj.base1))
            elif event.key == pygame.K_w:
                projectiles.append(Projectile.Projectile(screen, groundObj.base2))
            elif event.key == pygame.K_e:
                projectiles.append(Projectile.Projectile(screen, groundObj.base3))
            elif event.key == pygame.K_RIGHT:
                gui.updateDifficulty(1)
            elif event.key == pygame.K_LEFT:
                gui.updateDifficulty(-1)


    screen.fill("lightgray")

    for projectile in projectiles[:]:
        if projectile.update(dt):
            projectiles.remove(projectile)
        else:
            projectile.draw()
            for enemy in enemies[:]:
                if projectile.checkCollision(enemy):
                    enemies.remove(enemy)
                    gui.score += 100
    for enemy in enemies:
        enemy.update(dt)
        enemy.draw()




    # ground stuff
    groundObj.draw()
    # gui stuff
    gui.draw()
    # cursor stuff
    cursor.draw()
    cursor.update()
    # enemy stuff
    if gui.difficultyLevel == 0 and len(enemies) < 6 and pygame.time.get_ticks() % 3000 < dt * 1000:
        new_enemy = EnemyStuff.Enemy(screen)
        new_enemy.speed = 25
        enemies.append(new_enemy)
    elif gui.difficultyLevel == 1 and len(enemies) < 10 and pygame.time.get_ticks() % 2500 < dt * 1000:
        new_enemy = EnemyStuff.Enemy(screen)
        new_enemy.speed = 50
        enemies.append(new_enemy)
    elif gui.difficultyLevel == 2 and len(enemies) < 15 and pygame.time.get_ticks() % 2500 < dt * 1000:
        new_enemy = EnemyStuff.Enemy(screen)
        new_enemy.speed = 75
        enemies.append(new_enemy)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()