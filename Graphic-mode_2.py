
from processing import*

def setup():


  word = input("Enter word (L, I, N, E): ").upper()
  
  size(800, 400)
  
  
  
  w = 60    
  h = 100    
  gap = 30  
  start_x = 50
  start_y = 150

  for i in range(len(word)):
      letter = word[i]
      
      current_x = start_x + (i * (w + gap))
      
      if letter == 'L':
          line(current_x, start_y, current_x, start_y + h)
          line(current_x, start_y + h, current_x + w, start_y + h)
          
      elif letter == 'I':
          line(current_x + (w / 2), start_y, current_x + (w / 2), start_y + h)
          line(current_x, start_y, current_x + w, start_y)
          line(current_x, start_y + h, current_x + w, start_y + h)
          
      elif letter == 'N':
          line(current_x, start_y, current_x, start_y + h)
          line(current_x, start_y, current_x + w, start_y + h)
          line(current_x + w, start_y, current_x + w, start_y + h)
          
      elif letter == 'E':
          line(current_x, start_y, current_x, start_y + h)
          line(current_x, start_y, current_x + w, start_y)
          line(current_x, start_y + (h / 2), current_x + w, start_y + (h / 2))
          line(current_x, start_y + h, current_x + w, start_y + h)
          
run()
