x = 10 

def setup():
    size(500, 500)

def draw():
    global x
    background(255)
    
    draw_balloon(x)  
    
    x = x + 2  
    if x > 500:
        x = 10

def draw_balloon(x):
    ellipse(x, 100, 100, 100) 
    line(x, 150, x, 250)        
