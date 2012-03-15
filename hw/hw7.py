"""Submission for CS61A Homework 7.

Name: Lawrence Cao
Login: cs61a-gw
Collaborators:
"""

# Q1.

def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    """
    def p(k, n):
        if k > n:
            return 0
        elif k == n:
            return 1
        else:
            return p(k+1, n) + p(k, n-k)
    if n == 0:
        return 1
    else:
        return p(1,n)

# Q2.

def g(n):
    """Return the value of g, defined 
          g(n) = n,                                       if n <= 3
          g(n) = g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3),  if n > 3 
    For integers n > 0.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of g, defined 
          g(n) = n,                                       if n <= 3
          g(n) = g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3),  if n > 3 
    For integers n > 0.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    total = n
    f = [1,2,3]
    while n > 3:
        total = f[-1] + 2*f[-2] + 3*f[-3]
        f = [f[-2], f[-1], total]
        n -= 1
    return total
# Q3.

def g_counted(n):
    """Return a tuple (g(n), cost(n)), where cost(n) is the number of times
    the recursive version of g is called during the computation of g(n).

    >>> g_counted(2)
    (2, 1)
    >>> g_counted(4)
    (10, 4)
    >>> g_counted(5)
    (22, 7)
    """
    count = 1
    def g(n):
        if n <= 3:
            return n
        else:
            nonlocal count
            count += 3
            return g(n-1) + 2*g(n-2) + 3*g(n-3)
    return g(n), count
        
    

# Q4.

from math import sqrt

class vect:
    """A vector in 2-dimensional Euclidean space.

    >>> v1 = vect(3, 4)
    >>> v1
    vect(3, 4)
    >>> print(v1)
    (3, 4)
    >>> v1.x
    3
    >>> v1.y
    4
    >>> v1.x = 7
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute
    >>> v1 * 3
    vect(9, 12)
    >>> 3 * v1
    vect(9, 12)
    >>> v2 = vect(4, -2)
    >>> v1 + v2
    vect(7, 2)
    >>> v1 - v2
    vect(-1, 6)
    >>> v1 * v2             # inner product = 12 - 8
    4
    >>> abs(v1)             # = sqrt(3**2 + 4**2)
    5.0
    """

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
    
    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
    
    def __repr__(self):
        return 'vect({0}, {1})'.format(self.x, self.y)
        
    def __mul__(self, other):
        if type(other) is int:
            other = vect(other, other)
            return vect(self.x*other.x, self.y*other.y)
        else:
            return self.x*other.x + self.y*other.y
        
    def __rmul__(self, other):
        return mul(self, other)
        
    def __add__(self, other):
        return vect(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return vect(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
# Q5.

def partm(n):
    """Return the number of partitions of positive integer n.

    >>> partm(5)
    7
    >>> partm(500)
    2300165032574323995027
    """

    memo = {}
    def p(k, n):
        if (k, n) in memo.keys():
            return memo[k, n]
        elif k > n:
            return 0
        elif k == n:
            return 1
        else:
            memo[k, n] = p(k+1, n) + p(k, n-k) 
            return p(k+1, n) + p(k, n-k)
    if n == 0:
        return 1
    else:
        return p(1,n)
    

## Q6.

class rlist:
    """A mutable recursive list."""

    empty = None

    def __init__(self, first, rest = empty):
        self.__first = first
        self.__rest = rest

    def first(r):
        return r.__first

    def rest(r):
        return r.__rest

    def set_first(r, new_first):
        r.__first = new_first
    def set_rest(r, new_rest):
        r.__rest = new_rest

    def rlist_to_list(r):
        """The standard Python list containing the same items as R."""
        result = []
        while r is not rlist.empty:
             result.append(r.first())
             r = r.rest()
        return result

def has_cycle(L):
    """True iff L is a circular rlist.

    >>> C = rlist(1, rlist(2, rlist(3)))
    >>> has_cycle(C)
    False
    >>> C.rest().rest().set_rest(C)
    >>> has_cycle(C)
    True
    >>> C = rlist(0, C)
    >>> has_cycle(C)
    True
    """
    memo = []
    def cycle(L):
        nonlocal memo
        memo += [L]
        if L.rest() in memo:
            return True
        elif L.rest() is not rlist.empty:
            return cycle(L.rest())
        else:
            return False
            
    return cycle(L)
## Q7.  Extra for experts

def has_cycle2(L):
    """True iff L is a circular rlist.

    >>> C = rlist(1, rlist(2, rlist(3)))
    >>> has_cycle2(C)
    False
    >>> C.rest().rest().set_rest(C)
    >>> has_cycle2(C)
    True
    >>> C = rlist(0, C)
    >>> has_cycle2(C)
    True
    """
    

## Q8.  Extra for experts

from operator import sub, mul

def fact_maker():
    "*** YOUR CODE HERE ***"
    return YOUR_CODE_HERE
"""
>>> fact_maker()(5)
120
"""

