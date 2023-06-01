from graphics import Canvas
import time

class Magic:
    """
    The Magic class creates a canvas, wand, and sparkles that follow
    the users mouse. It initializes all state variables, creates the wand, and
    creates the sparkles. It uses other classes, such as Canvas, to draw the
    GUI (Graphical User Interface).
    """

    """Wand constants"""
    WAND_WIDTH = 5
    WAND_HEIGHT = 50

    """Sparkle constants"""
    SPARKLE_RADIUS = 5
    SPARKLE_Y_VEL = 10

    """Graphics delay"""
    DELAY = 1 / 60

    def __init__(self, wand_width=WAND_WIDTH, wand_height=WAND_HEIGHT):
        """
        When creating the canvas, we want to initialize variables to keep track of our
        "state", which is a fancy way of saying what all the values of our variables
        are at any given moment. In this function, we create the canvas, create the wand,
        and create a data structure to hold our sparkles (that will be drawn later).

        Args:
            wand_width: the width of the wand to create (if not specified, uses WAND_WIDTH)
            wand_height: the height of the wand (if not specified, uses WAND_HEIGHT)
        """
        # Create the canvas
        self.canvas = Canvas()
        self.width = self.canvas.get_width()
        self.height = self.canvas.get_height()

        # Create the wand and keep track of attributes for later
        self.wand = self.canvas.create_rectangle(0, 0, wand_width, wand_height)
        self.wand_width = wand_width
        self.wand_height = wand_height
        self.wand_left_x = 0
        self.wand_top_y = 0

        # Create placeholder for future sparkles to be drawn
        # To demystify, I created this AFTER I realized I needed it. That's the beauty
        # of classes, you can just keep creating self variables as you need them
        self.sparkles = []

    def move_wand(self):
        """
        Move the bottom right of the wand to the user's mouse. To calculate the bottom right,
        we get the x coordinate by subtracting the wand_width from the mouse, and the y coordinate
        by subtracting the wand_height from the mouse.
        """
        self.wand_left_x = self.canvas.get_mouse_x() - self.wand_width
        self.wand_top_y = self.canvas.get_mouse_y() - self.wand_height
        self.canvas.move_to(self.wand, self.wand_left_x, self.wand_top_y)

    def move_sparkle(self, sparkle, y_vel=SPARKLE_Y_VEL):
        """
        Move a sparkle up the canvas a specified amount to simulate velocity.

        Args:
            sparkle: the sparkle that is to be moved upwards
            y_vel: the speed at which the sparkle moves (if not specified, uses SPARKLE_Y_VEL)
        """
        self.canvas.move(sparkle, 0, -y_vel)

    def create_sparkle(self, sparkle_radius=SPARKLE_RADIUS, color='yellow'):
        """
        Create a sparkle of specified dimensions. The sparkle will be drawn as an oval on the top
        middle of our wand, which we can access from the class.

        Args:
            sparkle_radius: the radius of each sparkle (if not specified, uses SPARKLE_RADIUS)
            color: the color of each sparkle (if not specified, uses 'yellow')
        """
        sparkle = self.canvas.create_oval(self.wand_left_x + self.wand_width / 2 - sparkle_radius,
                                          self.wand_top_y - sparkle_radius,
                                          self.wand_left_x + self.wand_width / 2 + sparkle_radius,
                                          self.wand_top_y + sparkle_radius,
                                          color)
        # Append to our state variables to keep track of all sparkles drawn so far
        self.sparkles.append(sparkle)

    def canvas_update(self, delay=DELAY):
        """
        Update the canvas to reflect changes.

        Args:
            delay: the amount of delay between each update (if not specified, uses DELAY)
        """
        time.sleep(delay)
        self.canvas.update()


def main():
    """
    What makes classes so powerful is their usability. Once you've put in the hard
    work of creating a class, other programmers can use it and edit the values as
    they wish. For example, the 'canvas' class you use makes it easy to draw graphics
    without having to call a bunch of individual functions. Try it yourself, edit
    parameters to change the wand, sparkles, canvas, etc.
    """
    # Initialization. Automatically creates canvas and (static) wand
    magic = Magic()
    # Try uncommenting next line for a wand double the height
    # magic = Magic(wand_height=100)

    while True:
        # Move our wand to follow our mouse at each iteration
        magic.move_wand()
        # Access created sparkles from our state variable 'sparkles'
        for sparkle in magic.sparkles:
            # Move each sparkle, individually
            magic.move_sparkle(sparkle)
            # Uncomment next line to see sparkles twice as fast
            # magic.move_sparkle(sparkle, y_vel=20)

        # Create a new sparkle, time has passed
        magic.create_sparkle()
        # Try commenting out the previous line and uncommenting the next
        # magic.create_sparkle(color='blue')

        # Update canvas to reflect changes
        magic.canvas_update()



if __name__ == '__main__':
    main()
