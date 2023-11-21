import pygame
import time
SCREEN_SIZE = [800, 1000]
weapons = ["machine_gun", "missile", "laser"]

class Jet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player/plane.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_SIZE[0] / 2 - 50
        self.rect.bottom = SCREEN_SIZE[1]
        
        self.weapons = "machine_gun"
        self.hp = 3
        self.speed = 1
        self.attack_speed = 1
        self.damage = 1
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # pygame.time.delay(10)
            # time.sleep(0.015)
            self.rect.left = max(self.rect.left - self.speed, 0)
        elif keys[pygame.K_RIGHT]:
            # pygame.time.delay(10)
            # time.sleep(0.015)
            self.rect.right = min(self.rect.right + self.speed, SCREEN_SIZE[0])
        elif keys[pygame.K_UP]:
            # pygame.time.delay(10)
            # time.sleep(0.015)
            self.rect.top = max(self.rect.top - self.speed, 0)
        elif keys[pygame.K_DOWN]:
            # pygame.time.delay(10)
            # time.sleep(0.015)
            self.rect.bottom = min(self.rect.bottom + self.speed, SCREEN_SIZE[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, weapon, jet):
        super().__init__()
        self.weapon = weapon
        self.image = pygame.image.load("weapons/" + self.weapon + ".png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.bottom = jet.rect.top
        self.rect.left = (jet.rect.left + jet.rect.right) / 2 - 5
        

    def move(self):
        if self.rect.bottom > 0:
            self.rect.bottom = self.rect.bottom - 1




