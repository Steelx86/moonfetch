from math import sqrt

def draw_moon() -> None:
    radius = 10
    circle_eq = lambda x, y: abs(sqrt(x ** 2 + y ** 2))
    for y in range(-radius, radius +1):
        for x in range(-radius, radius + 1):
            if circle_eq(x, y) - radius < 0.5:
                print('#', end= '')
            else:
                print(' ', end= '')
    

#testing
draw_moon()
