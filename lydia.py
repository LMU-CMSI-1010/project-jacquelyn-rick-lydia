import pygame
import english_words
import time

pygame.init()

green = (0, 200, 0)
blue = (0, 0, 200)
red = (200, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
light_gray = (200, 200, 200)

screen_width = 500
screen_height = 500


screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)


pygame.display.set_caption('Wordle Game')

font = pygame.font.SysFont('timesnewroman', 56)
text = font.render('Wordle', True, black, None)

text_rect = text.get_rect(center = (screen_width / 2, screen_height / 10))
screen.blit(text, text_rect)

# Centers the text and puts it onto the screen

pygame.display.update()


from english_words import english_words_lower_alpha_set


for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item

# Picks a word from the random list of english words


girl = ''
boy = 0

print(word)

def play_game():
    user_word = input('what is your guess? ')
    if user_word == word:
        global girl
        girl = 'You won! '
        print(girl)
    elif len(user_word) != 5 or type(user_word) != str:
        print('guess must be a five letter word')
    else:
        if user_word[0] == word[0]:
            print('first box turns green')
        if user_word[1] == word[1]:
            print('second box turns green')
        if user_word[2] == word[2]:
            print('third box turns green')
        if user_word[3] == word[3]:
            print('fourth box turns green')
        if user_word[4] == word[4]:
            print('fifth box turns green')


while boy != 5:
    boy += 1
    play_game()
    if girl == 'You won! ':
        boy = 5


'''playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False'''

# Loop that keeps the game open until the user quits

pygame.display.update()





