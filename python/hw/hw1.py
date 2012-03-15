from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b > 0:
        op = add
    else:
        op = sub
    return op(a, b)

def two_of_three(a, b, c):
    """Return x**2 + y**2, where x and y are the two largest of a, b, c."""
    return a**2 + b**2 + c**2 - min(a, b, c)**2

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result

def c():
    global x
    x = 1
    return False

def t():
    global x
    x = 0
    return x

def f():
    return x

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def hailstone(n):
    """Print the hailstone sequence starting at n, returning its length."""
    print(str(n).rstrip('.0'))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n/2)
    else:
        return 1 + hailstone(n*3+1)
