import math

class Triangle:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        if len(self.points) < 3:
            self.points.append(point)
        else:
            print("A triangle can only have three points.")

    def perimeter(self):
        if len(self.points) == 3:
            a, b, c = self.side_lengths()
            print("Perimeter is : {} ".format(a + b + c))
        else:
            print("A triangle must have three points to calculate the perimeter.")
            return 0

    def side_lengths(self):
        if len(self.points) == 3:
            a = math.dist(self.points[0], self.points[1])
            b = math.dist(self.points[1], self.points[2])
            c = math.dist(self.points[2], self.points[0])
            return a, b, c

    # def is_equal(self, other_triangle):
    #     if len(self.points) == 3 and len(other_triangle.points) == 3:
    #         if sorted(self.points) == sorted(other_triangle.points):
    #             print("Triangles {} and {} are equal".format(self.points,other_triangle.points))
    #         else:
    #             print("Triangles {} and {} are not equal".format(self.points,other_triangle.points))
    #     else:
    #         print("Both triangles must have three points to compare.")
    def __eq__ (self, other_triangle):
        if len(self.points) == 3 and len(other_triangle.points) == 3:
            if sorted(self.points) == sorted(other_triangle.points):
                print("Triangles {} and {} are equal".format(self.points,other_triangle.points))
            else:
                print("Triangles {} and {} are not equal".format(self.points,other_triangle.points))
        else:
            print("Both triangles must have three points to compare.")



t1 = Triangle()
t1.add_point((0, 0))
t1.add_point((0, 3))
t1.add_point((4, 0))
t1.perimeter()



t2 = Triangle()
t2.add_point((1, 2))
t2.add_point((2, 1))
t2.add_point((1, 5))
t2.perimeter()


t3 = Triangle()
t3.add_point((1, 2))
t3.add_point((2, 1))
t3.add_point((1, 5))


# t2.is_equal(t3)
# t1.is_equal(t3)

t1.__eq__(t3)