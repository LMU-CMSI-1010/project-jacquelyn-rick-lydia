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



counter = 0
while True:

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                playing = False
                exit()

        if counter < 6:
            counter += 1
            pygame.draw.rect(screen, dark_gray, pygame.Rect((screen_width * 0.5), (screen_height * 0.05) + counter * 80, box_width, box_height), 0)
            print(counter)

        elif counter == 6:
            counter += 1
            print(counter)
            pygame.draw.rect(screen, green, pygame.Rect((screen_width * 0.5), (screen_height * 0.05) + counter * 80, box_width, box_height), 0)



        pygame.display.update()
        pygame.time.delay(4000)
        if counter == 7:
            break

