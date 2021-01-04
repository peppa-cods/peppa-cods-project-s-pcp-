import turtle as t
t.fillcolor("red");t.begin_fill();
for x in range(4):
	t.fd(100)
	t.rt(90)
t.end_fill();t.fillcolor("green");t.begin_fill();t.bk(10)
for x in range(3):
	t.fd(120)
	t.lt(120)
t.end_fill()