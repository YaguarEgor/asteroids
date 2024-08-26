import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    
    clock = pygame.time.Clock()
    dt = 0

    
    while True: 
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill(BLACK)
        
        player.update(dt)
        
        
        player.draw(screen)
        pygame.display.flip()
       



    
if __name__ == "__main__":
    main()