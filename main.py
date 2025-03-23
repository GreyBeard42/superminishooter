from classes import Bullet
from classes import Enemy

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((20, 30))
pygame.display.set_caption("Super Mini Shooter")
clock = pygame.time.Clock()
print("\nThe games have begun!\n\n---")
framecount = 0

def pixel(x,y):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 1, 1))

gameover = False
# player
p = pygame.Rect(10, 27, 1, 1)
# bullets
bs = []
bclock = 0
# enemies
es = []
es.append(Enemy(pygame.Rect(2, 2, 1, 1)))
es.append(Enemy(pygame.Rect(6, 2, 1, 1)))
es.append(Enemy(pygame.Rect(10, 2, 1, 1)))
es.append(Enemy(pygame.Rect(14, 2, 1, 1)))
es.append(Enemy(pygame.Rect(18, 2, 1, 1)))

es.append(Enemy(pygame.Rect(4, 5, 1, 1)))
es.append(Enemy(pygame.Rect(8, 5, 1, 1)))
es.append(Enemy(pygame.Rect(12, 5, 1, 1)))
es.append(Enemy(pygame.Rect(16, 5, 1, 1)))
lastmove = pygame.time.get_ticks()
movedelay = 750

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nBye for now!\n\n---")
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    #player
    pygame.draw.rect(screen, (255, 0, 255), (p.centerx-2, p.centery, 1, 1))
    pygame.draw.rect(screen, (255, 0, 255), (p.centerx-1, p.centery, 1, 1))
    pygame.draw.rect(screen, (255, 0, 255), (p.centerx, p.centery, 1, 1))
    pygame.draw.rect(screen, (255, 0, 255), (p.centerx+1, p.centery, 1, 1))
    pygame.draw.rect(screen, (255, 0, 255), (p.centerx+2, p.centery, 1, 1))
    pygame.draw.rect(screen, (255, 0, 255), (p.centerx, p.centery-1, 1, 1))

    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p.centerx -= 1
        if keys[pygame.K_RIGHT]:
            p.centerx += 1
        
        if p.centerx < 2: p.centerx = 2
        if p.centerx > 18: p.centerx = 18

        # bullets
        if bclock > 0: bclock -= 1
        if keys[pygame.K_SPACE] and bclock == 0:
            bs.append(Bullet(pygame.Rect(p.centerx, p.centery-2, 1, 1), -1))
            bclock = 5
        
        for b in bs:
            pygame.draw.rect(screen, (0, 0, 255), (b.rect.centerx, b.rect.centery, 1, 1))
            b.rect.centery += b.v
        for b in bs:
            if b.rect.centery < 0: bs.remove(b)
        
        # enemies
        now = pygame.time.get_ticks()
        move = now - lastmove > movedelay
        if move: lastmove = now
        for e in es:
            pygame.draw.rect(screen, (0, 255, 0), (e.rect.centerx-1, e.sy, 1, 1))
            pygame.draw.rect(screen, (0, 255, 0), (e.rect.centerx, e.my, 1, 1))
            pygame.draw.rect(screen, (0, 255, 0), (e.rect.centerx+1, e.sy, 1, 1))
            kill = False
            for b in bs:
                if (b.rect.centerx == e.rect.centerx-1 and b.rect.centery == e.sy) or (b.rect.centerx == e.rect.centerx and b.rect.centery == e.my) or (b.rect.centerx == e.rect.centerx+1 and b.rect.centery == e.sy):
                    kill = True
            if kill:
                e.alive = False
                bs.remove(b)
            if e.sy == 28 or e.my == 28:
                gameover = True
            if move: e.move()
        for e in es:
            if not e.alive: es.remove(e)
        if len(es) == 0:
            movedelay -= 50
            es.append(Enemy(pygame.Rect(2, -4, 1, 1)))
            es.append(Enemy(pygame.Rect(6, -4, 1, 1)))
            es.append(Enemy(pygame.Rect(10, -4, 1, 1)))
            es.append(Enemy(pygame.Rect(14, -4, 1, 1)))
            es.append(Enemy(pygame.Rect(18, -4, 1, 1)))

            es.append(Enemy(pygame.Rect(4, -1, 1, 1)))
            es.append(Enemy(pygame.Rect(8, -1, 1, 1)))
            es.append(Enemy(pygame.Rect(12, -1, 1, 1)))
            es.append(Enemy(pygame.Rect(16, -1, 1, 1)))
    else:
        # G
        pixel(4,5)
        pixel(3,5)
        pixel(2,5)
        pixel(2,6)
        pixel(2,7)
        pixel(2,8)
        pixel(2,9)
        pixel(2,10)
        pixel(3,10)
        pixel(4,10)
        pixel(4,9)
        pixel(4,8)
        # A
        pixel(6, 5)
        pixel(6, 6)
        pixel(6, 7)
        pixel(6, 8)
        pixel(6, 9)
        pixel(6, 10)
        pixel(7, 5)
        pixel(7, 7)
        pixel(8, 5)
        pixel(8, 6)
        pixel(8, 7)
        pixel(8, 8)
        pixel(8, 9)
        pixel(8, 10)
        # M
        pixel(10, 5)
        pixel(10, 6)
        pixel(10, 7)
        pixel(10, 8)
        pixel(10, 9)
        pixel(10, 10)
        pixel(11, 6)
        pixel(12, 7)
        pixel(12, 8)
        pixel(13, 6)
        pixel(14, 5)
        pixel(14, 6)
        pixel(14, 7)
        pixel(14, 8)
        pixel(14, 9)
        pixel(14, 10)
        # E
        pixel(16, 5)
        pixel(17, 5)
        pixel(18, 5)
        pixel(16, 6)
        pixel(16, 7)
        pixel(17, 7)
        pixel(16, 8)
        pixel(16, 9)
        pixel(16, 10)
        pixel(17, 10)
        pixel(18, 10)

        # O
        pixel(2,12)
        pixel(3,12)
        pixel(3,17)
        pixel(2,13)
        pixel(2,14)
        pixel(2,15)
        pixel(2,16)
        pixel(2,17)
        pixel(4,12)
        pixel(4,13)
        pixel(4,14)
        pixel(4,15)
        pixel(4,16)
        pixel(4,17)
        # V
        pixel(6,12)
        pixel(6,13)
        pixel(7,14)
        pixel(7,15)
        pixel(8,16)
        pixel(9,14)
        pixel(9,15)
        pixel(10,12)
        pixel(10,13)
        # E
        pixel(12,12)
        pixel(13,12)
        pixel(14,12)
        pixel(12,13)
        pixel(12,14)
        pixel(13,14)
        pixel(12,15)
        pixel(12,16)
        pixel(12,17)
        pixel(13,17)
        pixel(14,17)
        # R
        pixel(16,12)
        pixel(17,12)
        pixel(18,12)
        pixel(16,13)
        pixel(18,13)
        pixel(16,14)
        pixel(17,14)
        pixel(18,14)
        pixel(16,15)
        pixel(17,15)
        pixel(16,16)
        pixel(18,16)

    pygame.display.flip()
    clock.tick(15)
    framecount += 1
