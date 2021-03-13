import turtle
import random 
import matplotlib.pyplot as plt
import math

mypen = turtle.Turtle()
mypen.hideturtle()
mypen.speed(0)

mypen.up()
mypen.setposition(-100, -100)
mypen.down()
mypen.fd(200)
mypen.left(90)
mypen.fd(200)

mypen.left(90)
mypen.fd(200)
mypen.left(90)
mypen.fd(200)
mypen.left(90)

mypen.up()
mypen.setposition(0,-100)
mypen.down()
mypen.circle(100)


in_circle = 0
out_circle = 0

pi_values = []


for i in range(5):
    for j in range(1000):
        
        x = random.randrange(-100, 100)
        y = random.randrange(-100, 100)
        
        if(x**2 + y**2 > 100**2):
            mypen.color("black")
            mypen.up()
            mypen.goto(x,y)
            mypen.down()
            mypen.dot()
            out_circle = out_circle + 1
        else:
            mypen.color("red")
            mypen.up()
            mypen.goto(x,y)
            mypen.down()
            mypen.dot()
            in_circle = in_circle + 1
            
        pi = 4.0 * in_circle/  (in_circle +  out_circle)
        
        pi_values.append(pi)
        
        avg_pi_errors = [abs(math.pi - pi) for pi in pi_values]
        
        print(pi_values[-1])
        
        
        
plt.axhline(y = math.pi, color = 'g', linestyle='-')
plt.plot(pi_values)
plt.xlabel("Iterations")
plt.ylabel("Value of PI")
plt.show()

plt.axhline(y = 0.0, color = 'g', linestyle = '-')
plt.plot(avg_pi_errors)
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()
