r = int(input())
g = int(input())
b = int(input())

if ((r != 255) and (g != 255) and (b != 255)) or ((r != 0) and (g != 0) and (b != 0)):
    if g > r < b:
        g = g-r
        b = b-r
        r = r-r
        print(r,g,b)
    elif r > g < b:
        r = r-g
        b = b-g
        g = g-g
        print(r,g,b)
    elif g > b < r:
        r = r-b
        g = g-b
        b = b-b
        print(r,g,b)
    else:
        print(0,0,0)