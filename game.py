import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Window")

white = (255, 255, 255)
blue = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)
    pygame.draw.rect(screen, blue, (screen_width // 2 - 50, screen_height // 2 - 25, 100, 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
