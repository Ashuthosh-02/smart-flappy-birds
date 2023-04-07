import random
import math

class Matrix:

    #MAKES MATRIX OBJECT WITH ROWS AND COLUMN WITH ALL VALUES AS 0
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.data=[]

        #MAKES ARRAY OF ROW AND COLUMN WITH VALUE 1
        for i in range(self.row):
            self.data.append([])
            for j in range(self.col):
                self.data[i].append(1)

    #RETURNS THE DATA OF MATRIX AS A LIST
    def ToList(self):
        temp=[]
        for i in range(self.row):
            temp.append([])
            for j in range(self.col):
                temp[i].append(self.data[i][j])
        return temp



    #TO RANDOMIZE THE ELEMENTS OF A MATRIX BETWEEN THE -1 to 1
    def randomize(self,**kwargs ):
        start=-10
        end=10
        if kwargs:
            start=kwargs["start"]
            end=kwargs["end"]

        for i in range(self.row):
            for j in range(self.col):
                self.data[i][j] = random.uniform(start,end)

    # SCALAR MULTIPLICATION, IF N=LIST THEN ELEMENTARY MULTIPLICATION
    def multiply(self,n):
        if type(n)==Matrix:
            n=n.ToList()
        if type(n)==list :


            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] *= n[i][j]
            #IF THERE IS A ERROR HERE IT MUST BE BECAUSE OF THE DIMENSION OF DATA AND N NOT BEING SAME
        else:
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j]*=n

    # SCALAR ADDITION, IF N=LIST THEN ELEMENTARY ADDITION
    def add(self,n):
        if type(n)==Matrix:

            n=n.ToList()


        if type(n)==list:
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j] += n[i][j]
            #IF THERE IS A ERROR HERE IT MUST BE BECAUSE OF THE DIMENSION OF DATA AND N NOT BEING SAME
        else:
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j]+=n

    def subtract(self,n):
        if type(n)==Matrix:

            n=n.ToList()

        result=Matrix(col=self.col,row=self.row)

        if type(n)==list:
            for i in range(self.row):
                for j in range(self.col):
                   result.data[i][j] = self.data[i][j] -n[i][j]

            return result
            #IF THERE IS A ERROR HERE IT MUST BE BECAUSE OF THE DIMENSION OF DATA AND N NOT BEING SAME
        else:
            for i in range(self.row):
                for j in range(self.col):
                    self.data[i][j]-=n

    #CROSS PRODUCT OF MATRIX RETURNS A MATRIX OBJECT
    def cross(self,n):
        if type(n)!=Matrix:
            print("N MUST BE A MATRIX OBJECT IN CROSS")
            return
        if self.col!= n.row:
            print("COL OF A NOT EQUAL TO ROWS OF B IN CROSS")
            return
        else:
            result=Matrix(self.row,n.col)

            for i in range(result.row):
                for j in range(result.col):
                    for k in range(self.col):
                        result.data[i][j]+=self.data[i][k]*n.data[k][j]
        return result

    #TRANSPOSE THE GIVEN MATRIX AND RETURN NEW MATRIX OBJECT WITH THE TRANSPOSE
    def transpose(self):
        result= Matrix(self.col,self.row)
        for i in range(self.row):
            for j in range(self.col):
                result.data[j][i]+=self.data[i][j]
        return result

    #TAKES A FUNCTION AND APPLIES IT TO EACH ELEMENT OF A MATRIX
    def sigmoid(self):
        try:
            #print(self.data,"before sig")
            for i in range(0, self.row):
                for j in range(0, self.col):
                    self.data[i][j] = 1 / (1 + math.exp(-self.data[i][j]))
            #print(self.data, "after sig")
        except:

            for i in range(0, self.row):
                for j in range(0, self.col):
                    self.data[i][j] = float(self.data[i][j])


    def dsigmoid(self):
        for i in range(self.row):
            for j in range(self.col):
                self.data[i][j]*=(1-self.data[i][j])
    def tanh(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.data[i][j] =math.tanh(self.data[i][j])
    def dtanh(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.data[i][j] =1-(self.data[i][j])**2

    def send_output(self):
        output=[]
        for i in range(len(self.data)):
            output.append(self.data[i][0])
        return output


def ToMatrix(n):
    result=Matrix(len(n),1)

    for i in range(len(n)):
        result.data[i]=[n[i]]

    return result


