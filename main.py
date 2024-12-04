import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to manage the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate a Player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)
        # fill the screen with black        
        screen.fill((0, 0, 0))

        player.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        # Pause the game loop to maintain 60 FPS and get the delta time
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()