import pygame

# size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "CROSSY RPG"
# colors according to RGB codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# clock used to update game events and frames
clock = pygame.time.Clock()

class Game:
    # FPS 60
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))

        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)

        # Set the title of the game
        pygame.display.set_caption(title)


    def run_game_loop(self):
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('./Images/player.png', 375, 700, 50, 50)
        enemy_0 = NonPlayerCharacter('./Images/enemy.png', 20, 400, 50, 50)
        treasure = GameObject('./Images/treasure.png', 375, 50, 50, 50)

        # Main game loop, used to update all gameplay such as movement, checks, and graphhics
        # Runs until is_game_over = True
        while not is_game_over:
        # A loop to get all of the events occuring at any given time
        # Events are most often mouse movement, mouse and button clicks, or exit
            for event in pygame.event.get():
            # If we have a quite type event (exit out) then exit out of the game
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            # redraw the screen to be a blank 
            self.game_screen.fill(WHITE_COLOR)

            treasure.draw(self.game_screen)

            #update the player position
            player_character.move(direction, self.height)

            #Draw the player at the new position
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True


            # Update all game graphics
            pygame.display.update()

            #Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

# Generic game object class to be subclassed by other objects in the game
class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))
        
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # Draw the object by blitting it onto the background (game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
    
class PlayerCharacter(GameObject):
    
    #How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    #Move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # keeps the character in the game screen
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        
        return True

class NonPlayerCharacter(GameObject):
    
    #How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    #Move function will move character up if direction > 0 and down if < 0
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED) # abs makes sure it's always positive
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()


# load the player image
# player_image = pygame.image.load('./images/player.png')

# scale the image up
# player_image = pygame.transform.scale(player_image, (50, 50))

    # draw rectangul
    # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])

    # # draw circle
    # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

    # draw the player image on top of the screen at (x,y) position
    # game_screen.blit(player_image, (375, 375))