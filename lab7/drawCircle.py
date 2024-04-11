import pygame
 
 # Import pygame.locals for easier access to key coordinates
 from pygame.locals import (
     K_UP,
     K_DOWN,
     K_LEFT,
     K_RIGHT,
     K_ESCAPE,
     KEYDOWN,
     QUIT,
 )
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True


# Main loop
while running:
     for event in pygame.event.get():
         # Did the user hit a key?
         if event.type == KEYDOWN:
             # Was it the Escape key? If so, stop the loop.
             if event.key == K_ESCAPE:
                 running = False
 
        # Did the user click the window close button? If so, stop the loop.
         elif event.type == QUIT:
             running = False

# Fill the screen with white
screen.fill((255, 255, 255))
surf = pygame.Surface((50, 50))
# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()


surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)
# Draw surf at the new coordinates
screen.blit(surf, surf_center)
pygame.display.flip()


def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -20)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 20)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-20, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(20, 0)
    # Keep player on the screen
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT


# Define a Player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()