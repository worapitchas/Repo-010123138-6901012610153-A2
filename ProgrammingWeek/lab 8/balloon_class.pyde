# ===================================================
# COMPARISON: With Class
# 1. Encapsulates all attributes of a single balloon inside one object.
# 2. Clear variable access via named attributes (self.x, self.y, self.speed), improving readability.
# 3. Bundles drawing (show) and animation (move) behaviors neatly inside the same class.
# 4. Scalable and safer to extend or create more balloons without breaking existing logic.
# ===================================================

class Balloon:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
    def show(self):
        ellipse(self.x, self.y, 40, 50) 
        line(self.x, self.y + 25, self.x, self.y + 65) 
        
    def move(self):
        self.y -= self.speed 
        
        if self.y < -30: 
            self.y = height + 30

balloons = []

def setup():
    size(600, 500)
    
    balloons.append(Balloon(100, 400, 2))
    balloons.append(Balloon(200, 450, 3))
    balloons.append(Balloon(300, 420, 1))
    balloons.append(Balloon(400, 480, 2.5))
    balloons.append(Balloon(500, 410, 1.5))

def draw():
    background(255) 
    
    for b in balloons:
        b.show()
        b.move()
