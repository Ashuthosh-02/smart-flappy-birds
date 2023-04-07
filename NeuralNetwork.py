from matrix import Matrix
from matrix import ToMatrix


#copy
#mutate
class neuralnetwork():
    def __init__(self,input_nodes,hidden_nodes,output_nodes):
        self.input_nodes=input_nodes
        self.hidden_nodes=hidden_nodes
        self.output_nodes=output_nodes

        self.weights_ih=Matrix(self.hidden_nodes,self.input_nodes)
        self.weights_ho=Matrix(self.output_nodes,self.hidden_nodes)
        self.weights_ho.randomize()
        self.weights_ih.randomize()

        self.bias_ih=Matrix(hidden_nodes,1)
        self.bias_ho=Matrix(output_nodes,1)
        self.bias_ho.randomize()
        self.bias_ih.randomize()



        self.learning_rate=0.2

    def copy(self,brain):
        self.weights_ho=brain.weights_ho
        self.weights_ih=brain.weights_ih
        self.bias_ho=brain.bias_ho
        self.bias_ih=brain.bias_ih

    def mutate(self):
        weights_ho=self.weights_ho.ToList()
        weights_ih=self.weights_ih.ToList()
        bias_ho=self.bias_ho.ToList()
        bias_ih=self.bias_ih.ToList()

        self.weights_ho.randomize(start=-0.1,end=0.1)
        self.weights_ih.randomize(start=-0.1,end=0.1)
        self.bias_ho.randomize(start=-0.1,end=0.1)
        self.bias_ih.randomize(start=-0.1,end=0.1)

        self.weights_ho.add(weights_ho)
        self.weights_ih.add(weights_ih)

        self.bias_ho.add(bias_ho)
        self.bias_ih.add(bias_ih)
        self.bias_ho.tanh()
        self.bias_ih.tanh()
        self.weights_ih.tanh()
        self.weights_ho.tanh()



    def feedforward(self,input):

        # TO GET HIDDEN OUPUTS
        inp=ToMatrix(input)
        hidden=self.weights_ih.cross(inp)
        hidden.add(self.bias_ih)

        hidden.tanh()

        #TO GET OUTPUT OUTPUT
        output = self.weights_ho.cross(hidden)
        output.add(self.bias_ho)
        output.tanh()

        return output

    def train(self, input,answer):
        #SAME CODE AS THE FEEDFORWARD
        # TO GET HIDDEN OUPUTS
        inp = ToMatrix(input)
        hidden = self.weights_ih.cross(inp)
        hidden.add(self.bias_ih)
        hidden.tanh()

        # TO GET OUTPUT OUTPUT
        output = self.weights_ho.cross(hidden)
        output.add(self.bias_ho)
        output.tanh()

        # CONVERT THE ANSWER LIST TO MATRIX OBJECT
        m=len(answer)
        target=Matrix(col=1,row=m)
        for i in range(m):
            target.data[i][0]=answer[i]

        #FIND ERRORS IN THE FINAL OUTPUT
        output_error=target.subtract(output)

        #FIND THE ERROR IN THE HIDDEN OUTPUT
        who_t=self.weights_ho.transpose()
        hidden_error=who_t.cross(output_error)

        #CALCULATING THE GRADIENT AND ADJUSTING THE WEIGHTS FOR BETWEEN HIDDEN AND OUTPUT
        output.dtanh()
        output.multiply(output_error)
        output.multiply(self.learning_rate)

        self.bias_ho.add(output)


        hidden_trans=hidden.transpose()
        weight_ho_deltas=output.cross(hidden_trans)

        self.weights_ho.add(weight_ho_deltas)

        # CALCULATING THE GRADIENT AND ADJUSTING THE WEIGHTS FOR BETWEEN INPUT AND HIDDEN
        hidden.dtanh()
        hidden.multiply(hidden_error)
        hidden.multiply(self.learning_rate)

        self.bias_ih.add(hidden)

        input_trans=inp.transpose()
        weight_ih_deltas=hidden.cross(input_trans)

        self.weights_ih.add(weight_ih_deltas)


