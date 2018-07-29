import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)
		
def draw_cirgle(some_turtle):	
	some_turtle.circle(100)

def draw_triangle(some_turtle):
	for i in range(1,4):
		nani.forward(100)
		nani.right(360 / 3)

	window.exitonclick()


def draw_stuff(n = int(input()):
	window = turtle.Screen()	
	window.bgcolor("red")
	#Create the turtle Brad - Draws a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(3)
	for i in range(1,360/n):
		draw_square(brad)
		brad.right(n)
	window.exitonclick()

draw_stuff()