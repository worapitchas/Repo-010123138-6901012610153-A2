
def setup():
    size(500,500)

def draw():
    global x, y
    x = random(100,400) 
    y = random(150,350)
    draw_house(x,y)


def draw_roof(x,y):
    line(x,y,x-75,y+75)
    line(x,y,x+75,y+75)
    
def draw_ceiling(x,y):
    line(x-75,y+75,x+75,y+75)

def draw_wall(x,y):
    line(x-75,y+75,x-75,y+175)
    line(x+75,y+75,x+75,y+175)

def draw_floor(x,y):
    line(x-75,y+175,x+75,y+175)
    
def draw_door(x,y):
    ellipse(x,y+125,100,100)
    line(x,y+75,x,y+175)
    
def draw_house(x,y):
    draw_roof(x,y)
    draw_ceiling(x,y)
    draw_wall(x,y)
    draw_floor(x,y)
    draw_door(x,y)
