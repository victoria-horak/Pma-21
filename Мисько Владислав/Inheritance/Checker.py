class Checker:
    
    def check_sides_of_triangle(a, b, c):
        if c >= a + b or a >= b + c or b >= a + c or Checker.check_side(a) or Checker.check_side(b) or Checker.check_side(c):
            return False
        else:
            return True

    def check_side(a):
        return a <= 0

