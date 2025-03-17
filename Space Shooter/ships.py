import pygame
from constants import BULLET_SOUND, HIT, HEIGHT, PLAYER_SHIP, RED_SHIP, GREEN_SHIP, BLUE_SHIP, YELLOW_BULLET, RED_BULLET, GREEN_BULLET, BLUE_BULLET

# Function to detect collision between the masks os obj1 and obj2, if not collision, function return None, if have a collision, returns a tuple of x,y
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

# Class for the bullets, have a X, Y position and a image.
class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        #mask for better collision detection
        self.mask = pygame.mask.from_surface(self.img)

    # function to draw the bullet 
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    # function for the direction of the bullet
    def move(self, vel):
        self.y += vel

    # Detect if bullet goes of screen
    def off_screen(self, height):
        return not(self.y < height and self.y >= 0)
    
    # Detect if the bullet colide with another object
    def collision(self, obj):
        return collide(obj, self)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100,):
        # Player position and health
        self.x = x
        self.y = y
        self.health = health
        #ship que bullet img is none because the subclasses that will define
        self.ship_img = None
        self.bullet_img = None
        self.bullets = []
        # cooldown for the bullets
        self.cd_counter = 0

    # Draw the ship and bullets on the screen
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)

    # Check if bullet is on CD, move bullet down the screen. 
    # If it goes offscreen the bullet is deleted, if collides with the player, player loses 10 health and bullet is also deleted.
    def move_bullets(self, vel, obj):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 10
                pygame.mixer.Sound.play(HIT)
                self.bullets.remove(bullet)

    # If the CD counter past 0.5s, the CD is set to 0 and a new bullet is add to the list to shoot, if is still in cooldown, the CD counter is set to 1.
    def cooldown(self):
        if self.cd_counter >= self.COOLDOWN:
            self.cd_counter = 0
        elif self.cd_counter > 0:
            self.cd_counter += 1

    # If the CD counter is in 0, a bullet is created and add to a list.
    def shoot(self):
        if self.cd_counter == 0:
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cd_counter = 1
            pygame.mixer.Sound.play(BULLET_SOUND)

    # Return the width and height of the ship
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()
    
    
class Player(Ship):
    def __init__(self, x, y, health=100):
        # Inherit atributes from the Ship class
        super().__init__(x, y, health)
        # Get ship and bullet img
        self.ship_img = PLAYER_SHIP
        self.bullet_img = YELLOW_BULLET
        # Create a mask for the img
        self.mask = pygame.mask.from_surface(self.ship_img)
        # Set the max health
        self.max_health = health
    
    # Almost the same as in the Ship class, but instead of removing 10 points of the health, the obj is remove when hit
    def move_bullets(self, vel, objs):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            else:
                for obj in objs:
                   if bullet.collision(obj):
                        objs.remove(obj)
                        pygame.mixer.Sound.play(HIT)
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

    # Override parent draw function, inherit the atributes and add a healthbar
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    # Draw a green rectangle above a red rectangle, and the green will shrink a % when player loses health
    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Ship):
    # Create dict with the possible 3 enemy ships
    COLOR_DICT = {
        "red": (RED_SHIP, RED_BULLET),
        "green": (GREEN_SHIP, GREEN_BULLET),
        "blue": (BLUE_SHIP, BLUE_BULLET)
    }
    #inherit atributes from the class Ship, get the ship color, and create a mask for the img
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.bullet_img = self.COLOR_DICT[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    # define velocite and movement of the enemy
    def move(self, vel):
        self.y += vel

    # Same as in Ship but adjust in axis X for the bullet come out of the center of the enemies
    def shoot(self):
        if self.cd_counter == 0:
            bullet = Bullet(self.x-18, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.cd_counter = 1
            