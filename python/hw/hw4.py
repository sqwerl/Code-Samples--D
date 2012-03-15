"""Submission for CS 61A Homework 4.

Name: Larry Cao
Login: cs61a-gw
Collaborators:
"""

# Q1.

# [This problem, as promised, held over from last week.]
# Submit a copy of your hw3.py solution with the this hw4.py file.

from hw3 import *

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0 

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = make_interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.
    
    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    lowerbound = 0
    upperbound = 0
    for i in seq:
        if non_zero(i):
            lowerbound += lower_bound(square_interval(i))
            upperbound += upper_bound(square_interval(i))
    return make_interval(lowerbound, upperbound)
        

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.
    
    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    return make_interval(reduce(add, map(lambda x: lower_bound(x)**2, filter(non_zero, seq))), reduce(add, map(lambda x: upper_bound(x)**2, filter(non_zero, seq))))

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.
    
    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    return make_interval(reduce(add, (lower_bound(x)**2 for x in seq if non_zero(x))), reduce(add, (upper_bound(x)**2 for x in seq if non_zero(x))))


# Definitions from lecture.

empty_rlist = None

def make_rlist(first, rest = empty_rlist):
    """A recursive list, r, such that first(r) is 'first' and 
    rest(r) is 'rest,'  which must be an rlist."""
    return first, rest

def first(r):
    """The first item in r."""
    return r[0]

def rest(r):
    """The tail of r."""
    return r[1]

def extend_rlist(left, right):
    """The sequence of items of rlist 'left' followed
    by the items of 'right'."""
    if left == empty_rlist:
         return right
    else:
         return make_rlist(first(left), 
                           extend_rlist(rest(left), right))
    
# Q2.

def is_tuple(x):
    return type(x) is tuple

def to_rlist(items):
    """The sequence of values in 'items', converted into a corresponding
    rlist.  Any tuples among the items also become rlists.
    >>> to_rlist((1, (0, 2), (), 3))
    (1, ((0, (2, None)), (None, (3, None))))
    """
    
    
    if len(items) == 0:
        return empty_rlist
    elif is_tuple(items[0]):
        return make_rlist(to_rlist(items[0]), to_rlist(items[1:]))
    else:
        return make_rlist(items[0], to_rlist(items[1:]))
  
        
# Q3.

def could_be_rlist(x):
    """Return true iff x might represent an rlist."""
    return x is None or type(x) is tuple

def to_tuple(L):
    """Assuming L is an rlist, returns a tuple containing the same
    sequence of values.
    >>> x = to_rlist((1, (0, 2), (), 3))
    >>> to_tuple(x)
    (1, (0, 2), (), 3)
    """
    if L is empty_rlist:
        return ()
    if not could_be_rlist(L):
        return L
    return (to_tuple(first(L)),) + to_tuple(rest(L))

    

# Q4.

def inserted_into_all(item, list_list):
    """Assuming that 'list_list' is an rlist of rlists, return the
    rlist consisting of the rlists in 'list_list', but with 
    'item' prepended as the first item in each.
    >>> L0 = to_rlist(((), (1, 2), (3,)))
    >>> L1 = inserted_into_all(0, L0)
    >>> to_tuple(L1)
    ((0,), (0, 1, 2), (0, 3))
    """
    if list_list is empty_rlist:
        return empty_rlist
    else:
	    return make_rlist(make_rlist(item, first(list_list)), inserted_into_all(item, rest(list_list)))
    

def subseqs(S):
    """Assuming that S is an rlist, return an rlist of all subsequences
    of S (an rlist of rlists).  The order in which the subsequences
    appear is unspecified.  
    >>> seqs = subseqs(to_rlist((1, 2, 3)))
    >>> show = list(to_tuple(seqs))   # Can only sort lists, not tuples
    >>> show.sort()
    >>> show
    [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
    """
    if S is empty_rlist:
        return empty_rlist
    else:
        return extend_rlist(subseqs(rest(S)), inserted_into_all(first(S), subseqs(rest(S))))

# Q5.

def inserted_into_all_tuples(item, tuple_tuple):
   """Assuming that 'tuple_tuple' is a tuple of tuples, return the
   tuple consisting of the tuples in 'tuple_tuple', but with 
   'item' prepended as the first item in each.
   >>> inserted_into_all_tuples(0, ((), (1, 2), (3, )))
   ((0,), (0, 1, 2), (0, 3))
   """
   return tuple(map(lambda x: ((item,)+x), tuple_tuple))

def subseqs_tuples(S):
   """Assuming that S is a tuple, return tuple of all subsequences
   of S (a tuple of tuples).  The order in which the subsequences
   appear is unspecified.  
   >>> seqs = subseqs_tuples((1, 2, 3))
   >>> show = list(seqs)
   >>> show.sort()
   >>> show
   [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
   """
   
   

# Q6.

def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("acme", "madam", "pivot", "pip"))
    2
    """
    return len(tuple(filter(lambda x: x.lower() == x[::-1].lower(), L)))


# Q7.

def alt_filter(pred, L):
    """The tuple containing all elements, x, of L such that pred(x).
    >>> alt_filter(lambda x: x%2 == 0, (0, 1, 3, 8, 4, 12, 13))
    (0, 8, 4, 12)
    """

    return reduce(add, map(lambda a, b: (b,) if a == True else (), map(pred, L), L))

# Q8.

def capitalize_sentences(S):
    """The sequence of words (strings) S, with all initial words in 
    sentences capitalized, and all others unchanged.  A word begins a 
    sentence if it is either the first word in S, or the preceding word 
    in S ends in a period.
    >>> capitalize_sentences(("see", "spot", "run.", "run", "spot", "run."))
    ('See', 'spot', 'run.', 'Run', 'spot', 'run.')
    """
    if len(S) == 0:
        return S
    return (S[0].capitalize(),) + tuple(map(lambda a,b : b.capitalize() if '.' in a else b, S, S[1:]))


        
# Q9.

def repeat(f, x, n):
     """Apply f to x n times.  When n is 0, the result is x; when n is
     1, the result is f(x); when n is 2, f(f(x)), etc.
     >>> repeat(lambda x: x+1, 1, 5)
     6
     """
     return reduce(lambda a,b: f(a), range(n), x)


# Q10.  Extra for experts.

"The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."
"quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."

def sortit(S):
    """The sequence of strings S sorted into lexicographic order 
    (the < operator).
    >>> sortit(("The", "quick", "brown", "fox", "jumps", "over", "the", "lazy",
    ...         "dog."))
    ('The', 'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the')
    """
    
    
    
