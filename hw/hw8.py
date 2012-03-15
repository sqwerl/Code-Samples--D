"""Submission for CS61A Homework 8.

Name: Lawrence Cao
Login: cs61a-gw
Collaborators:
"""
from ucb import*
# Copied from lecture.  

class Tree:
    """A Tree consists of a label and a sequence of 0 or more
    Trees, called its children."""

    def __init__(self, label, *children):
        """A Tree with given label and children.  For convenience,
        if children[k] is not a Tree, it is converted into a leaf
        whose operator is children[k]."""
        self.__label = label;
        self.__children = \
          [ c if type(c) is Tree else Tree(c) for c in children]

    @property
    def is_leaf(self):
        return self.arity == 0

    @property
    def label(self):
        return self.__label
    
    @property
    def children(self):
        return self.__children

    @property
    def arity(self):
        return len(self.__children)

    def __getitem__(self, k):
        return self.__children[k]

    def __iter__(self):
        return iter(self.__children)

    def __repr__(self):
        if self.is_leaf:
            return "Tree({0})".format(self.label)
        else:
            return "Tree({0}, {1})" \
               .format(self.label, str(self.__children)[1:-1])


# Q1.

from random import Random
from math import sqrt

def make_binary_tree(L, randoms = Random()):
    """Returns a binary tree, T, such that the labels of T in inorder (i.e.,
    keys in left child of T, followed by the label of T, followed
    by keys in the right child of T) are L.  The structure of the tree
    (which nodes are children of which) is determined randomly according to
    RANDOMS, an instance of Random.  An empty tree is represented as a
    Tree with a label of None."""
    if len(L) == 0:
        return Tree(None)
    else:
        left = randoms.randint(0, len(L)-1)
        return Tree(L[left], make_binary_tree(L[0:left], randoms),
                    make_binary_tree(L[left+1:], randoms))
    
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
          191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
          257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
          331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
          401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
          467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
          563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
          631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
          709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
          877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953,
          967, 971, 977, 983, 991, 997 )


PRIME_BINARY_TREE = make_binary_tree(PRIMES)

# Implement the following non-recursively:

def tree_find(T, x):
    """True iff x is a label in set T, represented as a search tree.
    That is, T 
       (a) Represents an empty tree if its label is None, or
       (b) has two children, both search trees, and all labels in 
           T[0] are less than T.label, and all labels in T[1] are 
           greater than T.label.
    >>> tree_find(PRIME_BINARY_TREE, 5)
    True
    >>> tree_find(PRIME_BINARY_TREE, 0)
    False
    >>> tree_find(PRIME_BINARY_TREE, 27)
    False
    >>> tree_find(PRIME_BINARY_TREE, 929)
    True
    >>> tree_find(PRIME_BINARY_TREE, 989)
    False
    """
    
    while True:
        if T.is_leaf:
            return False
        elif T.label == x:
            return True
        elif x < T.label:
            T = T[0]
        elif x > T.label:
            T = T[1]
        
        

# Q2.

def depth(T, x):
    """The depth, in any, at which x appears as a label in T.  Returns
    None if x is not in T.
    >>> T = Tree(1, Tree(3, Tree(4, 5, 6)))
    >>> depth(T, 1)
    0
    >>> depth(T, 5)
    3
    >>> depth(T, 10)   # Result is None
    """

    if T.label == x:
        return 0
    try:
        for c in range(T.arity):
            return 1 + depth(T[c], x) 
    except TypeError:
        return None

# Q3.

# Define a "general search tree" to be one whose labels are lists of keys
# such that

#  a. A node whose label is None represents an empty collection.
#  b. Otherwise, there is at least one key in a node label and
#     the keys are sorted in ascending order.
#  c. A non-empty node with *N* keys has *N+1* children, which are
#     also general search trees.
#  d. If x is key #k in a node's label, then all keys in child #k are 
#     less than x and all those in child #k+1 are greater than x.

def make_general_tree(L, randoms = Random()):
    """Returns a general search tree, T, containing the labels of L, assuming
    it is ordered.  The numbers of keys in each and subtree is decided
    randomly according to RANDOMS, an instance of random.Random."""
    if len(L) == 0:
        return Tree(None)
    else:
        arity = randoms.randint(1, int(sqrt(len(L))))
        key_indices = randoms.sample(range(0, len(L)), arity)
        key_indices.sort()
        keys = [ L[i] for i in key_indices ]
        children = [make_general_tree(L[0:key_indices[0]], randoms)] \
                   + [ make_general_tree(L[key_indices[i]+1:key_indices[i+1]],
                                         randoms)
                       for i in range(0, len(key_indices)-1) ] \
                   + [make_general_tree(L[key_indices[-1]+1:], randoms)]
        return Tree(keys, *children)

PRIME_GENERAL_TREE = make_general_tree(PRIMES)


def gen_tree_find(T, x):
    """True iff x is a label in set T, represented as a general
    search tree.
    >>> gen_tree_find(PRIME_GENERAL_TREE, 5)
    True
    >>> gen_tree_find(PRIME_GENERAL_TREE, 0)
    False
    >>> gen_tree_find(PRIME_GENERAL_TREE, 27)
    False
    >>> gen_tree_find(PRIME_GENERAL_TREE, 929)
    True
    >>> gen_tree_find(PRIME_GENERAL_TREE, 989)
    False
    """
    # (non-recursive version)
    while True:
        index = 0
        if T.is_leaf:
            return False
        for a in T.label:
            if x > a:
                index = T.label.index(a)+1
        if x in T.label:
            return True
        else:
            T = T[index]

# Q4.

def memoize(func):
    """Returns a function that takes the same arguments as 'func'
    and returns the same value, but with memoization.  That is, if
    f is the function returned by memoize(func), then f(v) returns
    func(v), but if f is called twice with the same arguments, v, it
    does not call func(v), but returns the previously returned value.
    We assume that 'func' is a pure function whose value depends only
    on the values of its arguments, and whose side-effects are irrelevant,
    and that the values of its argument, v, are of a type suitable for
    use as keys in a Python dictionary."""
    
    c = {}
    
    def f(*a):
        nonlocal c
        if a not in c.keys():
            c[a] = func(*a)
        return c[a]
    
    return f
    
def fib(x):
    print(x)
    if x <= 1:
        return 1
    else:
        return fib(x-2) + fib(x-1)

# Q5.

def checked_memoize(func):
    """Returns a function that takes the same arguments as 'func'
    and returns the same value, but with memoization.  That is, if
    f is the function returned by memoize(func), then f(v) returns
    func(v), but if f is called twice with the same arguments, v, it
    does not call func(v), but returns the previously returned value.
    We assume that 'func' is a pure function whose value depends only
    on the values of its arguments, and whose side-effects are irrelevant,
    and that the values of its argument, v, are of a type suitable for
    use as keys in a Python dictionary.  Raises a RuntimeError if a
    value of the arguments is encountered during the computation of the
    value of the function on those arguments."""
    
    c = {}
    d = []
    

    def f(*a):
        nonlocal c
        
        if a not in c.keys():
            c[a] = safe(func)(*a)
        return c[a]
        
    def safe(func):
        def f(*a):
            nonlocal d
            if a in d:
                raise RuntimeError
            else:
                d += [a]
                return func(*a)
        return f
        
        
    return f

  

# Q6.

empty_set = Tree(None)

def is_empty(T):
    return T.label is None

def adjoin_set(S, v):
    """Assuming S is a binary search tree representing a set (no
    duplicate values), the binary search tree representing the set
    S U {v}."""
    if S.label is None:
        return Tree(v, None, None)
    elif v < S.label:
        return Tree(S.label, adjoin_set(S[0], v), S[1])
    elif v == S.label:
        return S
    else:
        return Tree(S.label, S[0], adjoin_set(S[1], v))	

def adjoin_all(S, L):
    """The result of adding all the elements of L to set S, in order."""
    for v in L:
        S = adjoin_set(S, v)
    return S
    
import math

def bad(N):
    L = [a for a in range(N)]
    S = []
    for i in range((N+1)//2):
        S += [L[i]]
        if N % 2 != 1 or i != (N+1)//2 -1:
            S += [L[-i-1]]
    return S

def good(N):
    return [1]*N

# Q7. [Extra for experts]

def inorder_labels(T):
    """The non-null labels in T in inorder (labels in the left child,
    then the label of T, then labels in the right child)."""
    if T.label is None:
        return []
    else:
        return inorder_labels(T[0]) + [T.label] + inorder_labels(T[1])

def delete_set(S, v):
    """Assuming S is a binary search tree representing a set, a binary
    search tree representing the same set but with v removed (if
    it is present).  The result is the same as S if v is not present.
    >>> T = Tree(5, Tree(3, Tree(2, None, None), Tree(4, None, None)),
    ...             Tree(6, None, Tree(10, Tree(9, None, None),
    ...                                    Tree(13, None, None))))
    >>> inorder_labels(T)
    [2, 3, 4, 5, 6, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 7))
    [2, 3, 4, 5, 6, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 2))
    [3, 4, 5, 6, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 6))
    [2, 3, 4, 5, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 5))
    [2, 3, 4, 6, 9, 10, 13]
    """
    "*** YOUR CODE HERE ***"

# Q8. [Extra for experts]

def preorder(T):
    return preorder_iter(T)

class preorder_iter:
    """>>> T = Tree(1, Tree(2, Tree(3, 4, 5), 6), 7, 8)
    >>> list(preorder(T))
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    def __init__(self, tree):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        """Allow this iterator to be used after 'in' in a for loop."""
        return self

