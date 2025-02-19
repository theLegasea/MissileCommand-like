import pygame
import Cursor

# 640 by 480 reso
# 3 bases on the ground - QWE shoots
# player moves cursor with keypad?


pygame.init()
height = 480
width = 640
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
dt = 0

# Cursor
cursor = Cursor.Cursor(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # render the gray backdrop
    screen.fill("lightgray")
    # print the title "Almost Missile Command" at the top of the screen
    font = pygame.font.SysFont(None, 36)
    title = font.render("Almost Missile Command", True, "black")
    screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, 10))

    # Play button in the center of the screen
    playButton = pygame.Rect(screen.get_width() / 2 - 50, screen.get_height() / 2 - 25, 100, 50)
    pygame.draw.rect(screen, "red", playButton)
    playText = font.render("Play", True, "black")
    screen.blit(playText, (playButton.x + playButton.width / 2 - playText.get_width() / 2, playButton.y + playButton.height / 2 - playText.get_height() / 2))

    cursor.update()

    if playButton.collidepoint(cursor.x, cursor.y) and event.type == pygame.MOUSEBUTTONDOWN:
        import InGame



    cursor.draw()

    pygame.display.flip()
pygame.quit()