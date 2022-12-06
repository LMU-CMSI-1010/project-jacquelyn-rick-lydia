import pygame

# initializing the game
pygame.init()
pygame.event.get()

green = (0, 200, 0)
blue = (0, 0, 200)
red = (200, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
light_gray = (200, 200, 200)
yellow = (255, 235, 0)
dark_gray = (135, 135, 135)



screen_width = 600
screen_height = 600


box_width = screen_width / 10
box_height = screen_height / 10


screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)

# Centers the text and puts it onto the screen

pygame.display.set_caption('Wordle Game')

font = pygame.font.SysFont('timesnewroman', 65)
text = font.render('Wordle', True, black, None)

text_rect = text.get_rect(center = (screen_width / 2, screen_height / 10))
screen.blit(text, text_rect)
pygame.display.update()

# Picks a word from the random list of english words 

from english_words import english_words_lower_alpha_set

five_list = []

for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item
        five_list.append(item)

# Creates the rows and boxes

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

r6b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 375, box_width, box_height)
r6b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 375, box_width, box_height)
r6b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 375, box_width, box_height)
r6b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 375, box_width, box_height)
r6b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 375, box_width, box_height)


pygame.display.update()

# Box class

class BoxRow():

    def __init__(self):
        self.firstrow()
        self.secondrow()
        self.thirdrow()
        self.fourthrow()
        self.fifthrow()
        self.sixthrow()

    def firstrow(self):
        pygame.draw.rect(screen, light_gray, r1b3, 3)
        pygame.draw.rect(screen, light_gray, r1b2, 3)
        pygame.draw.rect(screen, light_gray, r1b1, 3)
        pygame.draw.rect(screen, light_gray, r1b4, 3)
        pygame.draw.rect(screen, light_gray, r1b5, 3)
        pygame.display.update()

    def secondrow(self):
        pygame.draw.rect(screen, light_gray, r2b3, 3)
        pygame.draw.rect(screen, light_gray, r2b2, 3)
        pygame.draw.rect(screen, light_gray, r2b1, 3)
        pygame.draw.rect(screen, light_gray, r2b4, 3)
        pygame.draw.rect(screen, light_gray, r2b5, 3)
        pygame.display.update()

    def thirdrow(self):
        pygame.draw.rect(screen, light_gray, r3b3, 3)
        pygame.draw.rect(screen, light_gray, r3b2, 3)
        pygame.draw.rect(screen, light_gray, r3b1, 3)
        pygame.draw.rect(screen, light_gray, r3b4, 3)
        pygame.draw.rect(screen, light_gray, r3b5, 3)
        pygame.display.update()

    def fourthrow(self):
        pygame.draw.rect(screen, light_gray, r4b3, 3)
        pygame.draw.rect(screen, light_gray, r4b2, 3)
        pygame.draw.rect(screen, light_gray, r4b1, 3)
        pygame.draw.rect(screen, light_gray, r4b4, 3)
        pygame.draw.rect(screen, light_gray, r4b5, 3)
        pygame.display.update()

    def fifthrow(self):
        pygame.draw.rect(screen, light_gray, r5b3, 3)
        pygame.draw.rect(screen, light_gray, r5b2, 3)
        pygame.draw.rect(screen, light_gray, r5b1, 3)
        pygame.draw.rect(screen, light_gray, r5b4, 3)
        pygame.draw.rect(screen, light_gray, r5b5, 3)
        pygame.display.update()

    def sixthrow(self):
        pygame.draw.rect(screen, light_gray, r6b3, 3)
        pygame.draw.rect(screen, light_gray, r6b2, 3)
        pygame.draw.rect(screen, light_gray, r6b1, 3)
        pygame.draw.rect(screen, light_gray, r6b4, 3)
        pygame.draw.rect(screen, light_gray, r6b5, 3)
        pygame.display.update()


    def turn_green(self, box):
        pygame.draw.rect(screen, green, box, 0)
        print('turn green function is running')
        pygame.display.update()

    def turn_yellow(self, box):
        pygame.draw.rect(screen, yellow, box, 0)
        print('turn yellow function is running')
        pygame.display.update()

    def turn_dark_gray(self, box):
        pygame.draw.rect(screen, dark_gray, box, 0)
        print('turn dark gray function is running')
        pygame.display.update()


    def quit_game(self):
        pygame.time.delay(3000)
        cong_screen = pygame.Rect(screen_width / 16, screen_height / 4, screen_width * 0.9, screen_height * 0.16)
        pygame.draw.rect(screen, white, cong_screen, 0)
        pygame.draw.rect(screen, red, cong_screen, 4)
        cong_font = pygame.font.SysFont('timesnewroman', 25)
        if counter == 1:
            congrats = cong_font.render('Congrats! You guessed the word in ' + str(counter) + ' try.', True, black, None)
        else:
            congrats = cong_font.render('Congrats! You guessed the word in ' + str(counter) + ' tries.', True, black, None)
        cong_rect = congrats.get_rect(center = (screen_width / 2, screen_height / 3))
        screen.blit(congrats, cong_rect)
        print('congrats')
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    def out_of_tries(self):
        pygame.time.delay(3000)
        out_screen = pygame.Rect(screen_width / 16, screen_height / 4, screen_width * 0.9, screen_height * 0.16)
        pygame.draw.rect(screen, white, out_screen, 0)
        pygame.draw.rect(screen, red, out_screen, 4)
        out_font = pygame.font.SysFont('timesnewroman', 25)
        out = out_font.render('Out of tries! The correct word was: "' + word + '".', True, black, None)
        out_rect = out.get_rect(center = (screen_width / 2, screen_height / 3))
        screen.blit(out, out_rect)
        print('out of tries')
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()



# print(word)

# Loop that keeps the game open until the user quits

user_word = ''

def play_game(game):
    user_word = input('what is your guess? ')
    if len(user_word) != 5:
        print('guess must be a five letter word')
        return True
    else:

# incorrect letter

        if user_word[0] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[1] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[2] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[3] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[4] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        

# correct letter incorrect placement

        if user_word[0] != word[0] and user_word[0] in word:
           game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
           pygame.display.update()
        if user_word[1] != word[1] and user_word[1] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[2] != word[2] and user_word[2] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[3] != word[3] and user_word[3] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[4] != word[4] and user_word[4] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()


# correct letter and placement

        if user_word[0] == word[0]:
           game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
           pygame.display.update()
        if user_word[1] == word[1]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[2] == word[2]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[3] == word[3]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()
        if user_word[4] == word[4]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
            pygame.display.update()


        letter1 = font.render(user_word[0], True, black, None)
        letter_rect1 = letter1.get_rect(center = (screen_width / 4.77 , screen_height / 3.8 + (counter - 1) * 72))
        screen.blit(letter1, letter_rect1)
        pygame.display.update()

        letter2 = font.render(user_word[1], True, black, None)
        letter_rect2 = letter2.get_rect(center = (screen_width / 2.9 , screen_height / 3.8 + (counter - 1) * 72))
        screen.blit(letter2, letter_rect2)
        pygame.display.update()

        letter3 = font.render(user_word[2], True, black, None)
        letter_rect3 = letter3.get_rect(center = (screen_width / 2 , screen_height / 3.8 + (counter - 1) * 72))
        screen.blit(letter3, letter_rect3)
        pygame.display.update()

        letter4 = font.render(user_word[3], True, black, None)
        letter_rect4 = letter4.get_rect(center = (screen_width / 1.53 , screen_height / 3.8 + (counter - 1) * 72))
        screen.blit(letter4, letter_rect4)
        pygame.display.update()

        letter5 = font.render(user_word[4], True, black, None)
        letter_rect5 = letter5.get_rect(center = (screen_width / 1.25 , screen_height / 3.8 + (counter - 1) * 72))
        screen.blit(letter5, letter_rect5)
        pygame.display.update()


        if user_word == word:
                game.quit_game()
                return False
                 

        return True



pygame.display.update()




counter = 0     

playing = True
game = BoxRow()
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
            exit()
    counter += 1
    if counter < 7:
        print(counter)
        playing = play_game(game)

    if counter == 6:
            print('game over')
            game.out_of_tries()
            print(word)
            pygame.quit()
            playing = False

