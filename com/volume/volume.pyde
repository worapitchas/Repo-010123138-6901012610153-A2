def setup():
  size(500,500)

volume = float(input("Volume of rain drop per loop : ")) 

def draw_circle(x,y,r):
  ellipse(x,y,r,r)

def draw_rain_drops_until(volume):
  sum = 0
  while (sum < volume): 
    x = random(100,400) 
    y = random(150,350) 
    r = random(3,30) 
    draw_circle(x,y,r)
    sum = sum + r 
def draw():
  global volume
  background(125)
  draw_rain_drops_until(volume)
