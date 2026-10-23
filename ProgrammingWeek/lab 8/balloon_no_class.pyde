# ===================================================
# COMPARISON: Without Class
# 1. Stores data (x, y, speed) in a 2D List, making it easy to confuse index positions (e.g., b[0]=x, b[1]=y).
# 2. Drawing logic (draw_balloon) and movement logic (b[1] -= b[2]) are separated in different places.
# 3. Harder to maintain or extend when adding new properties to multiple items.
# ===================================================

balloons = [
    [100, 400, 2],
    [200, 450, 3],
    [300, 420, 1],
    [400, 480, 2.5],
    [500, 410, 1.5]
]

def setup():
    size(600, 500)

def draw():
    background(255)
    
    for b in balloons:
        draw_balloon(b[0], b[1])
        b[1] -= b[2] 
        
        if b[1] < -30: 
            b[1] = height + 30

def draw_balloon(x, y):
    ellipse(x, y, 40, 50) 
    line(x, y + 25, x, y + 65) 
