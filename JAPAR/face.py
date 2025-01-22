import pygame
import time

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((750, 1500))
pygame.display.set_caption("Image Display")

# Load images
face_image_path = "face.png"
eye_close_image_path = "eye_close.png"

face_image = pygame.image.load(face_image_path)
eye_close_image = pygame.image.load(eye_close_image_path)

def show_face():
    screen.blit(face_image, (0, 0))
    pygame.display.flip()

def show_eye_close():
    screen.blit(eye_close_image, (0, 0))
    pygame.display.flip()

def repeat_face_and_eye_close():
    while True:
        show_face()
        time.sleep(1)
        show_eye_close()
        time.sleep(1)

# Run the script
repeat_face_and_eye_close()
    