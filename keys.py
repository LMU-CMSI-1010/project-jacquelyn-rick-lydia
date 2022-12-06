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