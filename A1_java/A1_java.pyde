float x = 50;
float speed = 3;
boolean boxDropped = false;
float boxX = 0;
float boxY = 200;
float boxSpeed = 0.5f;
float boxFallSpeed = 0;

void setup() {
  size(500, 500);
}

void draw() {
  background(135, 206, 235);
  fill(34, 139, 34);
  rect(0, 450, 500, 100);
  
  if (boxDropped == true) {
    fill(139, 69, 19);
    drawBox(boxX, boxY);
    
    if (boxY > 240 && boxY < 400) {
      fill(255, 0, 0);
      triangle(boxX - 50, boxY - 60, boxX + 50, boxY - 60, boxX, boxY - 110);
      line(boxX - 50, boxY - 60, boxX - 25, boxY);
      line(boxX + 50, boxY - 60, boxX + 25, boxY);
      boxSpeed = 0.1f;
    } else {
      boxSpeed = 0.5f;
    }
    
    boxFallSpeed = boxFallSpeed + boxSpeed;
    boxY = boxY + boxFallSpeed;
    
    if (boxY + 50 >= 450) {
      boxY = 400;
      boxFallSpeed = 0;
    }
  }
  
  if (speed > 0) {
    heliRight(x);
  } else {
    heliLeft(x);
  }
  
  x = x + speed;
  if (x > 440) {
    speed = -3;
  } else if (x < 60) {
    speed = 3;
  }
}

void mousePressed() {
  boxDropped = true;
  boxX = x;
  boxY = 135;
  boxFallSpeed = 0;
  boxSpeed = 0.5f;
}

void heliRight(float x) {
  fill(255, 215, 0);
  line(x, 50, x, 75);
  square(x - 5, 65, 10);
  triangle(x + 10, 75, x - 100, 75, x + 10, 125);
  triangle(x - 100, 75, x - 100, 50, x - 80, 75);
  ellipse(x, 100, 100, 50);
  line(x + 10, 100, x + 50, 100);
  line(x + 10, 100, x + 10, 75);
  ellipse(x - 25, 50, 50, 15);
  ellipse(x + 25, 50, 50, 15);
  ellipse(x, 50, 10, 10);
  line(x - 25, 124, x - 25, 135);
  line(x + 25, 124, x + 25, 135);
  line(x - 50, 135, x + 50, 135);
  line(x + 50, 135, x + 60, 125);
}

void heliLeft(float x) {
  fill(255, 215, 0);
  line(x, 50, x, 75);
  square(x - 5, 65, 10);
  triangle(x - 10, 75, x + 100, 75, x - 10, 125);
  triangle(x + 100, 75, x + 100, 50, x + 80, 75);
  ellipse(x, 100, 100, 50);
  line(x - 10, 100, x - 50, 100);
  line(x - 10, 100, x - 10, 75);
  ellipse(x - 25, 50, 50, 15);
  ellipse(x + 25, 50, 50, 15);
  ellipse(x, 50, 10, 10);
  line(x - 25, 124, x - 25, 135);
  line(x + 25, 124, x + 25, 135);
  line(x - 50, 135, x + 50, 135);
  line(x - 50, 135, x - 65, 125);
}

void drawBox(float bx, float by) {
  square(bx - 25, by, 50);
}
