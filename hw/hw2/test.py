a = 1


def f():
    global a
    a = 0

b = f()

print(a)

def g():
    global a
    a = 2

f = g()

print(a)
