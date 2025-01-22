import pygame
import time

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1000, 100))
pygame.display.set_caption("Image Display")

# Load images
one_m_image_path = "1m.png"
two_m_image_path = "2m.png"

one_image = pygame.image.load(one_m_image_path )
two_image = pygame.image.load(two_m_image_path)

def mone():
    screen.blit(one_image, (0, 0))
    pygame.display.flip()

def mtwo():
    screen.blit(two_image, (0, 0))
    pygame.display.flip()

def mouth():
    while True:
        mone()
        time.sleep(1)
        mtwo()
        time.sleep(1)

# Run the script
mouth()
