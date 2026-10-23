x = 50
speed = 3 
box_dropped = False 
box_x = 0 
box_y = 200 
box_speed = 0.5 
box_fall_speed = 0 

def setup(): 
    size(500, 500) 

def draw(): 
    global x, speed, box_dropped, box_x, box_y, box_fall_speed, box_speed 
    background(135, 206, 235) 
    
    fill(34, 139, 34) 
    rect(0, 450, 500, 100) 
    
    if box_dropped == True: 
        fill(139, 69, 19) 
        box(box_x, box_y) 
        
        if box_y > 240 and box_y < 400:
            fill(255, 0, 0)
            triangle(box_x - 50, box_y - 60, box_x + 50, box_y - 60, box_x, box_y - 110)
            line(box_x - 50, box_y - 60, box_x - 25, box_y) 
            line(box_x + 50, box_y - 60, box_x + 25, box_y) 
            box_speed = 0.1
        else:
            box_speed = 0.5
            
        box_fall_speed = box_fall_speed + box_speed 
        box_y = box_y + box_fall_speed 
        
    
        if box_y + 50 >= 450: 
            box_y = 400
            box_fall_speed = 0 

    if speed > 0: 
        heli_right(x) 
    else: 
        heli_left(x) 
        
    x = x + speed 
    if x > 440: 
        speed = -3 
    elif x < 60: 
        speed = 3 

def mousePressed(): 
    global box_dropped, box_x, box_y, box_fall_speed, box_speed 
    box_dropped = True 
    box_x = x 
    box_y = 135 
    box_fall_speed = 0 
    box_speed = 0.5 

def heli_right(x): 
    fill(255, 215, 0) 
    line(x,50,x,75) 
    square(x-5,65,10) 
    triangle(x+10,75,x-100,75,x+10,125) 
    triangle(x-100,75,x-100,50,x-80,75) 
    ellipse(x, 100, 100, 50) 
    line(x+10,100,x+50,100) 
    line(x+10,100,x+10,75) 
    ellipse(x-25,50,50,15) 
    ellipse(x+25,50,50,15) 
    ellipse(x,50,10,10) 
    line(x-25,124,x-25,135) 
    line(x+25,124,x+25,135) 
    line(x-50,135,x+50,135) 
    line(x+50,135,x+60,125) 

def heli_left(x): 
    fill(255, 215, 0) 
    line(x,50,x,75) 
    square(x-5,65,10) 
    triangle(x-10,75,x+100,75,x-10,125) 
    triangle(x+100,75,x+100,50,x+80,75) 
    ellipse(x, 100, 100, 50) 
    line(x-10,100,x-50,100) 
    line(x-10,100,x-10,75) 
    ellipse(x-25,50,50,15) 
    ellipse(x+25,50,50,15) 
    ellipse(x,50,10,10) 
    line(x-25,124,x-25,135) 
    line(x+25,124,x+25,135) 
    line(x-50,135,x+50,135) 
    line(x-50,135,x-65,125) 

def box(bx, by): 
    square(bx-25, by, 50)
