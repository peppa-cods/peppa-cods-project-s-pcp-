import turtle as t
n = 50
for x in range(5):
	t.circle(x*n)
	t.pu()
	t.goto(0,0-(x*n))
	t.pd()