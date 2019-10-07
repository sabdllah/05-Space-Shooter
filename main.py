import sys, logging, arcade, random

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)



PLANET_COUNT = 50

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "2D Game"

#arcade.open_window (SCREEN_WIDTH, SCREEN_HEIGHT, "2D Game")

class Planet(arcade.Sprite):

    def reset_pos(self):

        
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

       
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_sprite_list = None
        self.planet_sprite_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.DARK_BLUE)


    def setup(self):

        self.player_sprite_list = arcade.SpriteList()
        self.planet_sprite_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("images/ship.png")
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        #add sprite to sprite list
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        planet_list = ['BluePlanet','Earth','FullMoon','Hurricane']
        for i in range(PLANET_COUNT):
            planet_image = random.choice(planet_list)
            planet = Planet("images/{}.png".format(planet_image))

            planet.center_x = random.randrange(SCREEN_WIDTH)
            planet.center_y = random.randrange(SCREEN_HEIGHT)

            self.planet_sprite_list.append(planet)


    
        
    def on_draw(self):  
        arcade.start_render()
        self.planet_sprite_list.draw()
        self.player_sprite_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.planet_sprite_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.planet_sprite_list)
        for planet in hit_list:
            planet.kill()
            self.score += 1
       
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()