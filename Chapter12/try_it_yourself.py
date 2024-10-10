import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Rocket Game")

# Define colors
blue_color = (135, 206, 235)

# Load the rocket image (ensure the image is in the same directory)
rocket_image = pygame.image.load("./Chapter12/images/ship.bmp")

# Get the rectangle of the rocket
rocket_rect = rocket_image.get_rect()

# Start the rocket in the center of the screen
rocket_rect.center = (screen_width // 2, screen_height // 2)

# Define movement variables
rocket_speed = 5
moving_right = False
moving_left = False
moving_up = False
moving_down = False

# Main loop
while True:
    # Handle events (such as closing the window and key presses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
                print(f"Key pressed: {event.key}")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
                print(f"Key released: {event.key}")

    # Move the rocket
    if moving_right and rocket_rect.right < screen_width:
        rocket_rect.x += rocket_speed
    if moving_left and rocket_rect.left > 0:
        rocket_rect.x -= rocket_speed
    if moving_up and rocket_rect.top > 0:
        rocket_rect.y -= rocket_speed
    if moving_down and rocket_rect.bottom < screen_height:
        rocket_rect.y += rocket_speed

    # Fill the screen with blue
    screen.fill(blue_color)

    # Draw the rocket on the screen
    screen.blit(rocket_image, rocket_rect)

    # Update the display
    pygame.display.update()
