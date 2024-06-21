import pygame
import sys
import random

# Initialize Pygame
pygame.init()
my_file = open("words.txt", "r", encoding="utf-8")
data = my_file.read()
words = data.split("\n")
word = random.choice(words)

pygame.display.set_caption('Wisielec')  # Title
# VARIABLES
checked_letters = []


class Game:
    def __init__(self):
        self.lifes = 11
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((100, 121, 12))
        cords = (100, 200)
        length = int(300 / len(word))
        for _ in word:
            pygame.draw.line(self.screen, (0, 0, 0), cords, (cords[0] + length, cords[1]))
            cords = (cords[0] + 2 * length, cords[1])
        pygame.display.flip()

    def print_lines(self, my_word, letter):
        cords = (100, 200)
        length = int(300 / len(my_word))
        for w in my_word:

            if w == letter:
                self.draw_text(w, pygame.font.Font(None, 36), (255, 255, 255), cords[0] + length // 2, cords[1] - 20)
            cords = (cords[0] + 2 * length, cords[1])
        pygame.display.flip()

    def print_checked_letters(self):
        x_start = 50
        y = 50
        for idx, letter in enumerate(checked_letters):
            x = x_start + idx * 30
            self.draw_text(letter, pygame.font.Font(None, 40), (255, 255, 255), x, y)

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_hangman(self):
        cord = (500, 550)
        length = 90
        width = 4
        match self.lifes:
            case 11:
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] + length, cord[1]), width)
            case 10:
                cord = (cord[0] + length / 2, cord[1])
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0], cord[1] - 2 * length), width)
            case 9:
                cord = (cord[0] + length / 2, cord[1] - 2 * length)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] + length, cord[1]), width)
            case 8:
                cord = (cord[0] + length, cord[1] - 2 * length)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] - length / 2, cord[1] + length / 2), width)
            case 7:
                cord = (cord[0] + 1.5 * length, cord[1] - 2 * length)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0], cord[1] + length / 2), width)
            case 6:
                cord = (cord[0] + 1.5 * length, cord[1] - 1.25 * length)
                pygame.draw.circle(self.screen, (0, 0, 0), cord, length / 4, width)
            case 5:
                cord = (cord[0] + 1.5 * length, cord[1] - length - width / 2)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] - length / 8, cord[1] + length / 4), width)
            case 4:
                cord = (cord[0] + 1.5 * length, cord[1] - length - width / 2)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] + length / 8, cord[1] + length / 4), width)
            case 3:
                cord = (cord[0] + 1.5 * length, cord[1] - length - width / 2)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0], cord[1] + length / 2), width)
            case 2:
                cord = (cord[0] + 1.5 * length, cord[1] - length / 2 - width / 2)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] - length / 8, cord[1] + length / 4), width)
            case 1:
                cord = (cord[0] + 1.5 * length, cord[1] - length / 2 - width / 2)
                pygame.draw.line(self.screen, (0, 0, 0), cord, (cord[0] + length / 8, cord[1] + length / 4), width)
                return False
        self.lifes -= 1

    def make_game(self, my_word):
        counter = my_word.__len__()
        running = True
        while running:
            # Handle user input and events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():  # Check if the pressed key is a letter
                        letter = event.unicode  # Update the letter variable with the pressed letter
                        if letter not in my_word:
                            if letter not in checked_letters:
                                checked_letters.append(letter)
                                if self.draw_hangman() is False:
                                    running = False
                        else:
                            if letter not in checked_letters:
                                checked_letters.append(letter)
                                decrement = my_word.count(letter)
                                print(checked_letters)
                                counter -= decrement
                        self.print_lines(my_word, letter)
                if counter == 0:
                    running = False
                self.print_checked_letters()
                pygame.display.flip()

        print(word)
        pygame.quit()
        sys.exit()


scr = Game()
scr.make_game(word)
