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

box_width = screen_width / 10
box_height = screen_height / 10


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

five_list = []

for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item
        five_list.append(item)

# Picks a word from the random list of english words 




# displays rows of boxes to the screen


class BoxRow():

    def __init__(self, width, height, amount):
        self.width = width
        self.height = height
        self.amount = amount

    def firstrow():
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2), box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2), box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2), box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2), box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2), box_width, box_height), 3)
        pygame.display.update()

    def secondrow():
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 75, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 75, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 75, box_width, box_height), 3)
        pygame.display.update()

    def thirdrow():
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.display.update()





BoxRow.firstrow()
BoxRow.secondrow()
BoxRow.thirdrow()
pygame.display.update()



girl = ''
boy = 0

print(word)


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

# Loop that keeps the game open until the user quits

def play_game():
    user_word = input('what is your guess? ')
    if user_word == word:
        global girl
        girl = 'You won! '
        print(girl)
    elif len(user_word) != 5 or type(user_word) != str:
        print('guess must be a five letter word')
    elif user_word not in five_list:
        print('invlaid word')
    else:

# correct letter and placement

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

# correct letter but wrong place

        if user_word[0] != word[0] and user_word[0] == word[1] or user_word[0] == word[2] or user_word[0] == word[3] or user_word[0] == word[4]:
            print('first box turns yellow')
        if user_word[1] != word[1] and user_word[1] == word[0] or user_word[1] == word[2] or user_word[1] == word[3] or user_word[1] == word[4]:
            print('second box turns yellow')
        if user_word[2] != word[2] and user_word[2] == word[0] or user_word[2] == word[1] or user_word[2] == word[3] or user_word[2] == word[4]:
            print('third box turns yellow')
        if user_word[3] != word[3] and user_word[3] == word[0] or user_word[3] == word[1] or user_word[3] == word[2] or user_word[3] == word[4]:
            print('fourth box turns yellow')
        if user_word[4] != word[4] and user_word[4] == word[0] or user_word[4] == word[1] or user_word[4] == word[2] or user_word[4] == word[3]:
            print('fifth box turns yellow')

# incorrect letter

        if user_word[0] not in word:
            print('first box turns dark gray')
        if user_word[1] not in word:
            print('second box turns dark gray')
        if user_word[2] not in word:
            print('third box turns dark gray')
        if user_word[3] not in word:
            print('fourth box turns dark gray')
        if user_word[4] not in word:
            print('fifth box turns dark gray')


while boy != 5:
    boy += 1
    play_game()
    if girl == 'You won! ':
        boy = 5


# quits the game if the user gets the word right and prints you won message

