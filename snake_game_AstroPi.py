from sense_hat import SenseHat
import random
import time

"""

  Simple Snake Game-
  
  Play snake game with your Raspberry Pi.  The snake dies immediately if the temperature is less than -10 deg.C or
  more than 60 deg.C. Use key board arrow keys to move the snake in the  desired direction and eat the food to gain 
  points.  
  
  Score will be displayed when the game ends!
  
  Note: Requires sense_hat version 2.2.0 or later
  
"""

#sense = SenseHat()
#sense.low_light = True

# Correcting the orientation of the screen to match the labels on the Astro Pi GUI buttons
#sense.set_rotation(90)

# RGB pixel values for snake, food and clear(0 pixels)
green = (0, 255, 0)
red = (255, 0, 0)
clear = (0, 0, 0)


class Snake:
  def __init__(self, body):
    self.sense = SenseHat()
    self.snakeBody = body
    #self.__score = 0
    
  def checkTemp(self):
    '''
    Checks if the temperature is either below -10 or above 60 degree Celcius. 
    Snake will die in these ranges.
    '''
    
    temp = self.sense.get_temperature()
    
    if temp <= -10:
      
      self.sense.show_message("Snake died because of extremely LOW temperature", text_colour=[255, 0, 0])
      exit()
    
    if temp >= 60:
      self.sense.show_message("Snake died because of extremely HIGH temperature", text_colour=[255, 0, 0])
      exit()
    
  
  def body(self):
    '''
    Places the body of snake into the grid
    '''
    
    for pos in self.snakeBody:
      pixels[pos[1] * 8 + pos[0]] = green
    
  
  def snakeFood(self):
    '''
    Places the snake food into the LED grid display.
    '''
    pixels[food[1] * 8 + food[0]] = red
    
    
  def setDirection(self, d): 
    '''
    Sets up the direction of snake movement such as 0 for up, 1 for right, 2 for down, 3 for left
    '''
  
    global direction
  
    if d == 0:
      direction = [0, -1]
      
    elif d == 1:
      direction = [1, 0]
  
    elif d == 2:
      direction = [0, 1]
      
    elif d == 3:
      direction = [-1, 0]
      
      
  def moveSnake(self):
    '''
    This function does the followings: 
    - Move the snake using joystick. 
    - Randomly place the next food after its eaten. 
    - Calculate score at the end of the game.
    '''
    
    global length, food, score
    
    for event in self.sense.stick.get_events():
      
      if event.action == "pressed":
        
        if event.direction == "up":
          self.setDirection(0)
          
        elif event.direction == "right":
          self.setDirection(1)
        
        elif event.direction == "down":
          self.setDirection(2) 
        
        elif event.direction == "left":
          self.setDirection(3)
          
    self.snakeBody.insert(0, [self.snakeBody[0][0] + direction[0], self.snakeBody[0][1] + direction[1]])
    
    # if snakes goes off the screen it will die
    if self.snakeBody[0][0] < 0:
      self.sense.show_message("GAME OVER! Your Score:", text_colour=[255, 0, 0])
      self.sense.show_message(str(score), text_colour=[255, 255, 0])
      exit()
      
    if self.snakeBody[0][1] < 0:
      self.sense.show_message("GAME OVER! Your Score:", text_colour=[255, 0, 0])
      self.sense.show_message(str(score), text_colour=[255, 255, 0])
      exit()
      
    if self.snakeBody[0][0] > 7:
      self.sense.show_message("GAME OVER! Your Score:", text_colour=[255, 0, 0])
      self.sense.show_message(str(score), text_colour=[255, 255, 0])
      exit()
      
    if self.snakeBody[0][1] > 7:
      self.sense.show_message("GAME OVER! Your Score:", text_colour=[255, 0, 0])
      self.sense.show_message(str(score), text_colour=[255, 255, 0])
      exit()

    # if snake eats the food
    if self.snakeBody[0] == food: 
      food = [] 
      while food == []:  
        food = [random.randint(0, 7), random.randint(0, 7)]  
        if food in self.snakeBody:  
          food = []  
        length += 1
        score += 10
        
    elif self.snakeBody[0] in self.snakeBody[1:]:  
      self.sense.show_message("GAME OVER! Your Score:", text_colour=[255, 0, 0])
      self.sense.show_message(str(score), text_colour=[255, 255, 0])
      exit()
        
    else:
      while len(self.snakeBody) > length: 
        self.snakeBody.pop()   
      
      
#########
# Main
#########

# This array shows coordinates of vectors for each part the snake's body
# Initial position of snake body
#
snakeBody = [[2, 2]]  

# Normal direction of snake movement, left to right of the screen
direction = [1, 0] 

# Length of the snake
length = 1 
score = 0
# Generate an initial random position for food
food = [random.randint(0, 7), random.randint(0, 7)]

while True:
  
  # clear the screen
  pixels = [clear] * 64
  
  snk = Snake(snakeBody)
  
  snk.checkTemp()
  
  # Display snake's initial position
  snk.body()
  
  # Display food position
  snk.snakeFood()
  
  # Move snake with joystick
  snk.moveSnake()
  
  # setting the sense_Hat pixels to the pixels array
  snk.sense.set_pixels(pixels)

  time.sleep(0.50)
