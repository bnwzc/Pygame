import pygame
from player import Jet
from player import Bullet
from enemy import Enemy
from enemy import Enemy1
from enemy import Enemy2
from enemy import Bullet2
import time


def main():
    pygame.init()
    pygame.display.set_caption('Air Fighter')
    win = pygame.display.set_mode((800, 1000))

    # Load the Background
    img_surf = pygame.image.load("background/background.jpg").convert()
    img_surf = pygame.transform.rotate(img_surf, 90)
    img_surf = pygame.transform.scale(img_surf, (800, 1000))

    # Loading the material
    player = Jet()
    bullets = pygame.sprite.Group()
    bullets_produce = 0
    enemies = pygame.sprite.Group()
    enemies_produce = 0
    enemy_bullets = pygame.sprite.Group()

    # Start the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Loading the player jet
        win.blit(img_surf, (0,0))
        win.blit(player.image, player.rect)
        player.move()

        # Attack!
        if bullets_produce == 0:
            bullets.add(Bullet("machine_gun", player))
        for bullet in bullets:
            hitted_enemies = pygame.sprite.spritecollide(bullet, enemies, dokill=False)
            if pygame.sprite.spritecollide(bullet, enemies, dokill=False):
                bullets.remove(bullet)
            for enemy in hitted_enemies:
                enemy.hp = enemy.hp - 1
            win.blit(bullet.image, bullet.rect)
            bullet.move()
        bullets_produce = bullets_produce + player.attack_speed
        if bullets_produce > 3000:
            bullets_produce = 0
        
        # Warning! Enemies!
        if enemies_produce == 50:
            enemies.add(Enemy1(1))
        if enemies_produce == 100:
            enemies.add(Enemy2(2))
        for enemy in enemies:
            enemy.move()
            if enemy.hp <= 0:
                enemies.remove(enemy)
            win.blit(enemy.image, enemy.rect)
        enemies_produce = enemies_produce + 1
        if enemies_produce > 5000:
            enemies_produce = 0

        # Enemies Attack!
        for enemy in enemies:
            if enemy.attack_clock == 0:
                enemy_bullets.add(Bullet2(enemy))
            enemy.attack_clock = enemy.attack_clock + enemy.level
            if enemy.attack_clock > 3000:
                enemy.attack_clock = 0
        
        # Enemies bullets!
        for bullet in enemy_bullets:
            win.blit(bullet.bullet_image, bullet.bullet_rect)
            bullet.move()

        pygame.display.flip()

main()
