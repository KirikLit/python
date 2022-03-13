import pygame
import random


# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.transform.scale(ship, (50, 38))

        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        
        self.speedx = 0

    def update(self):
        key = pygame.key.get_pressed()
        # Check Controls
        self.speedx = 0                     # Reset speed

        if key[pygame.K_a]:                 # Check key A
            self.speedx -= SPEED
        if key[pygame.K_d]:
            self.speedx += SPEED            # Check key D

        self.rect.x += self.speedx          # Move

        if self.rect.right > WIDTH:         # Защита от выхода за экран
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


# Make enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = random.choice(met_img )
        self.image_orig = self.image

        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.rect.right = random.randint(0 + self.rect.width, WIDTH)
        self.rect.top = random.randint(-100, 0)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

        # Set moving speed
        self.speedx = random.randint(-4, 4) / 2
        self.speedy = random.randint(2, 6)

    def update(self):
        # Move sprite
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rotate()

        if self.rect.right > WIDTH:         # Защита от выхода за экран по горизонтали
            self.speedx = random.randint(-4, 1) / 2
        elif self.rect.left < 0:
            self.speedx = random.randint(1, 4) / 2

        if self.rect.top > HEIGHT:       # Защита от выхода за экран по вертикали
            b = Enemy()
            all_sprites.add(b)
            mobs.add(b)
            self.kill()
        elif self.rect.top < 0:
            self.rect.top = 0

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            old_center = self.rect.center
            self.image = pygame.transform.rotate(self.image_orig, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = old_center


# Bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        # Making bullet
        self.image = laser

        self.rect = self.image.get_rect()
        self.rect.bottom = posy
        self.rect.centerx = posx
        
        self.speedy = -10

    def update(self):
        # Move
        self.rect.y += self.speedy

        # Защита от выхода за экран
        if self.rect.bottom < 0:
            self.kill()


if __name__ == '__main__':
    # Colors (R, G, B)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Settings
    WIDTH = 480
    HEIGHT = 600
    FPS = 60
    SPEED = 8

    # Load graphics
    background = pygame.image.load('Assets\\back.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    ship = pygame.image.load('Assets\\ship.png')
    laser = pygame.image.load('Assets\\laser.png')

    meteors = ['big1', 'big2', 'big3', 'big4', 'med1', 'small1', 'small2', 'tiny1', 'tiny2']
    met_img = []
    for met in meteors:
        mtr = pygame.image.load('Meteors\\meteorGrey_%s.png' % met)
        met_img.append(mtr)

    # Sprites
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # Spawn enemies
    for x in range(8):
        mob = Enemy()
        all_sprites.add(mob)
        mobs.add(mob)

    # Init game
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Strelyalka1")
    clock = pygame.time.Clock()
    run = True

    # Main Cycle
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():    # Check quit
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Check collide
        hitp = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        hite = pygame.sprite.groupcollide(mobs, bullets, True, True)

        if hitp:
            run = False
        for x in hite:
            m = Enemy()
            all_sprites.add(m)
            mobs.add(m)

        # Render
        all_sprites.update()                # Sprite update
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()

    # Quit the game
    pygame.quit()
