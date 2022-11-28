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
yellow = (255, 235, 0)
dark_gray = (135, 135, 135)


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



from english_words import english_words_lower_alpha_set

five_list = []

for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item
        five_list.append(item)

# Picks a word from the random list of english words 

r1b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2), box_width, box_height)
r1b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2), box_width, box_height)
r1b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2), box_width, box_height)
r1b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2), box_width, box_height)
r1b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2), box_width, box_height)

r2b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 75, box_width, box_height)
r2b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height)
r2b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 75, box_width, box_height)
r2b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height)
r2b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 75, box_width, box_height)

r3b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 150, box_width, box_height)
r3b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height)
r3b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 150, box_width, box_height)
r3b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height)
r3b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 150, box_width, box_height)

r4b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 225, box_width, box_height)
r4b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 225, box_width, box_height)
r4b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 225, box_width, box_height)
r4b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 225, box_width, box_height)
r4b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 225, box_width, box_height)

r5b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 300, box_width, box_height)
r5b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 300, box_width, box_height)
r5b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 300, box_width, box_height)
r5b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 300, box_width, box_height)
r5b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 300, box_width, box_height)


# displays rows of boxes to the screen:


class BoxRow():

    def __init__(self):
        pass

    def firstrow():
        pygame.draw.rect(screen, light_gray, r1b3, 3)
        pygame.draw.rect(screen, light_gray, r1b2, 3)
        pygame.draw.rect(screen, light_gray, r1b1, 3)
        pygame.draw.rect(screen, light_gray, r1b4, 3)
        pygame.draw.rect(screen, light_gray, r1b5, 3)
        pygame.display.update()

    def secondrow():
        pygame.draw.rect(screen, light_gray, r2b3, 3)
        pygame.draw.rect(screen, light_gray, r2b2, 3)
        pygame.draw.rect(screen, light_gray, r2b1, 3)
        pygame.draw.rect(screen, light_gray, r2b4, 3)
        pygame.draw.rect(screen, light_gray, r2b5, 3)
        pygame.display.update()

    def thirdrow():
        pygame.draw.rect(screen, light_gray, r3b3, 3)
        pygame.draw.rect(screen, light_gray, r3b2, 3)
        pygame.draw.rect(screen, light_gray, r3b1, 3)
        pygame.draw.rect(screen, light_gray, r3b4, 3)
        pygame.draw.rect(screen, light_gray, r3b5, 3)
        pygame.display.update()

    def fourthrow():
        pygame.draw.rect(screen, light_gray, r4b3, 3)
        pygame.draw.rect(screen, light_gray, r4b2, 3)
        pygame.draw.rect(screen, light_gray, r4b1, 3)
        pygame.draw.rect(screen, light_gray, r4b4, 3)
        pygame.draw.rect(screen, light_gray, r4b5, 3)
        pygame.display.update()

    def fifthrow():
        pygame.draw.rect(screen, light_gray, r5b3, 3)
        pygame.draw.rect(screen, light_gray, r5b2, 3)
        pygame.draw.rect(screen, light_gray, r5b1, 3)
        pygame.draw.rect(screen, light_gray, r5b4, 3)
        pygame.draw.rect(screen, light_gray, r5b5, 3)
        pygame.display.update()

    def turn_green(box):
        pygame.draw.rect(screen, green, box, 0)
        pygame.display.update()

    def turn_yellow(box):
        pygame.draw.rect(screen, yellow, box, 0)
        pygame.display.update()

    def turn_dark_gray(box):
        pygame.draw.rect(screen, dark_gray, box, 0)
        pygame.display.update()

BoxRow.firstrow()
BoxRow.secondrow()
BoxRow.thirdrow()
BoxRow.fourthrow()
BoxRow.fifthrow()



counter = 0

print(word)

# Loop that keeps the game open until the user quits

user_word = ''

def play_game():
    user_word = input('what is your guess? ')
    if len(user_word) != 5 or type(user_word) != str:
        print('guess must be a five letter word')
    elif user_word not in five_list:
        print('invalid word')
    else:
        if counter == 1:

# correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r1b1)
            if user_word[1] == word[1]:
                BoxRow.turn_green(r1b2)
            if user_word[2] == word[2]:
                BoxRow.turn_green(r1b3)
            if user_word[3] == word[3]:
                BoxRow.turn_green(r1b4)
            if user_word[4] == word[4]:
                BoxRow.turn_green(r1b5)
            if user_word == word:
                print('You won! ')
                BoxRow.turn_green(r1b1)
                BoxRow.turn_green(r1b2)
                BoxRow.turn_green(r1b3)
                BoxRow.turn_green(r1b4)
                BoxRow.turn_green(r1b5)


# correct letter but wrong place

            if user_word[0] != word[0] and user_word[0] in word:
                BoxRow.turn_yellow(r1b1)
            if user_word[1] != word[1] and user_word[1] in word:
                BoxRow.turn_yellow(r1b2)
            if user_word[2] != word[2] and user_word[2] in word:
                BoxRow.turn_yellow(r1b3)
            if user_word[3] != word[3] and user_word[3] in word:
                BoxRow.turn_yellow(r1b4)
            if user_word[4] != word[4] and user_word[4] in word:
                BoxRow.turn_yellow(r1b5)

# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r1b1)
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r1b2)
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r1b3)
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r1b4)
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r1b5)

        
        elif counter == 2:

            # correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r2b1)
            if user_word[1] == word[1]:
                BoxRow.turn_green(r2b2)
            if user_word[2] == word[2]:
                BoxRow.turn_green(r2b3)
            if user_word[3] == word[3]:
                BoxRow.turn_green(r2b4)
            if user_word[4] == word[4]:
                BoxRow.turn_green(r2b5)
            if user_word == word:
                print('You won! ')
                BoxRow.turn_green(r2b1)
                BoxRow.turn_green(r2b2)
                BoxRow.turn_green(r2b3)
                BoxRow.turn_green(r2b4)
                BoxRow.turn_green(r2b5)
 

# correct letter but wrong place

            if user_word[0] != word[0] and user_word[0] in word:
                BoxRow.turn_yellow(r2b1)
            if user_word[1] != word[1] and user_word[1] in word:
                BoxRow.turn_yellow(r2b2)
            if user_word[2] != word[2] and user_word[2] in word:
                BoxRow.turn_yellow(r2b3)
            if user_word[3] != word[3] and user_word[3] in word:
                BoxRow.turn_yellow(r2b4)
            if user_word[4] != word[4] and user_word[4] in word:
                BoxRow.turn_yellow(r2b5)
            

# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r2b1)
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r2b2)
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r2b3)
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r2b4)
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r2b5)

            pygame.display.update()

        elif counter == 3:

            # correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r3b1)
            if user_word[1] == word[1]:
                BoxRow.turn_green(r3b2)
            if user_word[2] == word[2]:
                BoxRow.turn_green(r3b3)
            if user_word[3] == word[3]:
                BoxRow.turn_green(r3b4)
            if user_word[4] == word[4]:
                BoxRow.turn_green(r3b5)
            if user_word == word:
                print('You won! ')
                BoxRow.turn_green(r3b1)
                BoxRow.turn_green(r3b2)
                BoxRow.turn_green(r3b3)
                BoxRow.turn_green(r3b4)
                BoxRow.turn_green(r3b5)
        

# correct letter but wrong place

            if user_word[0] != word[0] and user_word[0] in word:
                BoxRow.turn_yellow(r3b1)
            if user_word[1] != word[1] and user_word[1] in word:
                BoxRow.turn_yellow(r3b2)
            if user_word[2] != word[2] and user_word[2] in word:
                BoxRow.turn_yellow(r3b3)
            if user_word[3] != word[3] and user_word[3] in word:
                BoxRow.turn_yellow(r3b4)
            if user_word[4] != word[4] and user_word[4] in word:
                BoxRow.turn_yellow(r3b5)
            

# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r3b1)
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r3b2)
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r3b3)
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r3b4)
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r3b5)

            pygame.display.update()

        elif counter == 4:

            # correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r4b1)
            if user_word[1] == word[1]:
                BoxRow.turn_green(r4b2)
            if user_word[2] == word[2]:
                BoxRow.turn_green(r4b3)
            if user_word[3] == word[3]:
                BoxRow.turn_green(r4b4)
            if user_word[4] == word[4]:
                BoxRow.turn_green(r4b5)
            if user_word == word:
                print('You won! ')
                BoxRow.turn_green(r4b1)
                BoxRow.turn_green(r4b2)
                BoxRow.turn_green(r4b3)
                BoxRow.turn_green(r4b4)
                BoxRow.turn_green(r4b5)


# correct letter but wrong place

            if user_word[0] != word[0] and user_word[0] in word:
                BoxRow.turn_yellow(r4b1)
            if user_word[1] != word[1] and user_word[1] in word:
                BoxRow.turn_yellow(r4b2)
            if user_word[2] != word[2] and user_word[2] in word:
                BoxRow.turn_yellow(r4b3)
            if user_word[3] != word[3] and user_word[3] in word:
                BoxRow.turn_yellow(r4b4)
            if user_word[4] != word[4] and user_word[4] in word:
                BoxRow.turn_yellow(r4b5)
            

# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r4b1)
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r4b2)
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r4b3)
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r4b4)
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r4b5)

            pygame.display.update()

        elif counter == 5:

            # correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r5b1)
            if user_word[1] == word[1]:
                BoxRow.turn_green(r5b2)
            if user_word[2] == word[2]:
                BoxRow.turn_green(r5b3)
            if user_word[3] == word[3]:
                BoxRow.turn_green(r5b4)
            if user_word[4] == word[4]:
                BoxRow.turn_green(r5b5)
            if user_word == word:
                print('You won! ')
                BoxRow.turn_green(r5b1)
                BoxRow.turn_green(r5b2)
                BoxRow.turn_green(r5b3)
                BoxRow.turn_green(r5b4)
                BoxRow.turn_green(r5b5)


# correct letter but wrong place

            if user_word[0] != word[0] and user_word[0] in word:
                BoxRow.turn_yellow(r5b1)
            if user_word[1] != word[1] and user_word[1] in word:
                BoxRow.turn_yellow(r5b2)
            if user_word[2] != word[2] and user_word[2] in word:
                BoxRow.turn_yellow(r5b3)
            if user_word[3] != word[3] and user_word[3] in word:
                BoxRow.turn_yellow(r5b4)
            if user_word[4] != word[4] and user_word[4] in word:
                BoxRow.turn_yellow(r5b5)



# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r5b1)
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r5b2)
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r5b3)
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r5b4)
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r5b5)

            pygame.display.update()



playing = True
while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            while counter != 5:
                counter += 1
                print(counter)
                play_game()
                if user_word == word:
                    counter = 5

pygame.display.update()

# quits the game if the user gets the word right and prints you won message