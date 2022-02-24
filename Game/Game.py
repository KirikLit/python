import pygame

pygame.init()

win = pygame.display.set_mode(size=(720,480))

pygame.display.set_caption('MyGame')

player = pygame.image.load('Sprite-0001.png')
bg = pygame.image.load('Sprite-0002.png')

clock = pygame.time.Clock()
FPS = 60

x = 50
y = 50
width = 36
height = 80
speed = 5
jumpCount = 10
isJump = False

def jump():
    global x, y, jumpCount, isJump

    isJump = True
    while isJump:
        if jumpCount >= 0:
            y += (jumpCount // 2) ** 2
            jumpCount -= 1
        elif jumpCount > -10:
            y -= (jumpCount // 2) ** 2
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

def controls():
    global x, y, speed, jumpCount, isJump

    key = pygame.key.get_pressed()

    if key[pygame.K_w] and y > 5:
         y -= speed
    if key[pygame.K_s] and y < 480 - height - 5:
        y += speed
    if key[pygame.K_a] and x > 5:
        x -= speed
    if key[pygame.K_d] and x < 720 - width - 5:
        x += speed
    if key[pygame.K_SPACE]:
        jump()

def graphics():
    global y, x, width, height
    win.blit(bg, (0, 0))
    win.blit(player, (x, y))
    pygame.display.update()
    win.fill((0, 0, 0))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
    controls()
    graphics()