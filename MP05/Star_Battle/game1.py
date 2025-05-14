import pygame
import random
import sys
import requests
import io
import math
import json
from datetime import datetime

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

SCORE_FILE = "scores.json"

# Inicialitzar Pygame i la finestra
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Extensible - Ampliació 4: Menú i Reinici")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Carregar imatges de fons
image_url = "https://cdn.pixabay.com/photo/2017/08/15/08/23/stars-2643089_1280.jpg"
response = requests.get(image_url)
background = pygame.image.load(io.BytesIO(response.content))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

menu_background = pygame.image.load("Images/fondoInicio.png")
menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))

game_over_background = pygame.image.load("Images/game_over.png")
game_over_background = pygame.transform.scale(game_over_background, (WIDTH, HEIGHT))

# Cargar imagen de pausa
pause_background = pygame.image.load("Images/pause.png")
pause_background = pygame.transform.scale(pause_background, (WIDTH, HEIGHT))

explosion_img = pygame.image.load("Images/explosion.png")
explosion_img = pygame.transform.scale(explosion_img, (50, 50))




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


def save_score(score):
    """Guarda la puntuación con la fecha y hora en un archivo JSON."""
    try:
        # Intentar cargar los puntajes existentes
        with open(SCORE_FILE, "r") as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []  # Si no hay archivo o está vacío, crear lista nueva

    # Agregar la nueva puntuación con fecha y hora
    scores.append({
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    # Ordenar por puntuación de mayor a menor
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    # Guardar los puntajes en el archivo
    with open(SCORE_FILE, "w") as file:
        json.dump(scores, file, indent=4)

    return scores[:3]

# ========================
# Classes del Joc
# ========================

# ========================
# Clase de Explosión
# ========================
class Explosion(pygame.sprite.Sprite):
    """Clase para manejar la animación de explosión."""
    def __init__(self, x, y):
        super().__init__()
        self.image = explosion_img
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = pygame.time.get_ticks()

    def update(self):
        """La explosión desaparece después de 500ms."""
        if pygame.time.get_ticks() - self.timer > 500:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["laser"])  # Se agrega 'laser'
        self.image = pygame.image.load(f"Images/{'pistola.png' if self.type == 'laser' else self.type + '.png'}")
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, WIDTH - 100)
        self.rect.y = random.randint(50, HEIGHT - 50)
        self.lifetime = 5000  # 5 segundos en pantalla
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        """Eliminar el power-up si ha pasado su tiempo de vida"""
        if pygame.time.get_ticks() - self.spawn_time > self.lifetime:
            self.kill()



class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/laser.png")
        self.image = pygame.transform.scale(self.image, (10, 30))  # Ajustar tamaño
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8  # Velocidad del láser

    def update(self):
        """Mover el láser hacia la derecha"""
        self.rect.x += self.speed
        if self.rect.left > WIDTH:  # Eliminar si sale de la pantalla
            self.kill()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/nave.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 5
        self.shooting = False
        self.shooting_time = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.rect.clamp_ip(screen.get_rect())

        # Verificar si el tiempo de disparo ha terminado
        if self.shooting and pygame.time.get_ticks() > self.shooting_time:
            self.shooting = False



class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = random.randint(30, 80)
        height = random.randint(30, 80)

        if width > 70:
            self.image = pygame.image.load("Images/destructor.png")
        elif 50 < width <= 70:
            self.image = pygame.image.load("Images/caza.png")
        else:
            self.image = pygame.image.load("Images/meteorito.png")

        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - height)
        self.speed = random.randint(3 + difficulty_level, 7 + difficulty_level)

        # Movimiento aleatorio: puede ser lineal, sinusoidal o en zigzag
        self.movement_type = random.choice(["linear", "sinusoidal", "zigzag"])
        self.time = 0

    def update(self):
        global score
        self.rect.x -= self.speed

        # Movimiento en zigzag
        if self.movement_type == "zigzag":
            self.rect.y += random.choice([-2, 2])

        # Movimiento sinusoidal (curva)
        elif self.movement_type == "sinusoidal":
            self.rect.y += int(5 * math.sin(self.time * 0.1))
            self.time += 1

        # Eliminar obstáculos fuera de la pantalla
        if self.rect.right < 0:
            score += 1
            self.kill()


# ========================
# Funció per mostrar el menú inicial
# ========================

def show_menu():
    menu_running = True
    while menu_running:
        screen.blit(menu_background, (0, 0))
        draw_text(screen, "STAR BATTLE", font, WHITE, WIDTH // 2 - 100, 150)

        start_button = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)
        quit_button = pygame.Rect(WIDTH // 2 - 100, 500, 200, 50)

        pygame.draw.rect(screen, BLUE, start_button, border_radius=10)
        pygame.draw.rect(screen, RED, quit_button, border_radius=10)

        draw_text(screen, "Iniciar Juego", font, WHITE, WIDTH // 2 - 55, 410)
        draw_text(screen, "Salir del Juego", font, WHITE, WIDTH // 2 - 65, 510)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    menu_running = False
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# ========================
# Funció per mostrar la pantalla de Game Over
# ========================

def show_game_over():
    """Muestra la pantalla de Game Over con las mejores puntuaciones."""
    global score
    top_scores = save_score(score)

    game_over_running = True
    while game_over_running:
        screen.blit(game_over_background, (0, 0))

        # Dibujar los botones
        restart_button = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)
        quit_button = pygame.Rect(WIDTH // 2 - 100, 500, 200, 50)

        pygame.draw.rect(screen, BLUE, restart_button, border_radius=10)
        pygame.draw.rect(screen, RED, quit_button, border_radius=10)

        draw_text(screen, "TOP 3 PUNTUACIONES", font, WHITE, WIDTH // 2 - 100, 50)

        # Mostrar las 3 mejores puntuaciones
        y_offset = 100
        for i, entry in enumerate(top_scores):
            draw_text(screen, f"{i+1}. {entry['score']} - {entry['date']}", font, WHITE, WIDTH // 2 - 120, y_offset)
            y_offset += 30

        draw_text(screen, "Reiniciar Juego", font, WHITE, WIDTH // 2 - 75, 410)
        draw_text(screen, "Salir del Juego", font, WHITE, WIDTH // 2 - 65, 510)

        pygame.display.flip()

        # Eventos para salir o reiniciar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game_over_running = False
                    game_loop()  # Reiniciar el juego
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


# ========================
# Funció per executar la partida
# ========================

def pause_game():
    """Función para pausar el juego y mostrar la pantalla de pausa"""
    paused = True
    while paused:
        screen.blit(pause_background, (0, 0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Presionar 'P' para reanudar
                    paused = False

def game_loop():
    global difficulty_level, last_difficulty_update_time, spawn_interval, lives, score

    score = 0
    difficulty_level = 1
    lives = 3
    last_difficulty_update_time = pygame.time.get_ticks()
    spawn_interval = 1500

    pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)

    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    lasers = pygame.sprite.Group()  # Nuevo grupo de láseres
    player = Player()

    all_sprites.add(player)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == ADD_OBSTACLE:
                obstacle = Obstacle()
                all_sprites.add(obstacle)
                obstacles.add(obstacle)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_game()
                if event.key == pygame.K_SPACE and player.shooting:
                    laser = Laser(player.rect.right, player.rect.centery)
                    all_sprites.add(laser)
                    lasers.add(laser)

        all_sprites.update()

        # Generar PowerUps aleatoriamente
        if random.randint(1, 500) == 1:
            powerup = PowerUp()
            all_sprites.add(powerup)
            powerups.add(powerup)

        # Recoger PowerUps
        collected_powerup = pygame.sprite.spritecollideany(player, powerups)
        if collected_powerup:
            if collected_powerup.type == "laser":
                player.shooting = True
                player.shooting_time = pygame.time.get_ticks() + 20000  # 20 segundos de disparo activo
            collected_powerup.kill()

        # Comprobar si los láseres impactan obstáculos
        for laser in lasers:
            hit_obstacle = pygame.sprite.spritecollideany(laser, obstacles)
            if hit_obstacle:
                explosion = Explosion(hit_obstacle.rect.centerx, hit_obstacle.rect.centery)
                all_sprites.add(explosion)
                hit_obstacle.kill()
                laser.kill()

        # Comprobar colisiones con obstáculos (solo si no es invulnerable)
        if pygame.sprite.spritecollideany(player, obstacles):
            explosion = Explosion(player.rect.centerx, player.rect.centery)
            all_sprites.add(explosion)
            lives -= 1
            if lives > 0:
                player.rect.center = (100, HEIGHT // 2)
                for obs in obstacles:
                    obs.kill()
            else:
                pygame.time.delay(500)
                show_game_over()
                return

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        draw_text(screen, f"Puntuació: {score}", font, WHITE, 10, 10)
        draw_text(screen, f"Dificultat: {difficulty_level}", font, WHITE, 10, 40)
        draw_text(screen, f"Vides: {lives}", font, WHITE, 10, 70)
        pygame.display.flip()



# ========================
# Bucle principal del programa
# ========================

while True:
    show_menu()
    game_loop()
