import pygame
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
        self.firstrow()
        self.secondrow()
        self.thirdrow()
        self.fourthrow()
        self.fifthrow()

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



# BoxRow.firstrow()
# BoxRow.secondrow()
# BoxRow.thirdrow()
# BoxRow.fourthrow()
# BoxRow.fifthrow()


print(word)

# Loop that keeps the game open until the user quits

user_word = ''

def play_game(game):
    user_word = input('what is your guess? ')
    if user_word == 'q':
        return False
    elif len(user_word) != 5 or type(user_word) != str:
        print('guess must be a five letter word')
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
        letter_rect1 = letter1.get_rect(center = (screen_width / 4.77 , screen_height / 4 + (counter - 1) * 73))
        screen.blit(letter1, letter_rect1)

        letter2 = font.render(user_word[1], True, black, None)
        letter_rect2 = letter2.get_rect(center = (screen_width / 2.9 , screen_height / 4 + (counter - 1) * 73))
        screen.blit(letter2, letter_rect2)

        letter3 = font.render(user_word[2], True, black, None)
        letter_rect3 = letter3.get_rect(center = (screen_width / 2 , screen_height / 4 + (counter - 1) * 73))
        screen.blit(letter3, letter_rect3)

        letter4 = font.render(user_word[3], True, black, None)
        letter_rect4 = letter4.get_rect(center = (screen_width / 1.53 , screen_height / 4 + (counter - 1) * 73))
        screen.blit(letter4, letter_rect4)

        letter5 = font.render(user_word[4], True, black, None)
        letter_rect5 = letter5.get_rect(center = (screen_width / 1.25 , screen_height / 4 + (counter - 1) * 73))
        screen.blit(letter5, letter_rect5)

        
        pygame.display.update()

    return True


    import pygame

pygame.init()

pygame.display.set_caption('Keyboard')

screen_width = 800
screen_height = 500

box_width = screen_width / 17
box_height = screen_height / 10

white = (255, 255, 255)
light_gray = (200, 200, 200)
black = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)

font = pygame.font.SysFont('arial', 26)


class Keyboard:
    def __init__(self):
       self.keys = []

    def add_key(self, key):
       self.keys.append(key)

    def get_key(self, letter):
       for key in self.keys:
           if key.letter == letter:
               return key
       return None

    def draw(self, surface):
       for key in self.keys:
           key.draw(surface)


            


class Key:
    def __init__(self, letter, color):
       self.letter = letter
       self.color = color

    def draw(self, position_x, position_y, is_large=False):
        text = self.letter
        key = font.render(text, True, self.color, None)
        box = ''
        if is_large:
            box = pygame.Rect(position_x, position_y, box_width + 30, box_height)
        else:
            box = pygame.Rect(position_x, position_y, box_width, box_height)
        
        pygame.draw.rect(screen, light_gray, box)
        screen.blit(key, (position_x + 13, position_y + 10))
        pygame.display.update()

  '''def turn_green():
        if 'a' in word:
            A = Key('A', green)'''

# draw top line
top_line_height = (screen_height * 0.4)
Q = Key('Q', white)
Q.draw((screen_width / 8 + (screen_width / 15) * 1 - (box_width / 2)), top_line_height)
W = Key('W', white)
W.draw((screen_width / 8 + (screen_width / 15) * 2 - (box_width / 2)), top_line_height)
E = Key('E', white)
E.draw((screen_width / 8 + (screen_width / 15) * 3 - (box_width / 2)), top_line_height)
R = Key('R', white)
R.draw((screen_width / 8 + (screen_width / 15) * 4 - (box_width / 2)), top_line_height)
T = Key('T', white)
T.draw((screen_width / 8 + (screen_width / 15) * 5 - (box_width / 2)), top_line_height)
Y = Key('Y', white)
Y.draw((screen_width / 8 + (screen_width / 15) * 6 - (box_width / 2)), top_line_height)
U = Key('U', white)
U.draw((screen_width / 8 + (screen_width / 15) * 7 - (box_width / 2)), top_line_height)
I = Key('I', white)
I.draw((screen_width / 8 + (screen_width / 15) * 8 - (box_width / 2)), top_line_height)
O = Key('O', white)
O.draw((screen_width / 8 + (screen_width / 15) * 9 - (box_width / 2)), top_line_height)
P = Key('P', white)
P.draw((screen_width / 8 + (screen_width / 15) * 10 - (box_width / 2)), top_line_height)

# draw second line
second_line_height = (screen_height * 0.4) + box_height + 5
A = Key('A', white)
A.draw((screen_width / 8 + (screen_width / 15) * 1.6 - (box_width / 2)), second_line_height)
S = Key('S', white)
S.draw((screen_width / 8 + (screen_width / 15) * 2.6 - (box_width / 2)), second_line_height)
D = Key('D', white)
D.draw((screen_width / 8 + (screen_width / 15) * 3.6 - (box_width / 2)), second_line_height)
F = Key('F', white)
F.draw((screen_width / 8 + (screen_width / 15) * 4.6 - (box_width / 2)), second_line_height)
G = Key('G', white)
G.draw((screen_width / 8 + (screen_width / 15) * 5.6 - (box_width / 2)), second_line_height)
H = Key('H', white)
H.draw((screen_width / 8 + (screen_width / 15) * 6.6 - (box_width / 2)), second_line_height)
J = Key('J', white)
J.draw((screen_width / 8 + (screen_width / 15) * 7.6 - (box_width / 2)), second_line_height)
K = Key('K', white)
K.draw((screen_width / 8 + (screen_width / 15) * 8.6 - (box_width / 2)), second_line_height)
L = Key('L', white)
L.draw((screen_width / 8 + (screen_width / 15) * 9.6 - (box_width / 2)), second_line_height)

# draw bottom line
bottom_line_height = (screen_height * 0.4) + (2 * box_height) + 10
Enter = Key('Enter', white)
Enter.draw((screen_width / 8 + (screen_width / 15) * 1 - (box_width / 2)), bottom_line_height, True)
Z = Key('Z', white)
Z.draw((screen_width / 8 + (screen_width / 15) * 2 - (box_width / 2)) + 30, bottom_line_height)
X = Key('X', white)
X.draw((screen_width / 8 + (screen_width / 15) * 3 - (box_width / 2)) + 30, bottom_line_height)
C = Key('C', white)
C.draw((screen_width / 8 + (screen_width / 15) * 4 - (box_width / 2)) + 30, bottom_line_height)
V = Key('V', white)
V.draw((screen_width / 8 + (screen_width / 15) * 5 - (box_width / 2)) + 30, bottom_line_height)
B = Key('B', white)
B.draw((screen_width / 8 + (screen_width / 15) * 6 - (box_width / 2)) + 30, bottom_line_height)
N = Key('N', white)
N.draw((screen_width / 8 + (screen_width / 15) * 7 - (box_width / 2)) + 30, bottom_line_height)
M = Key('M', white)
M.draw((screen_width / 8 + (screen_width / 15) * 8 - (box_width / 2)) + 30, bottom_line_height)
Backspace = Key('<--', white)
Backspace.draw((screen_width / 8 + (screen_width / 15) * 9 - (box_width / 2)) + 30, bottom_line_height, True)



pygame.display.update()

playing = True
while playing: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # if (mouse[0], mouse[1]) is inside one of the keys then add the letter
            print('clicked')


counter = 0     

playing = True
game = BoxRow()
while playing:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
    print(counter)
    play_game(game)
    pygame.time.delay(20)

    if user_word == word:
        counter = 5

    if counter == 5:
        print('game over')
        pygame.time.delay(20)
        playing = False
        pygame.quit()
