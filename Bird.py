import NeuralNetwork
import matrix

Acceleration=0.8
class bird():
    def __init__(self):
        self.x=100
        self.y=200
        self.velocity=0
        self.alive=True
        self.brain=NeuralNetwork.neuralnetwork(4,3,1)
        self.score=1
        self.fitness=0

    def think(self,pipes):
        input=[0,0,0,0]

        input[0]=self.y/800

        for i in pipes:

            if i.x > -90 and i.x < 600:
                input[1] = (i.x) / 800
                input[2] = (i.y - 110) / 800
                input[3] = (i.y - 20) / 800

                continue
        return self.brain.feedforward(input).data

    def train(self,pipes):
        input = [0, 0, 0, 0,]

        input[0] = self.y / 800

        for i in pipes:

            if i.x > -90 and i.x < 600:
                input[1] = (i.x) / 800
                input[2] = (i.y - 110) / 800
                input[3] = (i.y - 20) / 800

                continue

        target=self.best_move(input)


        self.brain.train(input,target)
        return [target]

    def best_move(self,input):
        """input = [0, 0, 0, 0, 0]
        # bird_y, pipe_x, pipe_top_y, pipe_bottom_y
        input[0] = self.y / 800
        input[4] = self.velocity / 10


        for i in pipes:

            if i.x>-90 and i.x<600:
                input[1] = (i.x) / 800
                input[2] = (i.y -110) / 800
                input[3] = (i.y-20) / 800"""


        if input[0]>input[3]:

            return [1]
        elif input[0]<input[2]:
            return [0]

        else:
            return [1]

    def move(self):

        self.velocity+=Acceleration
        if self.velocity>10:
            self.velocity=10

        if  self.y<700 :
            self.y+=self.velocity
            if self.y<=0:
                self.y=0



    def jump(self):
        if self.velocity>0:
            self.velocity=-10
        #REMOVE THE ABOVE CODE AND ADD THE CODE BELOW WHILE TESTING
        #self.y -= 10

    def down(self):
        self.y+=10
    def right(self):
        self.x+=10
    def left (self):
        self.x-=10




