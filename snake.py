class Snake:
    '''
        This class contain the snake info.
        The snake have a list on X and Y that contains the body information.
    '''
    x = [0] # Horizontal snake body positions.
    y = [0] # Vertical snake body positions.
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # Initial snake positions.
       self.x[1] = 1 * 44
       self.x[2] = 2 * 44

    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # Update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # Update position of snake head
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0 # Set the snake moviment to right

    def moveLeft(self):
        self.direction = 1 # Set the snake moviment to left

    def moveUp(self):
        self.direction = 2 # Set the snake moviment to up

    def moveDown(self):
        self.direction = 3 # Set the snake moviment to down

    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))  # Drawing the snake images on surface
