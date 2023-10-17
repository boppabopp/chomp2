import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))

puffer_fish = pygame.image.load('images\puffer_fish.png')


background.fill((52, 140, 235))
sand_height = 100
pygame.draw.rect(background, (250, 192, 85), (0, HEIGHT-sand_height, WIDTH, sand_height))

screen.blit(background, (0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(puffer_fish, (400,300))

    pygame.display.flip()

