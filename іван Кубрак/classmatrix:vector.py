class matrix :
    def __init__(self, file="x.txt") :
        self.matr = []
        for row in file :
            count_=0
            for s in row:
                if s.isdigit():
                    count_ += 1
            if count_ == 0:
                continue
            else :
                row = row.split ()# робить з рядка список
                for i in range (len(row)) :
                    row[i]= int (row[i]) # робить з рядка число
                self.matr.append (row)
        if len(self.matr) == 0:
            return
        
        if len(self.matr) == 1 or len(self.matr[0]) == 1:
            print ("it is vector")
        if  len(self.matr[0]) == 1:
            l=[]
            for i in range(len(self.matr)):
                l.append( self.matr[i][0])
            self.matr = l
        if  len(self.matr) == 1:
            l=[]
            for i in range(len(self.matr[0])):
                l.append( self.matr[0][i])
            self.matr = l
           

    def __str__(self):
        s = "\n"
        if type(self.matr[0]) == int:
            s += " ".join(str(self.matr[i]) for i in range(len(self.matr))) + "\n" # кожне число перетворюєм в рядок та всі елементи зливаєм
        else:
            for i in range(len(self.matr)):
                s += " ".join(str(self.matr[i][j]) for j in range(len(self.matr[i]))) + "\n" # кожне число перетворюєм в рядок та всі елементи зливаєм
        return s
    
    '''
def matrixadd (self , matr1 , matr2) : 
        resmatr = []
        for i in range (len(matr1)) :
            row = []
            for j in range (len(matr1[0])) :
                row.append (matr1[i][j] + matr2[i][j])
            resmatr.append(row)
        return resmatr
    '''

    def __add__(self, m) :# перевантажений оператор додавання матриці
        try:
            if type(self.matr[0]) == int and type(m.matr[0]) == int:
                res= matrix()
                for i in range (len(self.matr)) :
                    res.matr.append(self.matr[i] + m.matr[i])
                return res

            elif len(self.matr) == len(m.matr) and len(self.matr[0]) == len(m.matr[0]):
                        
                res= matrix()
                for i in range (len(self.matr)) :
                    row=[]
                    for j in range (len(self.matr[0])) :
                        row.append(self.matr[i][j] + m.matr[i][j])
                    res.matr.append(row)
                return res
            else :
              raise Exception
    
    
        except Exception:
            print('Matrices have  different sizes')
            exit()

      
    def __sub__(self, m) :# перевантажений оператор додавання матриці
        try:
            if type(self.matr[0]) == int and type(m.matr[0]) == int:
                res= matrix()
                for i in range (len(self.matr)) :
                    res.matr.append(self.matr[i] - m.matr[i])
                return res

            elif len(self.matr) ==len(m.matr) and len(self.matr[0]) == len(m.matr[0]):
                        
                res= matrix()
                for i in range (len(self.matr)) :
                    row = []
                    for j in range (len(self.matr[0])) :
                        row.append (self.matr[i][j] - m.matr[i][j])
                    res.matr.append(row)
                return res
            else :
               raise Exception

    
        except Exception:
            print('Matrices have  different sizes')
            exit()
    

        



    
    
file = open("matr1.txt","r")
x = matrix (file)
print(x)
file2 = open("matr2.txt","r")
y = matrix (file2)
print ('\n',y)
#print(len(x.matr), len(y.matr), len(x.matr[0]), len(y.matr[0]))
z = x + y
print(z)
z = x - y
print(z)

file3 = open("vector1.txt","r")
x1 = matrix (file3)
print (x1)
file4 = open("vector2.txt","r")
y1 = matrix (file4)

print ('\n',y1)

#print(len(x1.matr), len(y1.matr))
z = x1 + y1
print(z)
z = x1 - y1
print(z)

