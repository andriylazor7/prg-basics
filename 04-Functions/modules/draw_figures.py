import turtle


def draw_square(length):
  # Set up the screen

  # Create the turtle
  turtle.speed(5)

  # Draw a square
  for i in range(4):
      turtle.forward(length)
      turtle.right(90)

  # Hide the turtle and finish
  turtle.hideturtle()

def draw_triangle(length):
    turtle.penup()
    turtle.goto(-length / 2, 0) 
    turtle.pendown()
    turtle.setheading(60)  

    for _ in range(3):
        turtle.forward(length)
        turtle.right(120) 

    turtle.hideturtle()  


def draw_rectangle(length_a, length_b):
    turtle.penup()
    turtle.goto(-300, 300) 
    turtle.pendown()
    turtle.setheading(0)  

    for _ in range(2):
        turtle.forward(length_a)  
        turtle.right(90)
        turtle.forward(length_b)  
        turtle.right(90)

    turtle.hideturtle() 


  
  
  