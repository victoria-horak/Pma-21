from Matrix import Matrix
from Vector import Vector
import Constants
vector1 = Vector("""

  2 3       5 6
   4 5 8     7



9 4 5 6

""")
vector2 = Vector().fromFile(Constants.PATH + "matrix.txt")
print(vector1 + vector2)
