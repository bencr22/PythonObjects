from test import Circle



firstCircle = Circle(50, 50, 10)
secondCircle = Circle(30, 30, 8)

active = firstCircle

print(active.x)

active = secondCircle

print(active.x)
active.leftKeyPress()
