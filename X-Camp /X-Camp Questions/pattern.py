import turtle as t 
t.penup()
t.bk(100)
t.pendown()
t.fd(20)
for x in range(5):
	t.lt(90);
	t.fd(20)
	for i in range(2):
		t.rt(90);
		t.fd(20)
	t.lt(90);
	t.fd(20)