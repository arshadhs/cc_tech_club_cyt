import turtle

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        turtle.color(c)
        turtle.forward(steps)
        turtle.right(30)

turtle.mainloop()
