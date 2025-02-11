import random
import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dog Burger")
#TODO: we need some constants.  WINDOW_WIDTH and WINDOW_HEIGHT, 800, 600
#TODO: create display_surface assign to it pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#TODO: call pygame.display.set_caption()  and pass in the argument "Burger Dog"

FPS = 60
clock = pygame.time.Clock()
#TODO: create an FPS variable and assign 60 to it.
#TODO: create a clock variable and assign pygame.time.Clock()

PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = 0.5
BUFFER_DISTANCE = 100
#TODO: we need the following constants
#TODO: PLAYER_STARTING_LIVES, PLAYER_NORMAL_VELOCITY, PLAYER_BOOST_VELOCITY, STARTING_BOOST_LEVEL
#TODO: STARTING_BURGER_VELOCITY, BURGER_ACCELERATION, BUFFER_DISTANCE
#TODO: values of these variables are: 3, 5, 10, 100, 3, 0.5, 100


score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY
#TODO: create a player_lives variable and assign PLAYER_STARTING_LIVES to it
#TODO: create a player_velocity variable and assign PLAYER_NORMAL_VELOCITY to it
#TODO: create a boost_level variable and assign STARTING_BOOST_LEVEL to it
#TODO: create a burger_velocity variable and assign STARTING_BURGER_VELOCITY to it

ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#TODO: 3 colors, ORANGE, BLACK, AND WHITE.  BLACK and WHITE are standard RGB, ORANGE is a tuple (246, 170, 54)
#TODO: please note the colors are tuples.

font = pygame.font.Font('Assets/Text_Accent/WashYourHand.ttf', 32)


#TODO: create a font variable and assign pygame.font.Font() passing in "WashYourHand.ttf", 32

#NOTES:  text is a str, background_color is a tuple[int, int, int]
#NOTES:  **locations is basically a dictionary of str, tuple[int, int] or int
#NOTES:  this prep_text returns a tuple containing a Font object and a Rectangle object.
def prep_text(text: str, background_color: tuple[int, int, int], **locations):
    text_to_return = font.render(text, True, background_color)
    rect = text_to_return.get_rect()
    # TODO: create a text_to_return variable and assign font.render(text, True, background_color)
    # TODO: create a rect variable and assign text_to_return.get_rect()
    # TODO: create a for location in locations loop
    # TODO: for loop block start
    for location in locations:
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
        # TODO: (2025-02-06): add this elif portion
        elif location == "y":
            rect.y = locations["y"]
        # TODO: (2025-02-06): add this elif portion
        elif location == "topright":
            rect.topright = locations["topright"]
        # TODO: (2025-02-06): add this elif portion
        elif location == "center":
            rect.center = locations["center"]
    return text_to_return, rect


# Set Text Blocks
(points_text, points_rect) = prep_text(f"Burger Points: {burger_points}", ORANGE, topleft=(10, 10))
# TODO: (2025-02-06): assign to (points_text, points_rect)
# TODO: (continued): the result of the call to prep_text() given f"Burger Points: {burger_points}", ORANGE,
# TODO: (continued): topleft=(10, 10)

(score_text, score_rect) = prep_text(f"Score: {score}", ORANGE, topleft=(10, 50))

# TODO: (2025-02-06): assign to (score_text, score_rect)
# TODO: (continued): the result of the call to prep_text() given f"Score: {score}", ORANGE,
# TODO: (continued): topleft=(10, 50)

(title_text, title_rect) = prep_text("Burger Dog", ORANGE, centerx=WINDOW_WIDTH // 2, y=10)
# TODO: (2025-02-06): assign to (title_text, title_rect)
# TODO: (continued): the result of the call to prep_text() given "Burger Dog", ORANGE,
# TODO: (continued): centerx=WINDOW_WIDTH // 2, y=10

(eaten_text, eaten_rect) = prep_text(f"Burgers Eaten: {burgers_eaten}", ORANGE, centerx=WINDOW_WIDTH // 2, y=50)
# TODO: (2025-02-06): assign to (eaten_text, eaten_rect)
# TODO: (continued): the result of the call to prep_text() given f"Burgers Eaten: {burgers_eaten}", ORANGE,
# TODO: (continued): centerx=WINDOW_WIDTH // 2, y=50


(lives_text, lives_rect) = prep_text(f"Lives: {player_lives}", ORANGE, topright=(WINDOW_WIDTH - 10, 10))
# TODO: (2025-02-06): assign to (lives_text, lives_rect)
# TODO: (continued): the result of the call to prep_text() given f"Lives: {player_lives}", ORANGE,
# TODO: (continued): topright=(WINDOW_WIDTH - 10, 10)


(boost_text, boost_rect) = prep_text(f"Boost: (boost_level)", ORANGE, topright=(WINDOW_WIDTH - 10, 50))
# TODO: (2025-02-06): assign to (boost_text, boost_rect)
# TODO: (continued): the result of the call to prep_text() given f"Boost: (boost_level)", ORANGE,
# TODO: (continued): topright=(WINDOW_WIDTH - 10, 50)

(game_over_text, game_over_rect) = prep_text(f"FINAL SCORE: {score}", ORANGE,
                                             center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
# TODO: (2025-02-06): assign to (game_over_text, game_over_rect)
# TODO: (continued): the result of the call to prep_text() given f"FINAL SCORE: {score}", ORANGE,
# TODO: (continued): center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2)

(continue_text, continue_rect) = prep_text("Press any key to play again", ORANGE,
                                           center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64))
# TODO: (2025-02-06): assign to (continue_text, continue_rect)
# TODO: (continued): the result of the call to prep_text() given "Press any key to play again", ORANGE,
# TODO: (continued): center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT //2 + 64)

# Set sounds and music
bark_sound = pygame.mixer.Sound("Assets/Sound Effects/bark_sound.wav")
miss_sound = pygame.mixer.Sound("Assets/Sound Effects/miss_sound.wav")
pygame.mixer.music.load("Assets/Sound Effects/bd_background_music.wav")
# TODO: (2025-02-06): create a bark_sound variable and assign pygame.mixer.Sound() passing in "bark_sound.wav"
# TODO: (2025-02-06): create a miss_sound variable and assign pygame.mixer.Sound() passing in "miss_sound.wav"
# TODO: (2025-02-06): call pygame.mixer.music.load() passing in "bd_background_music.wav"

# Set images
player_image_right = pygame.image.load("Assets/Images/dog_right.png")
player_image_left = pygame.image.load("Assets/Images/dog_left.png")
# TODO: (2025-02-06): create a player_image_right variable and assign pygame.image.load() passing in "dog_right.png"
# TODO: (2025-02-06): create a player_image_left variable and assign pygame.image.load() passing in "dog_left.png"

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("Assets/Images/burger.png")
burger_rect = burger_image.get_rect()
# TODO: (2025-02-06): create a burger_image variable and assign pygame.image.load() passing in "burger.png"
# TODO: (2025-02-06): create a burger_rect variable and assign from burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

pygame.mixer.music.play()
running = True
is_paused = False


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    #TODO: (2025-02-10):  make a for loop:  for event in pygame.event.get():
    # TODO: (2025-02-10): start of for loop block
    # TODO: (2025-02-10):  check if event.type is equal to pygame.QUIT()
    #TODO: (2025-02-10):  set running to False
    # TODO: (2025-02-10):  end of for loop block


def move_player():
    global player_image
    global player_velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_velocity -= player_rect.x
        player_image = player_image_left
    #TODO: (2025-02-10): check if keys[pygame.K_LEFT] and player_rect.left > 0:
    #TODO: (cont.): the if statement block
    #TODO: (cont.):  the if statement block should subtract player_velocity from player_rect.x
    #TODO: (cont.):  set the player_image to player_image_left
    #TODO: (cont.):  end of the if block

    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_velocity += player_rect.x
        player_image = player_image_right
    #TODO: (2025-02-10): check if keys[pygame.K_RIGHT] and player.rect.right < WINDOW_WIDTH:
    #TODO: (cont.):  the if statement block
    #TODO: (cont.):  the if statement block should add player_velocity to player_rect.x
    #TODO: (cont.):  set the player_image to player_image_right
    #TODO: (cont.):  end of the if block
    if keys[pygame.K_UP] and player_rect.top > 100:
        player_velocity -= player_rect.y
    #TODO: (2025-02-10): check if keys[pygame.K_UP] and player.rect.top > 100
    #TODO: (cont.): the if statement block
    #TODO: (cont.):  the if statement block should subtract player_velocity from player_rect.y
    #TODO: (cont.):  end of the if block
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_velocity += player_rect.y
    #TODO: (2025-02-10): check if keys[pygame.K_DOWN] and player.rect.bottom < WINDOW_HEIGHT
    #TODO: (cont.): the if statement block
    #TODO: (cont.):  the if statement block should add player_velocity to player_rect.y
    #TODO: (cont.):  end of the if block

    engage_boost(keys)


def engage_boost(keys):
    global boost_level
    global player_velocity
    if keys[pygame.K_SPACE] and boost_level > 0:
        boost_level -= 1
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY
    #TODO: (2025-02-10): check if keys[pygame.K_SPACE] and boost_level > 0
    #TODO: (2025-02-10): subtract 1 from boost_level
    #TODO: (2025-02-10): else set player_velocity to PLAYER_NORMAL_VELOCITY


def move_burger():
    global burger_velocity
    global burger_points
    burger_velocity += burger_rect.y
    #TODO: (2025-02-10): add burger_velocity to burger_rect.y
    burger_points = int(burger_velocity * (WINDOW_HEIGHT - burger_rect.y + 100))
    pass  #TODO: (2025-02-10):  remove this when done.


def handle_miss():
    global player_lives
    global burger_velocity
    global boost_level
    if burger_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        burger_velocity = STARTING_BURGER_VELOCITY
        player_rect.centerx = WINDOW_WIDTH // 2
        player_rect.bottom = WINDOW_HEIGHT
        boost_level = STARTING_BOOST_LEVEL
    #TODO: (2025-02-10): if burger_rect.y is greater than WINDOW_HEIGHT:
    #TODO: (2025-02-10):  the rest of this functions code is in an if statement block
    #TODO: (2025-02-10):  subtract 1 from player_lives
    #TODO: (2025-02-10):  call miss_sound's play method
    #TODO: (2025-02-10):  set burger_velocity to STARTING_BURGER_VELOCITY
    #TODO: (2025-02-10):  set player_rect.centerx to WINDOW_WIDTH // 2
    #TODO: (2025-02-10):  set player_rect.bottom to WINDOW_HEIGHT
    #TODO: (2025-02-10):  set boost_level to STARTING_BOOST_LEVEL


def check_collisions():
    global burger_points
    global score
    global burgers_eaten
    global BURGER_ACCELERATION
    global boost_level
    if player_rect.colliderect(burger_rect):
        burger_points += score
        burgers_eaten += 1
        bark_sound.play()
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        boost_level += 25
        if boost_level > STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL
        #TODO: (2025-02-10):  add burger_points to score
        #TODO: (2025-02-10):  add 1 to burgers_eaten
        #TODO: (2025-02-10):  call bark_sounds' play method
        #TODO: (2025-02-10):  add BURGER_ACCELERATION to burger_velocity
        #TODO: (2025-02-10):  add 25 to boost_level
        #TODO: (2025-02-10):  finally check if boost_level > STARTING_BOOST_LEVEL
        #TODO: (2025-02-10):  then set boost_level to STARTING_BOOST_LEVEL


def update_hud():
    global points_text
    global score_text
    global eaten_text
    global lives_text
    global boost_text
    points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)
    score_text = font.render("Score: " + str(score), True, ORANGE)
    eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, ORANGE)
    lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)
    boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)


def check_game_over():
    #TODO: hold till 2025-02-12
    pass  #TODO: (2025-02-10):  remove this when done.


def display_hud():
    display_surface.fill(BLACK)
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    pygame.draw.line(display_surface, WHITE, (0, 100), (WINDOW_WIDTH, 100), 3)
    player_image.blit(player_image, player_rect)
    burger_image.blit(burger_image, burger_rect)
    #TODO (2025-02-10): We just blit points_text and points_rect
    #TODO (cont.):  repeat for score, title, eaten, lives, boost
    #TODO (2025-02-10): blit player_image, player_rect
    #TODO (2025-02-10): blit burger_image, burger_rect


def handle_clock():
    pygame.display.update()
    clock.tick(FPS)
    pass  #TODO: (2025-02-10):  remove this when done.
