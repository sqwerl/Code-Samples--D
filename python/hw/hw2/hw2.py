"""Submission for 61A Homework 2.

Name: Lawrence Cao
Login: cs61a-gw
Collaborators:
"""
from operator import add, mul, sub 

# Q1
def product(n, term):
    """Return the product of the first n terms in a sequence.
    
    term -- a function that takes one argument
    """
    total, k = 1, 1
    while k<=n:
        total, k = total * term(k), k+1
    return total

def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    return product(n, lambda x: x)

# Q2
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence.
    
    combiner -- a function that takes in two arguments
    start -- base value
    n -- end value
    term -- a function that takes in one argument
    """
    
    total, k = start, 1
    while k <= n:
        total, k = combiner(total, term(k)), k+1
    return total

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate."""
    
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate."""
    
    return accumulate(mul, 1, n, term)


# Q3
def double(f):
    """Return a function that applies f twice.
    
    f -- a function that takes one argument
    """
    
    return lambda x: f(f(x))


# Q4
def repeated(f, n):
    """Return the function that computes the nth application of f.
    
    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    """
    k = n-1
    h = lambda x: f(x)
    while k >= 1:
        h = compose1(f, h)
        k -= 1
    
    return h

def square(x):
    """Return x squared."""
    return x * x

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

# Q5 (Extra)
def zero(f):
    """Church numeral 0."""
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1."""
    return successor(zero)(f)

def two(f):
    """Church numeral 2."""
    return successor(one)(f)

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n."""
    
    return lambda f: lambda x: m(f)(n(f)(x))

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(add_church(two, two))
    4
    """
    "*** YOUR CODE HERE ***"

    return (n)(lambda x: x+1)(0)
