
# Online Python - IDE, Editor, Compiler, Interpreter
import math

def get_min_max(points):
    xmin = points[0][0]
    xmax = points[0][0]
    ymin = points[0][1]
    ymax = points[0][1]
    
    for p in points:
        if p[0] < xmin:
            xmin = p[0]
        elif p[0] > xmax:
            xmax = p[0]
        if p[1] < ymin:
            ymin = p[1]
        elif p[1] > ymax:
            ymax = p[1]
    
    return (xmin,xmax,ymin,ymax)

def rect_int_area(rect):
    xmin, xmax, ymin, ymax = rect
    xmin = math.ceil(xmin)
    ymin = math.ceil(ymin)
    xmax = math.floor(xmax)
    ymax = math.floor(ymax)
    
    return (xmax-xmin+1)*(ymax-ymin+1)
    
def triangle_int_area(p1,p2,slope):
    
    
rect = get_min_max([(0.1,0.1),(3.1,5.1)])
print(rect_int_area(rect))

