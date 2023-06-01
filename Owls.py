import pygame
pygame.init()                                       # pygame.init() is required to use pygame.

screen = pygame.display.set_mode([800, 600])        # Make a screen object to draw on.
screen.fill("black")                                # This color should be a constant.

# Creates 24 point font... Size can be changed later with 'font.size = 30' for example.
font = pygame.freetype.Font(None, 24)

# This function draws text to the center of a 600 x 800 screen. If necessary, you can
#  enhance it with a parameter for color, or by allowing coordinates to put the text 
# in other locations.
def center_text(text):
    text_rect = font.get_rect(text)
    text_rect.center = (400, 300)
    text_rect = font.render_to(screen, text_rect, text, "gray")

# A very basic example class that can be enhanced and modified as needed.
class Block():
    def __init__(self, color):
        self.rect = pygame.Rect((50, 200), (40, 40))
        self.color = color

    def move_left(self):
        self.erase()
        self.rect.move_ip(-1,0)
        self.draw()
    
    def move_right(self):
        self.erase()
        self.rect.move_ip(1,0)
        self.draw()
    
    def move_up(self):
        self.erase()
        self.rect.move_ip(0,-1)
        self.draw()

    def move_down(self):
        self.erase()
        self.rect.move_ip(0,1)
        self.draw()
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def erase(self):
        pygame.draw.rect(screen, "black", self.rect)

center_text("Hello! Erase me with the block! Press 'Esc' to quit.")

left_block = Block("blue")
right_block = Block("red")
left_block.rect.center = (50,300)
right_block.rect.center = (750,300)

running = True
while running:
    pygame.display.update()

    # This section checks the state of keys... Not just events related to keys.
    # This is the right strategy for things that should happen while a key is down.
    if pygame.key.get_pressed()[pygame.K_a]:
        print("Keep going left!")
        left_block.move_left()

    if pygame.key.get_pressed()[pygame.K_d]:
        print("Keep going right")
        left_block.move_right()

    if pygame.key.get_pressed()[pygame.K_w]:
        print("Keep going right")
        left_block.move_up()

    if pygame.key.get_pressed()[pygame.K_s]:
        print("Keep going right")
        left_block.move_down()

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        print("Keep going left")
        right_block.move_left()

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        print("Keep going right")
        right_block.move_right()

    if pygame.key.get_pressed()[pygame.K_UP]:
        print("Keep going left")
        right_block.move_up()

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        print("Keep going left")
        right_block.move_down()


    # This section looks for events, including key down events. This is the right 
    #  stratagy for things that should happen once per key press.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                print("Spacebar was pressed")
            elif event.key == pygame.K_t:
                print("'t' key was pressed")
        elif event.type == pygame.QUIT:
            running = False

pygame.quit()