import pygame
import random
import time

# Initialize window
pygame.init()
width = 800
height = 600
black = (0, 0, 0)

# Setting game display size
game_display = pygame.display.set_mode((width, height))

# Scale image size
background = pygame.image.load("keyback.jpg")
background = pygame.transform.scale(background, (width, height))

font = pygame.font.Font("comic.ttf", 40)

# Define functions
word_speed = 0.5
score = 0


def new_word():
    global x_cor, y_cor, text, word_speed, your_word, display_word
    x_cor = random.randint(300, 700)
    y_cor = 200
    word_speed += 0.1
    your_word = ""
    words = open("words.txt").read().split(", ")
    display_word = random.choice(words)


new_word()

font_name = pygame.font.match_font("comic.ttf")


def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    game_display.blit(text_surface, text_rect)


def game_front_screen():
    game_display.blit(background, (0, 0))
    if not game_over:
        draw_text(game_display, "GAME OVER!", 90, width/2, height/4)
        draw_text(game_display, "Score : " + str(score), 70, width/2, height/2)
    else:
        draw_text(game_display, "Press any key to begin!", 54, width/2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Main loop
game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

    background = pygame.image.load("teacher-background.jpg")
    background = pygame.transform.scale(background, (width, height))
    character = pygame.image.load("char.jpg")
    character = pygame.transform.scale(character, (50, 50))
    wood = pygame.image.load("wood-.png")
    wood = pygame.transform.scale(wood, (90, 50))
    game_display.blit(background, (0, 0))
    game_display.blit(wood, (x_cor-50, y_cor+15))
    game_display.blit(character, (x_cor-100, y_cor))
    draw_text(game_display, str(display_word), 40, x_cor, y_cor)
    draw_text(game_display, "Score:" + str(score), 40, width/2, 5)

    y_cor += word_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            your_word += pygame.key.name(event.key)

            if display_word.startswith(your_word):
                if display_word == your_word:
                    score += len(display_word)
                    new_word()
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()

    if y_cor < height - 5:
        pygame.display.update()
    else:
        game_front_screen()
