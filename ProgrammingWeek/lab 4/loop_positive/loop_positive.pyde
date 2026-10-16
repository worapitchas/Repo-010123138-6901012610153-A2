def setup():
    size(1000,150)

def draw():
    x=50
    y=50
    while x < 1000:
        draw_positive(x,y)
        x=x+200

def draw_positive(x,y):
    draw_square(x,y)
    draw_square(x+50,y)
    draw_square(x-50,y)
    draw_square(x,y-50)
    draw_square(x,y+50)

def draw_square(x,y):
    square(x,y,50)
    
