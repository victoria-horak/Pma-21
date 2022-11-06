class Arraylist :
    def __init__ (self, arrlist):
        self.arrlist = []
        for element in arrlist :
            self.arrlist.append(element)

    def __str__ (self):
        s = ""
        for element in self.arrlist:
            s += str(element)+", " # зробили список
        return s

    def read_from_file (self, file):
        for row in file :
            count_= 0
            for s in row:
                if s.isdigit():
                    count_ += 1
            if count_ == 0:
                continue
            else :
                row = row.split()# робить з рядка список
                for i in range (len(row)) :
                    row[i]= int (row[i]) # робить з рядка число
                    self.arrlist.append(row[i])

    def add_element (self, element):
        self.arrlist.append(element)

    def add_elements (self, *elements):
        for element in elements :
            self.arrlist.append(element)

    def remove_element (self, value):
        self.arrlist.remove(value)

    def remove_elements (self,*elements):
        for element in elements :
            elcount = self.arrlist.count(element)
            for i in range(elcount):
                self.arrlist.remove(element)
                

    

