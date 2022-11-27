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

   def draw(self, surface):
       text = self.letter
       font = pygame.font.SysFont("arial", 16)
       text = font.render(text, True, self.color)
       surface.blit(text, (0,0))