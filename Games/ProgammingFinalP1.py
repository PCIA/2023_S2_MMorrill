import turtle
turtle.setup(550, 550)
turtle.setworldcoordinates(-25, 525, 525, -25)
turtle.speed(0)

CELL_SIZE = 50

def draw_grid():
    for i in range(11):
        turtle.penup()
        turtle.goto(i*CELL_SIZE, 0)
        turtle.pendown()
        turtle.goto(i*CELL_SIZE, 500)
        turtle.penup()
        turtle.goto(0, i*CELL_SIZE)
        turtle.pendown()
        turtle.goto(500, i*CELL_SIZE)

def on_click(x, y):
    # The x and y values coming in as input parameters here, 
    #   are the coordinates of a mouse click, as demonstrated 
    #   by the following 3 lines. Run the program before you 
    #   start, to see this output.
    x = int(x)
    y = int(y)
    print("Mouse clicked coordinates: ", (x, y))
    def column_check(num):
        column = 0
        if num >= 0:
            column = 1
        if num >= 50:
            column = 2
        if num >= 100:
            column = 3
        if num >= 150:
            column = 4
        if num >= 200:
            column = 5
        if num >= 250:
            column = 6
        if num >= 300:
            column = 7
        if num >= 350:
            column = 8
        if num >= 400:
            column = 9
        if num >= 450:
            column = 10
        return column
    def row_check(num):
        row = 0
        if num >= 0:
            row = 1
        if num >= 50:
            row = 2
        if num >= 100:
            row = 3
        if num >= 150:
            row = 4
        if num >= 200:
            row = 5
        if num >= 250:
            row = 6
        if num >= 300:
            row = 7
        if num >= 350:
            row = 8
        if num >= 400:
            row = 9
        if num >= 450:
            row = 10
        return row
        
    if x < 0 or y < 0 or x>500 or y>500:
        print('Coordinate outside of cell grid.')
    else:
        column_check(y)
        print('The cell is in row', row_check(y),'and the column is', column_check(x))
    
    # Analyze this code. Then add code here, to calculate the 
    #   grid cell corresponding to the mouse click. Print the 
    #   cell coordinate similar to how the mouse coordinates 
    #   are printed above.

draw_grid()
turtle.onscreenclick(on_click)
turtle.done()