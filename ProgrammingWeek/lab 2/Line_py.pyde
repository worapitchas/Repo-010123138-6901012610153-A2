def setup():
    size(500,500)

def draw_L(x,y):
    line(x,y,x,y+100)
    line(x,y+100,x+25,y+100)
def draw_I(x,y):
    line(x,y,x,y+100)
def draw_N(x,y):
    line(x,y,x,y+100)
    line(x+50,y,x+50,y+100)
    line(x,y,x+50,y+100)
def draw_E(x,y):
    line(x,y,x,y+100)
    line(x,y,x+50,y)
    line(x,(y*4)/2,x+50,(y*4)/2)
    line(x,y+100,x+50,y+100)

def draw():
    draw_L(50,50)
    draw_I(100,50)
    draw_N(150,50)
    draw_E(250,50)
