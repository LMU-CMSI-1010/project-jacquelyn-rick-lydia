import pygame
import english_words
import time

pygame.init()

green = (0, 255, 0)




game_screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('wordle game!')
pygame.draw.rect(game_screen, green, (30, 30, 50, 30))
time.sleep(10)



from english_words import english_words_lower_alpha_set


for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item

# Picks a word from the random list of english words




