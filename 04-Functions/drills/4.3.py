import math

def triangle_area(a,b,c):
    p = (a+b+c)/2
    area = math.sqrt(p * (p - a) * (p - b) * (p-c))
    return area

a = int(input("what's a? "))
b = int(input("what's b? "))
c = int(input("what's c? "))


area = triangle_area(a, b, c)
print('The area of ​​a triangle with sides sqrt(x) {}, {}, {} is {:g}'.format(a, b, c, area) )
