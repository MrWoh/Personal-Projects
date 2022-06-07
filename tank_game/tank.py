# Game Skeleton
import pygame
from random import randint
from itertools import repeat

# Settings from settings.py
from settings import *


# Player
class Player(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, 'tankBase.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH / 2, HEIGHT - 15
        self.speedx = 0
        self.speedy = 0

    # Tank Update/movement
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = +10
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


# Enemy
class Enemy(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, 'tankEnemy.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = randint(200, 600)
        self.rect.y = 100
        self.speed = 10

    def update(self):
        random_left = randint(150, 300)
        random_right = randint(500, 650)
        self.rect.x += self.speed
        if self.rect.left < random_left:
            self.speed = 10
        if self.rect.right > random_right:
            self.speed = -10

    def enemy_shoot(self):
        e_bullet = EnemyBullet(self.rect.centerx, self.rect.top)
        all_sprites.add(e_bullet)
        e_bullets.add(e_bullet)


# Bullet
class Bullet(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, 'bullet.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y  # bullet spawn y
        self.rect.centerx = x  # bullet spawn x
        self.speedy = -10  # bullet speed/movement up

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()  # remove bullet out of bounds


# Enemy bullet
class EnemyBullet(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, 'bullet.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = y  # bullet spawn y
        self.rect.centerx = x  # bullet spawn x
        self.speedy = 10  # bullet speed/movement up

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom == HEIGHT:
            self.kill()  # remove bullet out of bounds


# Game run
pygame.init()
pygame.mixer.init()

# Game display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
copy_screen = screen.copy()
screen_rect = copy_screen.get_rect()
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Sprites
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
e_bullets = pygame.sprite.Group()

# Sprite groups
player = Player()
enemy = Enemy()
all_sprites.add(player, enemy)


# Font function
def txt_object(txt, color, size="small"):
    s_font = pygame.font.SysFont("Times New Roman", 25)
    m_font = pygame.font.SysFont("Times New Roman", 50)
    l_font = pygame.font.SysFont("Times New Roman", 85)
    vs_font = pygame.font.SysFont("Times New Roman", 25)

    if size == "small":
        txt_surface = s_font.render(txt, True, color)
    if size == "medium":
        txt_surface = m_font.render(txt, True, color)
    if size == "large":
        txt_surface = l_font.render(txt, True, color)
    if size == "v_small":
        txt_surface = vs_font.render(txt, True, color)

    return txt_surface, txt_surface.get_rect()


# Button function
def txt_btn(message, color, button_x, button_y, button_width, button_height, size="v_small"):
    txt_surface, text_rect = txt_object(message, color, size)
    text_rect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    screen.blit(txt_surface, text_rect)


# Message function
def msg_screen(message, color, y_displace=0, size="small"):
    txt_surface, text_rect = txt_object(message, color, size)
    text_rect.center = (int(WIDTH / 2), int(HEIGHT / 2) + y_displace)
    screen.blit(txt_surface, text_rect)


# Button click function
def button(txt, x, y, width, height, inactive_color, active_color, action=None, size=" "):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # print(click)
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    txt_btn(txt, BLACK, x, y, width, height)


# Main screen
def game_intro():
    intro_interface = True

    while intro_interface:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro_interface = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        screen.fill(BLACK)
        msg_screen("Welcome to Tanks War!", WHITE, -100, size="medium")
        msg_screen("The goal is to shoot and destroy", WHEAT, 15)
        msg_screen("the enemy tank before they destroy you.", WHEAT, 60)

        button("Play", 150, 300, 100, 50, WHEAT, LIGHT_GREEN, action="play", size="vsmall")
        button("Controls", 350, 300, 100, 50, WHEAT, LIGHT_YELLOW, action="controls", size="vsmall")
        button("Quit", 550, 300, 100, 50, WHEAT, LIGHT_RED, action="quit", size="vsmall")

        pygame.display.update()

        clock.tick(FPS)


# Control menu
def game_controls():
    controls_interface = True

    while controls_interface:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        msg_screen("Controls", WHITE, -100, size="large")
        msg_screen("Fire: Q", WHEAT, -30)
        msg_screen("Enemy Fire: E", WHEAT, 10)
        msg_screen("Move Tank: arrow keys", WHEAT, 50)
        msg_screen("Pause: P", WHEAT, 90)

        button("Play", 150, 300, 100, 50, GREEN, LIGHT_GREEN, action="play")
        button("Main", 350, 300, 100, 50, YELLOW, LIGHT_YELLOW, action="main")
        button("Quit", 550, 300, 100, 50, RED, LIGHT_RED, action="quit")

        pygame.display.update()

        clock.tick(FPS)


# HP bars
def health_bars(p_health, e_health):
    if p_health > 75:
        p_health_color = GREEN
    elif p_health > 50:
        p_health_color = YELLOW
    else:
        p_health_color = RED

    if e_health > 75:
        e_health_color = GREEN
    elif e_health > 50:
        e_health_color = YELLOW
    else:
        e_health_color = RED

    pygame.draw.rect(screen, p_health_color, (680, 25, p_health, 25))
    pygame.draw.rect(screen, e_health_color, (20, 25, e_health, 25))


# End L screen
def game_over():
    game_over_interface = True

    while game_over_interface:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        msg_screen("Game Over", WHITE, -100, size="medium")
        msg_screen("You died.", WHEAT, -30)

        button("Play Again", 150, 300, 150, 50, WHEAT, LIGHT_GREEN, action="play")
        button("Controls", 350, 300, 100, 50, WHEAT, LIGHT_GREEN, action="controls")
        button("Quit", 550, 300, 100, 50, WHEAT, LIGHT_GREEN, action="quit")

        pygame.display.update()

        clock.tick(15)


# End W screen
def you_win():
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        msg_screen("You won!", WHITE, -100, size="medium")
        msg_screen("Congratulations!", WHEAT, -30)

        button("Play Again", 150, 300, 150, 50, WHEAT, LIGHT_GREEN, action="play")
        button("Controls", 350, 300, 100, 50, WHEAT, LIGHT_GREEN, action="controls")
        button("Quit", 550, 300, 100, 50, WHEAT, LIGHT_GREEN, action="quit")

        pygame.display.update()

        clock.tick(FPS)


# Hit screen shake
def shake(intensity, num_of_shakes):
    camera_shake = -1
    for _ in range(num_of_shakes):
        for x in range(0, intensity, 5):
            yield x * camera_shake, 0
        for x in range(intensity, 0, 5):
            yield x * camera_shake, 0
        camera_shake *= -1
    while True:
        yield 0, 0


# Main game_project loop
def gameLoop():
    # variable called before game_project run
    running = True
    p_health = 100
    e_health = 100
    enemy_x = 0
    enemy_y = 0

    # Shake offset variable
    offset = repeat((0, 0))

    # Enemy shooting interval/event timer
    enemy_shoot = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_shoot, randint(300, 600))

    while running:

        # game_project speed
        clock.tick(FPS)

        # Process input (events)
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # player key press event.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    # elif event.key == pygame.K_e:
                #     enemy.enemy_shoot()   
            if event.type == enemy_shoot:
                enemy.enemy_shoot()

        # Update
        all_sprites.update()

        # check collision
        hits = pygame.sprite.spritecollide(enemy, bullets, True)
        damage = 15
        for i in hits:
            enemy_x = player.rect.x - i.rect.x
            enemy_y = player.rect.y - i.rect.y
        if hits:
            e_health -= damage
            offset = shake(6, 3)

        hits = pygame.sprite.spritecollide(player, e_bullets, True)
        damage = 15
        if hits:
            p_health -= damage
            offset = shake(6, 3)

        # Draw / render

        screen.fill(BLACK)
        health_bars(p_health, e_health)
        all_sprites.draw(screen)

        if p_health < 1:
            game_over()
        elif e_health < 1:
            you_win()

        # drawing part.
        screen.blit(screen, next(offset))
        pygame.display.flip()


game_intro()
