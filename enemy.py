import pygame
import random
SCREEN_SIZE = [800, 1000]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.hp = level
        self.movement = 0
        self.attack_clock = 0

        self.image = pygame.image.load("enemies/enemy" + str(level) + ".png")
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, SCREEN_SIZE[0] - 50)
        self.rect.top = 0

class Enemy1(Enemy):
    def __init__(self, level):
        super().__init__(level)
    
    def move(self):
        self.attack_clock = -1
        if self.movement % 50 == 0:
            self.rect.bottom = self.rect.bottom + 1
        self.movement = self.movement + 2


class Enemy2(Enemy):
    def __init__(self, level):
        super().__init__(level)

    def move(self):
        if self.movement % 10 == 0:
            if random.randint(0,1) == 0:
                self.rect.left = max(self.rect.left - 1, 0)
            else:
                self.rect.right = min(self.rect.right + 1, SCREEN_SIZE[0])

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, Enemy):
        super().__init__()
        self.movement = 0
        self.bullet_image = pygame.image.load("enemies/bullet2.png")
        self.bullet_image = pygame.transform.rotate(self.bullet_image, -90)
        self.bullet_image = pygame.transform.scale(self.bullet_image, (10, 10))
        self.bullet_rect = self.bullet_image.get_rect()
        self.bullet_rect.x = (Enemy.rect.left + Enemy.rect.right) / 2
        self.bullet_rect.y = Enemy.rect.bottom

    def move(self):
        if self.movement == 0:
            self.bullet_rect.y = self.bullet_rect.y + 1
        self.movement = self.movement + 1
        if self.movement >= 10:
            self.movement = 0


