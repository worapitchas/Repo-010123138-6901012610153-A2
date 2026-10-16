x = 0
r = 10
g = 50
b = 100

def draw_balloon(x,y,r,g,b):
    a = color(r,g,b)
    fill(a)
    ellipse(x,y,100,100)
    line(x,y+50,x,y+200)

def setup():
    size(500,500)
    
def draw():
    global x
    global r
    global g
    global b
    background(255,255)
    draw_balloon(x,mouseY,0+r,0+g,0+b)
    draw_balloon(x+150,mouseY-20,50+r,25+g,70+b)
    x = x + 2
    if x == 500:
        x = 0
