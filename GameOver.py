import pygame
import Cursor
import GuiStuff
import InGame


# print game over to middle of screen
# print your score
# print a play again button
def game_over(gui):
    pygame.init()
    height = 480
    width = 640
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True
    dt = 0


    cursor = Cursor.Cursor(screen)



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("tomato")

        # all ogre now
        font = pygame.font.SysFont(None, 36)
        gameOver = font.render("Game Over", True, "black")
        screen.blit(gameOver, (screen.get_width() / 2 - gameOver.get_width() / 2, screen.get_height() / 2 - gameOver.get_height() / 2 - 50))
        # your score
        yourScore = font.render("Your Score:" + str(gui.score), True, "black")
        screen.blit(yourScore, (screen.get_width() / 2 - yourScore.get_width() / 2, screen.get_height() / 2 - yourScore.get_height() / 2))
        # again
        playAgain = pygame.Rect(screen.get_width() / 2 - 75, screen.get_height() / 2 + 50, 150, 50)
        pygame.draw.rect(screen, "green", playAgain)
        playText = font.render("Play Again", True, "black")
        screen.blit(playText, (playAgain.x + playAgain.width / 2 - playText.get_width() / 2, playAgain.y + playAgain.height / 2 - playText.get_height() / 2))

        if playAgain.collidepoint(cursor.x, cursor.y) and event.type == pygame.MOUSEBUTTONDOWN:
            InGame.playgame()

        cursor.draw()
        cursor.update()
        pygame.display.flip()
        clock.tick(60) / 1000

    pygame.quit()