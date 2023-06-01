import pygame
import os

pygame.init()


#Inistialing the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')
#set framerates
clock = pygame.time.Clock()
FPS = 60

# Define player action varabiles
moving_left = False
moving_right = False


# define color
BG =(144,201,120)
def draw_bg():
    screen.fill(BG)

# we use this class to set the posi scale of any character we want
class Soldier(pygame.sprite.Sprite):
    def _init_(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite._init_(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()  # Corrected line
        for i in range(5):
            img = pygame.image.load(f'F:/PythonGameSaad/img/{self.char_type}/Idle/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self,moving_left,moving_right):
        # reset  movement varabiles
        dx = 0
        dy = 0

        #assign movement varabiles if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        #update animtion
        ANIMATION_COOLDOWN = 100
        #update image depenmding on current frame
        self.image = self.animation_list[self.frame_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            # if the animation has run out reset back to start
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0


# display specific character and its invisible boundary by using the player
    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False), self.rect)


player = Soldier('player',200,200,2,5)
enemy = Soldier('enemy',400,200,2,5)




run = True
#using while loop to run it for ever till its true
while run:

    #setting some frames so that it should have a limit or else multiple img will occurs
    clock.tick(FPS)

    draw_bg()

    player.update_animation()
    # Calling draw method to display tht img
    player.draw()
    enemy.draw()

    player.move(moving_left,moving_right)


    for event in pygame.event.get():
        #quit game
       if event.type == pygame.QUIT:
           run = False

       #Keyboard presses
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
               moving_left = True
           if event.key == pygame.K_d:
               moving_right = True
    # Close windowby esc key
           if event.key == pygame.K_ESCAPE:
               run = False
     # KEyborad button released
       if event.type == pygame.KEYUP:
           if event.key == pygame.K_a:
               moving_left = False
           if event.key == pygame.K_d:
               moving_right = False

    pygame.display.update()

pygame.quit()