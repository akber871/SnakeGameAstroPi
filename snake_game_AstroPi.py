from sense_hat import SenseHat
import random
import time

"""

  Simple Snake Game
  
  Play snake game with your Raspberry Pi.  Use key board arrow keys to move the snake in the 
  desired direction and eat the food to gain points.  
  
  Score will be displayed when the game ends!
  
  Note: Requires sense_hat version 2.2.0 or later
  
"""

sense = SenseHat()
sense.low_light = True

# Correcting the orientation of the screen to match the labels on the interface
sense.set_rotation(270)

# RGB pixel values for snake, food and clear(0 pixels)
green = (0, 255, 0)
red = (255, 0, 0)
clear = (0, 0, 0)

class Snake:
  def __init__(self, snakeBody, direction, length):
    self.__snakeBody = snakeBody
    self.__directon = direction
    self.__length = length
  
  def snakePosition(self):    
    for pos in self.__snakeBody:
      pixels[pos[1] * 8 + pos[0]] = green
      #sense.set_pixels(pixels)
      
  def moveSnake(self):
    #pixels = [clear] * 64  
    for event in sense.stick.get_events():
      if event.action == "pressed":
        if event.direction == "up":
          self.setSnakeDirection(0)
          
        elif event.direction == "right":
          self.setSnakeDirection(1)
        
        elif event.direction == "down":
          self.setSnakeDirection(2) 
        
        elif event.direction == "left":
          self.setSnakeDirection(3)
          
    # To move, add new coordinates to the start of snakeBody array and remove the last element 
    self.__snakeBody.insert(0, [self.__snakeBody[0][0] + self.__direction[0], self.__snakeBody[0][1] + self.__direction[1]])
    
    
  def setSnakeDirection(self, d): # 0=up, 1=right, 2=down, 3=left
    if d == 0:
      self.__direction = [0, -1]
      
    elif d == 1:
      self.__direction = [1, 0]
  
    elif d == 2:
      self.__direction = [0, 1]
      
    elif d == 3:
      self.__direction = [-1, 0]
    
  
  
  def checkSnakePosition(self, food): 
    pass
  
  
  def collision(self):
    pass
  
      
######
# Main
######

# This array shows coordinates of vectors for each part the snake's body
# Initial position of snake body, center of the screen
snakeBody = [[3, 3]] 

# Array of the direction of moving, x, y
direction = [1, 0]

# Length of snake's body
length = 1 

# Randomizing the location of food in the 8x8 RGB LED grid
food = [random.randint(0, 7), random.randint(0, 7)]

while True:
  
  # clear all the LEDs to nothing (no light)
  pixels = [clear] * 64
  
  snk = Snake(snakeBody, direction, length)
  
  # Display snake position
  snk.snakePosition()
  
  # Display food position
  pixels[food[1] * 8 + food[0]] = red
  
  # Moving the snake
  snk.moveSnake()
  
  sense.set_pixels(pixels)

  time.sleep(1)


  


