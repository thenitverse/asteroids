import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        

    def draw(self, screen):
        draw= pygame.draw.circle(surface=screen,color="white",center=(self.position.x,self.position.y),radius=(self.radius),width=(LINE_WIDTH))
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            
            return
        else:
            log_event("asteroid_split")
            random_angle =random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid1.velocity = self.velocity.rotate(random_angle)*1.2
            new_asteroid2.velocity = self.velocity.rotate(-random_angle)*1.2
            




