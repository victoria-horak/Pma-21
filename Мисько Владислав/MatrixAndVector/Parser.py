def ParseRow(thelist):
        array = []
        currentNumber = 0
        flag = False
        for element in thelist:
            if (element != ' ' and element != '\n'):
                currentNumber *= 10
                flag = True
                currentNumber += int(element)
            else: 
                if (flag):
                   array.append(int(currentNumber))
                currentNumber = 0
                flag = False
        if (thelist[thelist.__len__() - 1] != '\n' and thelist[thelist.__len__() - 1] != ' '):
            array.append(currentNumber)
        return array
