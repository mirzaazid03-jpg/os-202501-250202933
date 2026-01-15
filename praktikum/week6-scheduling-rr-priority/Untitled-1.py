import turtle

t = turtle. turtle()
s = turtle. screen()

s.bgcolor('#262626')
t.pencolor('magneta')
t.speed(100)

col = ('cyan', 'yellow', 'red', 'light green')

for n in range (10):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.penzize(2)
            t.circle(80+n*20,90)
            t.it(45)
        t.pencolor(col[n%4])
    s.exitonclick()
    turtle.done
