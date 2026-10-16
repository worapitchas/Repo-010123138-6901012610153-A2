def setup():
    size(500,500)
    
def draw():
    x= random(50,450)
    y= random(50,450)
    draw_positive(x,y)
    
    
    
def draw_positive(x,y):
    draw_square(x,y)
    draw_square(x+50,y)
    draw_square(x-50,y)
    draw_square(x,y-50)
    draw_square(x,y+50)

def draw_square(x,y):
    square(x,y,50)
    
