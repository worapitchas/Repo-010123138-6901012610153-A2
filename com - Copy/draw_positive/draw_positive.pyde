
def setup():
    size(500,500)
    
def draw():
    global x, y
    x = random(100,400) 
    y = random(150,350)
    draw_positive(x,y)
    
    
def draw_square(x,y):
    line(x,y,x+50,y)
    line(x,y,x,y+50)
    line(x,y+50,x+50,y+50)
    line(x+50,y+50,x+50,y)
    
def draw_positive(x,y):
    draw_square(x,y)
    draw_square(x,y+50)
    draw_square(x,y+100)
    draw_square(x+50,y+50)
    draw_square(x-50,y+50)






       
