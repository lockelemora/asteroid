import pygame
import sys
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    
    clock = pygame.time.Clock()
    dt = 0
    asteroidfield = AsteroidField()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        
        for obj in updatable:
            obj.update(dt)
        
        for ast in asteroids:
            for sht in shots:
                if sht.collision_check(ast):
                    sht.kill()
                    ast.split()
            if ast.collision_check(player):
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()