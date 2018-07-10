class Apple:
    '''
        This class contain the apple info.
    '''
    x = 0 # Horizontal apple position.
    y = 0 # Vertical apple position.
    step = 44

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) # Drawing the apple image on surface
