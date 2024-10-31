# Object Oriented Programming
class cylinder:
    def __init__(self,radius,height, color):
        self.r = radius
        self.h = height
        self.rangi = color

    def calc_area(self, is_closed = True):
        if is_closed == True:
            area = 2 * 22/7 * self.r ** 2 + 2 * 22/7 * self.r * self.h
            print(f"Area of open cylinder is: {area}")
        else:
            area = 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            print(f"Area of closed cylinder is: {area}")

    def calc_volume(self):
        v = 22/7 * self.r ** 2 * self.h
        print(f"Volume of cylinder is: {v}")

c1 = cylinder(10, 11, "red")
c2 = cylinder(7.8, 22.6, "blue")
c1.calc_volume()
c1.calc_area(is_closed=False)