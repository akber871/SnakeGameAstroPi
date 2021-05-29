from sense_hat import SenseHat
import random
import time

"""

  Simple Snake Game-
  
  Play snake game with your Raspberry Pi.  Use key board arrow keys to move the snake in the 
  desired direction. The Pi picks randomly.  
  
  Score will be displayed when the game ends!
  
  Note: Requires sense_hat version 2.2.0 or later
  
"""

sense = SenseHat()
sense.low_light = True

green = (0, 255, 0)
blue = (0, 0, 255)
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
    
  def setSnakeDirection(self, d): # 0=up, 1=right, 2=down, 3=left
    pass
  
  def collision(self):
    pass
  
      
####
# Main
####

# This array shows coordinates of vectors for each part the snake's body
# Initial position of snake body, center of the screen
snakeBody = [[3, 3]] 

# Array of the direction of moving, x, y
direction = [1, 0]

# Length of snake's body
length = 1 


##################################################################
# Main Function
##################################################################

# Randomizing the location of food in the 8x8 RGB LED grid
food = [random.randint(0, 7), random.randint(0, 7)]

while True:
  pixels = [clear] * 64
  snk = Snake(snakeBody, direction, length)
  pixels = [clear] * 64
  snk.snakePosition()
  pixels[food[1] * 8 + food[0]] = red
  sense.set_pixels(pixels)

  time.sleep(0.10)


  


