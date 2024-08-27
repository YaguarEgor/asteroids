import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot

def main():
    print("Starting asteroids!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (shoots, updatable, drawable)
    
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    
    clock = pygame.time.Clock()
    dt = 0

    
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
        
        for ast in asteroids:
            if ast.detect_collsision(player):
                print("Game over!")
                return
            for bul in shoots:
                if ast.detect_collsision(bul):
                    ast.split()
                    bul.kill()

            
        screen.fill(BLACK)
        
        for obj in drawable:
            obj.draw(screen)
            
            
        pygame.display.flip()  
        dt = clock.tick(60) / 1000

        
        
        
       



    
if __name__ == "__main__":
    main()