# Example file showing a basic pygame "game loop"
import pygame, os, random
from constants import WIDTH, HEIGHT, BG, PLAYER_DEATH, HIT
from ships import Player, Enemy, collide

# Import fonts
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# pygame setup
def main():
    # Initialize the pygame, screen, display and FPS
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Space Shooter")
    pygame.mixer.music.load(os.path.join("Space Shooter", "assets", "sounds", "soundtrack.mp3"))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    pixel_font = pygame.font.Font(os.path.join("Space Shooter", "assets", "fonts", "PublicPixel.ttf"), 30)
    lost_font = pygame.font.Font(os.path.join("Space Shooter", "assets", "fonts", "PublicPixel.ttf"), 60)
    running = True
    FPS = 60

    # Variables of the game
    level = 0
    lives = 5
    player_velocity = 5
    enemy_vel = 1
    bullet_vel = 5
    lost = False
    lost_count = 0

    # Enemy list and quantity of enemies in the level 1
    enemies = []
    wave_lenght = 5

    # Instance of the obj player
    player = Player(620, 650)

    # Function to update the screen with the background
    def redraw_window():
        # Put background on the screen
        screen.blit(BG, (0,0))
  
        # Draw Text
        lives_label = pixel_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = pixel_font.render(f"Level: {level}", 1, (255, 255, 255))
        screen.blit(lives_label, (10, 10))
        screen.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        # for every enemy in the enemy list, draw them on the screen
        for enemy in enemies:
            enemy.draw(screen)

        # Draw the player ship
        player.draw(screen)

        # conditional if the player lose, play a song and render in the screen a lose message
        if lost:
            pygame.mixer.Sound.play(PLAYER_DEATH)
            lost_label = lost_font.render("You Lost !!", 1, (255, 255, 255))
            screen.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 370))


        pygame.display.update()

    while running:
        # poll for events
        # limits FPS to 60
        clock.tick(FPS)
        redraw_window()
        
        # If lives is less than 0 or health os 0, player lose
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        # When player loose, he sees a message that he lost for five seconds and is prevented to move the ship, after that the games ends
        if lost:
            if lost_count > FPS * 5:
                running = False
            else:
                continue

        #increase level after defeating all enemies
        if len(enemies) == 0:
            level += 1
            wave_lenght += 3
            for _ in range(wave_lenght):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1200, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)


        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                
    
        # listen to the keys being pressed to move the ship and also prevent to cross the borders of the screen.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + player_velocity > 0: #left
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity + player.get_width() < WIDTH: #right
            player.x += player_velocity
        if keys[pygame.K_UP] and player.y - player_velocity > 0: #up
            player.y -= player_velocity
        if keys[pygame.K_DOWN] and player.y + player_velocity + player.get_height() + 15 < HEIGHT: #down
            player.y += player_velocity

        # player use the space key to shoot
        if keys[pygame.K_SPACE]:
            player.shoot()
            

        # every enemy in the enemy list moves increasing his Y position and so the bullets
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_bullets(bullet_vel, player)

            # enemy shoots random in between 0 and 4 seconds.
            if random.randrange(0, 4*FPS) == 1:
                enemy.shoot()
                
            # if enemy collides with the player, enemy dies and player lose 10 health
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
                pygame.mixer.Sound.play(HIT)

            # if enemy pass the height of the screen, player loses 1 life and the enemy dies
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        # Player bullets have negative direction because they start at the bottom of the screen, and the arguments enemies, is the obj that the player bullet can hit
        player.move_bullets(-bullet_vel, enemies)

# Main menu to show before the game start
def main_menu():
    run = True
    title_font = pygame.font.Font(os.path.join("Space Shooter", "assets", "fonts", "PublicPixel.ttf"), 30)
    while run:
        screen.blit(BG, (0,0))
        title_label = title_font.render("Left click to start...", 1, (255,255,255))
        screen.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 400))
        pygame.display.update()
 
        # Game starts if player press a mouse buttom.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

    pygame.quit()

main_menu()