import turtle as t
t.speed('fastest')
t.fd(300) #center divider
t.bk(600)
t.fd(300)
t.lt(90)
t.fd(300)
t.bk(600)


t.rt(90) #box guidelines
t.bk(300)
for i in range(4):
  t.fd(600)
  t.lt(90)
t.pu()
t.goto(200,200)
t.pd()
t.rt()
t.fd(100)
