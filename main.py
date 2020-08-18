# Dianna Xu
# CS110A
# This will output 2 main types of shapes
# Input 4, then 100 to get a spiral with 

import turtle
totalsidestodraw = int(input("I will draw a series of rotated polygons. How many sides should each polygon have?"))
totalpolygonstodraw = int(input("How many of those polygons should I draw?"))
print("Please click on the 'result' tab above to see the drawing")
         
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  

for nPolygons in range(totalpolygonstodraw):         
    print("nPolygons = ", nPolygons)
    t.right(360/float(totalpolygonstodraw))
  
    for nSides in range(totalsidestodraw): 
      print("nSides = ", nSides)
      t.forward(100 + nPolygons)
      t.left(360/float(totalsidestodraw))

t2 = turtle.Turtle()
t2.speed(0)
t2 = turtle.Turtle()

for x in range(6):
  t2.up()
  t2.goto(-150 + 50*x, -200)
  t2.down()
  for w in range(0, 21, 2):
    t2.forward(5 + w)
    t2.left(90)

wn.exitonclick()
