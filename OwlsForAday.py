import pygame

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the game window
pygame.display.set_caption("Pong")

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If user clicked close, then exit
            pygame.quit()
            quit()

    # Clear the screen to white
    screen.fill(WHITE)

    # Draw the ball and paddles
    pygame.draw.rect(screen, BLACK, [50, 50, 10, 10])
    pygame.draw.rect(screen, BLACK, [350, 50, 10, 60])
    pygame.draw.rect(screen, BLACK, [40, 120, 10, 60])
    pygame.draw.rect(screen, BLACK, [350, 190, 10, 60])

    # Update the screen
    pygame.display.flip()
