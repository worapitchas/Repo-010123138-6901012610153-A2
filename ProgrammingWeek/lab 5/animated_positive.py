from processing import*
def setup():
    size(900, 400) 

def draw():
    background(255)
    
    i = 0
    while i < 5:
        
        x = 100 + (i * 170)
        y = 150
        
       
        if abs(mouseX - x) < 60 and abs(mouseY - (y + 50)) < 60:
            y = 100
            
        draw_positive(x, y)
        i += 1

def draw_square(x, y):
    line(x, y, x + 50, y)
    line(x, y, x, y + 50)
    line(x, y + 50, x + 50, y + 50)
    line(x + 50, y + 50, x + 50, y)

def draw_positive(x, y):
    draw_square(x, y)
    draw_square(x, y + 50)
    draw_square(x, y + 100)
    draw_square(x + 50, y + 50)
    draw_square(x - 50, y + 50)
    
run()