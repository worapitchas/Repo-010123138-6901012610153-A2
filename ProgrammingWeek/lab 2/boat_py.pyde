x = 0
y = 250

def setup():
    size(500,500)
    frameRate(240)
    
def boat(x, y):
    line(x, y, x + 80, y)         
    line(x + 80, y, x + 60, y + 20) 
    line(x + 60, y + 20, x + 20, y + 20) 
    line(x + 20, y + 20, x, y)     
    
    
    line(x + 40, y, x + 40, y - 40) 
    line(x + 40, y - 40, x + 70, y) 

def draw():
    global x
    global y
    background(255)
    boat(x, y)
    x += 1
    if x > 300:
        x = 300


  
