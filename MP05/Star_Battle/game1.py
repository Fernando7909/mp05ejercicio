import pygame
import random
import sys
import requests
import io

# ========================
# Configuració inicial
# ========================
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicialitzar Pygame i la finestra
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Extensible - Ampliació 4: Menú i Reinici")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Carregar imatge de fons des d'una URL
image_url = "https://cdn.pixabay.com/photo/2017/08/15/08/23/stars-2643089_1280.jpg"
response = requests.get(image_url)
background = pygame.image.load(io.BytesIO(response.content))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ========================
# Variables Globals del Joc
# ========================
score = 0
difficulty_level = 1
lives = 3
last_difficulty_update_time = pygame.time.get_ticks()
spawn_interval = 1500
ADD_OBSTACLE = pygame.USEREVENT + 1


# ========================
# Funcions Auxiliars
# ========================

def draw_text(surface, text, font, color, x, y):
    """Dibuixa un text a la pantalla."""
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))


# ========================
# Classes del Joc
# ========================

class Player(pygame.sprite.Sprite):
    """Classe per al jugador."""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 5

    def update(self):
        """Actualitza la posició del jugador segons les tecles premudes."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Evitar que el jugador surti de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Obstacle(pygame.sprite.Sprite):
    """Classe per als obstacles."""

    def __init__(self):
        super().__init__()
        width = random.randint(20, 100)
        height = random.randint(20, 100)
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - height)
        self.speed = random.randint(3 + difficulty_level, 7 + difficulty_level)

    def update(self):
        global score
        self.rect.x -= self.speed
        if self.rect.right < 0:
            score += 1
            self.kill()


# ========================
# Funció per reinicialitzar el Joc
# ========================

def new_game():
    global score, difficulty_level, lives, last_difficulty_update_time, spawn_interval, all_sprites, obstacles, player
    score = 0
    difficulty_level = 1
    lives = 3
    last_difficulty_update_time = pygame.time.get_ticks()
    spawn_interval = 1500
    pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)


# ========================
# Funció per executar la partida
# ========================

def game_loop():
    global difficulty_level, last_difficulty_update_time, spawn_interval, lives
    new_game()
    game_state = "playing"
    running = True
    while running and game_state == "playing":
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == ADD_OBSTACLE:
                obstacle = Obstacle()
                all_sprites.add(obstacle)
                obstacles.add(obstacle)

        current_time = pygame.time.get_ticks()
        if current_time - last_difficulty_update_time >= 15000:
            difficulty_level += 1
            last_difficulty_update_time = current_time
            spawn_interval = max(500, 1500 - difficulty_level * 100)
            pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)

        all_sprites.update()

        if pygame.sprite.spritecollideany(player, obstacles):
            lives -= 1
            if lives > 0:
                player.rect.center = (100, HEIGHT // 2)
                for obs in obstacles:
                    obs.kill()
            else:
                game_state = "game_over"

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        score_text = font.render("Puntuació: " + str(score), True, WHITE)
        difficulty_text = font.render("Dificultat: " + str(difficulty_level), True, WHITE)
        lives_text = font.render("Vides: " + str(lives), True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(difficulty_text, (10, 40))
        screen.blit(lives_text, (10, 70))
        pygame.display.flip()
    return score


# ========================
# Bucle principal del programa
# ========================

while True:
    game_loop()
