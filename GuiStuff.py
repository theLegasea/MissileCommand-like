import pygame

 # the GUI is rendered under the playerFloor height
 # it should display the current difficulty level
 # it should also display the current number of lives left, as well as the player's score

class GuiStuff:
    def __init__(self, screen):
        self.screen = screen
        self.playerFloor = screen.get_height() - 50
        self.difficultyLevel = 0
        self.difficultyText = ["Easy", "Medium", "Hard"]
        self.lives = 3
        self.score = 0
        self.font = pygame.font.SysFont(None, 24)

    def draw(self):
        pygame.draw.line(self.screen, "black", (0, self.playerFloor), (self.screen.get_width(), self.playerFloor))

        difficultyText = self.font.render("Difficulty: " + str(self.difficultyText[self.difficultyLevel]), True, "black")
        self.screen.blit(difficultyText, (10, self.playerFloor + 5))

        livesText = self.font.render("Lives: " + str(self.lives), True, "black")
        self.screen.blit(livesText, (self.screen.get_width() - livesText.get_width() - 10, self.playerFloor + 5))

        scoreText = self.font.render("Score: " + str(self.score), True, "black")
        self.screen.blit(scoreText, (self.screen.get_width() / 2 - scoreText.get_width() / 2, self.playerFloor + 5))

    def updateDifficulty(self, newdiff):
        if newdiff == 1:
            self.difficultyLevel = min(self.difficultyLevel + 1, 2)
        else:
            self.difficultyLevel = max(self.difficultyLevel - 1, 0)

    def update(self, dt):
        pass
