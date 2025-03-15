import pygame, os

# Declaration of constants used by other files.
# constant for screen size
WIDTH, HEIGHT = 800, 800

# Load enemy images
RED_SHIP = pygame.image.load(os.path.join("Space Shooter", "assets", "ships", "red_small.png"))
GREEN_SHIP = pygame.image.load(os.path.join("Space Shooter", "assets", "ships", "green_small.png"))
BLUE_SHIP = pygame.image.load(os.path.join("Space Shooter", "assets", "ships", "blue_small.png"))

# Player ship
PLAYER_SHIP = pygame.image.load(os.path.join("Space Shooter", "assets", "ships", "player_ship.png"))

# Load bullets
RED_BULLET = pygame.image.load(os.path.join("Space Shooter", "assets", "bullets", "red.png"))
GREEN_BULLET = pygame.image.load(os.path.join("Space Shooter", "assets", "bullets", "green.png"))
BLUE_BULLET = pygame.image.load(os.path.join("Space Shooter", "assets", "bullets", "blue.png"))
YELLOW_BULLET = pygame.image.load(os.path.join("Space Shooter", "assets", "bullets", "yellow.png"))

pygame.mixer.init()
# Background and sound effects
BG = pygame.transform.scale(pygame.image.load(os.path.join("Space Shooter", "assets", "backgrounds", "background-black.png")), (WIDTH, HEIGHT))
BULLET_SOUND = pygame.mixer.Sound(os.path.join("Space Shooter", "assets", "sounds", "shoot.mp3"))
pygame.mixer.Sound.set_volume(BULLET_SOUND, 0.2)
PLAYER_DEATH = pygame.mixer.Sound(os.path.join("Space Shooter", "assets", "sounds", "death.mp3"))
pygame.mixer.Sound.set_volume(PLAYER_DEATH, 0.2)
HIT = pygame.mixer.Sound(os.path.join("Space Shooter", "assets", "sounds", "enemy-hit.mp3"))
pygame.mixer.Sound.set_volume(HIT, 0.2)
