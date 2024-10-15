import pygame
from button import Button

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode(*size)

pygame.display.set_caption("Evolution")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def quit():
    global done
    done = True


quit_button = Button(
    round(size[0] * 0.9), 200,
    150, 50,
    'X',
    onclickFunction=quit)

buttons = [quit_button]

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        for button in buttons:
            button.handle_event(event)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    for button in buttons:
        button.draw(screen)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
