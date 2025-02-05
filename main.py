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
pygame.time.Clock()
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
def prep_text(text : str, background_color : tuple[int, int, int], **locations):

    text_to_return = font.render(text, True, background_color)
    rect = text_to_return.get_rect()
    for location
    #TODO: create a text_to_return variable and assign font.render(text, True, background_color)
    #TODO: create a rect variable and assign text_to_return.get_rect()
    #TODO: create a for location in locations loop
    #TODO: for loop block start
        if location == "topleft":
            rect.topleft = locations["topleft"]
        elif location == "centerx":
            rect.centerx = locations["centerx"]
        # NOTE:  We'll add more later.
    #TODO: for loop block end
    #TODO: return (text_to_return, rect)
    pass #TODO: remove this when done.