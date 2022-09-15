
def fibonachi(first = 0, second = 1,length=1,fibonachiLine = ""):
  if length<0:
    raise ValueError("Length cannot be negative")
  if(len(fibonachiLine) == 0):
    fibonachiLine += str(first) +", "
    fibonachiLine += str(second) +", "
  next = first + second
  fibonachiLine+= str(next) + ", "  
  return fibonachi(second,next,length-1,fibonachiLine) if length > 1 else fibonachiLine[:-2]

try:
  print(fibonachi(0,3,4),"\n")
  print(fibonachi(0,1,-2))
except ValueError as e:
 print(e)