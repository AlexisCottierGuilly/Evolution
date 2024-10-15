import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

# Button Class
class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buttonText = buttonText
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.state = 'normal'  # Button state: 'normal', 'hover', or 'pressed'

    def draw(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if the mouse is over the button
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            self.state = 'hover'
        else:
            self.state = 'normal'

        # Draw the button
        if self.state == 'normal':
            pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, self.width, self.height))
        elif self.state == 'hover':
            pygame.draw.rect(screen, (150, 150, 150), (self.x, self.y, self.width, self.height))
        elif self.state == 'pressed':
            pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height))

        # Draw button text
        text_surface = font.render(self.buttonText, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.state == 'hover':
                self.state = 'pressed'
                if self.onclickFunction:
                    self.onclickFunction()
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.state == 'pressed':
                self.state = 'hover'
                if not self.onePress:
                    self.onclickFunction()

'''
# Example usage
def my_custom_function():
    print("Button clicked!")

start_button = Button(200, 200, 150, 50, 'Start', onclickFunction=my_custom_function)
objects = [start_button]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for obj in objects:
            obj.handle_event(event)

    screen.fill((0, 0, 0))
    for obj in objects:
        obj.draw(screen)

    pygame.display.flip()
    fpsClock.tick(fps)
'''
