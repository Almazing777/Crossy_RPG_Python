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

        # Main game loop, used to update all gameplay such as movement, checks, and graphhics
        # Runs until is_game_over = True
        while not is_game_over:
        # A loop to get all of the events occuring at any given time
        # Events are most often mouse movement, mouse and button clicks, or exit
            for event in pygame.event.get():
            # If we have a quite type event (exit out) then exit out of the game
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            # Update all game graphics
            pygame.display.update()

            #Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        #Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))
        
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    # draw the object by blitting it onto the bacgkroudn (game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
    
class PlayerCharacter(GameObject):
    
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction):
        if direction > 0:
            self.y_pos -= SPEED
        elif direction < 0:
            self.y_pos += SPEED



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