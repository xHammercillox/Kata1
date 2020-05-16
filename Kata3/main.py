import pygame

screen_width = 1280
screen_heigth = 960

# Colors
white_color = (200, 200, 200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set.mode((screen_width, screen_heigth))

def mover_rectangulo():
    global speed

    if rectangulo.top + 50 < screen_heigth:
        rectangulo.top +=3

def mover_bola():

    if bola.top + 50 > screen_heigth:
        speed_bola_x =  -speed_bola_x

    bola.top += speed_bola_x
    bola.left += speed_bola_y


rectangulo = pygame.Rect(10, 10, 50, 50)
bola = pygame.Rect(50, 10, 50, 50)

speed = 0
speed_bola_x = 3
speed_bola_y = 3

while True:
    screen.fill(back_color)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3
            elif event.key == pygame.K_DOWN:
                speed = -3 
        elif event.type = 0


    pygame.draw.Rect(screen, white_color, rectangulo)
    pygame.draw.ellipse(screen, white_color, bola)

    pygame.display.flip()
    clock.tick(60)