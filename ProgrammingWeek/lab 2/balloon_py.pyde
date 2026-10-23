x = 0
y = 150
r = 50


def setup():
    frameRate(240)
    size(300,300)

def balloon(x,y):
    ellipse(x,y,r,r)
    line(x,y+25,x,y+80)
  
def draw():
    global x
    background(255)
    balloon(x,y)
    x += 1
    if (x > 300):
        x = 300
  
