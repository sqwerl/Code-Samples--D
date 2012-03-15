"""Submission for CS61A Homework 5.

Name: Lawrence Cao
Login: cs61a-gw
Collaborators:
"""

from ucb import main, interact
from copy import deepcopy

# Q1.

def reverse_list1(L):
	"""Reverse the contents of L and return None. (Use a loop)"""
	
	for i in range(len(L)):
		L.insert(i,L.pop(len(L)-1))
		


def reverse_list2(L):
	"""Reverse the contents of L and return None. (One assignment)"""
	L[:] = L[::-1]
	
	


# Q2

def make_account(balance):
	"""A new bank account with initial balance `balance`. 
	If acc is an account returned by make_account, then
	acc('balance') returns the current balance.
	acc('deposit', d) deposits d cents into the account
	acc('withdraw', w) withdraws w cents from the account, if
		possible.
	'deposit' and 'withdraw' return acc itself.
	>>> acc = make_account(1000)
	>>> acc('balance')
	1000
	>>> acc('deposit', 10)('balance')
	1010
	>>> acc('withdraw', 200)('balance')
	810
	"""
	B = [balance]
	def fn(action, amount = 0,):
		if action == 'balance':
			return B[0]
		elif action == 'deposit':
			B[0] = B[0] + amount
			
			return make_account(B[0])
		elif action == 'withdraw':
			
			B[0] = B[0] - amount
			return make_account(B[0])
	return fn

# Q3.

def shuffle(r):
	"""Interleave the first half of rlist R with the second half.
	The resulting list starts with the first item of the original R,
	then the middle item, then the second item, then the item after 
	the middle, etc.  If R contains an odd number of items, the extra
	one is in the first half and goes on the end of the resulting list.
	Nondestructive: does not disturb the original list.
	>>> L = [0, 1, 2, 3, 4, 5, 6, 7]
	>>> R = shuffle(L)
	>>> L
	[0, 1, 2, 3, 4, 5, 6, 7]
	>>> R
	[0, 4, 1, 5, 2, 6, 3, 7]
	"""
	S = r[:]
	if len(S) > 1:
		S[1::2] = r[round(len(r)/2):]
		S[::2] = r[:round(len(r)/2)]
	return S

# Q4.

import re

class Life(object):
	"""A representation of a position in J.H. Conway's Game of Life."""

	def __init__(self, starting_board):
		"""Initialize SELF to the position depicted in the string STARTING_BOARD.
		STARTING_BOARD has the form "xxxxx\nxxxxx\nxxxxx..." where each x is
		either '.' or '*', and the newlines separate rows.	The number of x's
		in each row must be equal.	Leading and trailing whitespace
		is ignored."""

		# Represent a board as a list of lists of single characters, one list
		# per row, and within each row, one character per column.  B0[r][c]
		# represents the current contents of row #R, column #C of the board,
		# numbering from 1.	 Row 1, column 1 is the upper left.
		# The first row (#0) and last (#self.H-1) row and first (#0) and last
		# and last (#self.W-1) column are added at initialization, and should
		# be kept permanently at '.' (this reduces the number of special
		# cases in the neighbor computation).
		# self.H: number of rows (including top and bottom "desert" rows)
		# self.W: number of columns (including left and right desert columns)
		# self.B0: current board.
		# self.B1: extra board.
		starting_board = starting_board.strip()
		if not re.match(r'[.*\n]*$', starting_board):
			raise ValueError("board contains invalid characters")
		
		A = starting_board.split('\n')
		
		if len(A) == 0 or len(A[0]) == 0:
			raise ValueError("board too small")
		self.H = len(A)+2
		self.W = len(A[0])+2

		if any(map(lambda row: len(row) != self.W-2, A)):
			raise ValueError("board is irregular")

		self.B0 = [ ['.'] * self.W ] + \
				  [ ['.'] + list(s) + ['.'] for s in A ] + \
				  [ ['.'] * self.W ]
		self.B1 = [ ['.'] * self.W for i in range(self.H) ]

	def advance(self):
		"""Advance SELF's board to the next turn."""
		for r in range(1, self.H-1):
			for i in range(1, self.W-1):
				neighbors = 0
				if self.B0[r-1][i-1] == '*':
					neighbors += 1
				if self.B0[r-1][i] == '*':
					neighbors += 1
				if self.B0[r-1][i+1] == '*':
					neighbors += 1
				if self.B0[r][i-1] == '*':
					neighbors += 1
				if self.B0[r][i+1] == '*':
					neighbors += 1
				if self.B0[r+1][i-1] == '*':
					neighbors += 1
				if self.B0[r+1][i] == '*':
					neighbors += 1
				if self.B0[r+1][i+1] == '*':
					neighbors += 1
				if neighbors == 3:
					self.B1[r][i] = '*'
				elif neighbors == 2 and self.B0[r][i] == '*':
					self.B1[r][i] = '*'
				else:
					self.B1[r][i] = '.'
		self.B0 = deepcopy(self.B1)
		

	def printable(self, empty=" ", occupied="*"):
		"""A printable representation of SELF, using EMPTY for unoccupied
		squares and OCCUPIED for occupied ones."""
		return "\n".join([ "".join(map(lambda c: empty if c == '.' else occupied,
									   row[1:-1]))
						   for row in self.B0[1:-1] ])

	def __str__(self):
		"""String representation returned by str(SELF)."""
		return self.printable()

# A couple of standard initialization strings for playing around.

GLIDER = """\
................
..*.............
...*............
.***............
................
................
................
................
"""

PULSAR = """\
....................
......***...***.....
....................
....*....*.*....*...
....*....*.*....*...
....*....*.*....*...
......***...***.....
....................
......***...***.....
....*....*.*....*...
....*....*.*....*...
....*....*.*....*...
....................
......***...***.....
...................."""


def run_life(board, n):
	"""Assuming BOARD is a Life object, print it and advance by N turns,
	printing each step."""
	print("Step 0")
	print(str(board))
	print()
	for i in range(n):
		print("Step", i+1)
		board.advance()
		print(str(board))
		print()

# Mutable rlists.

empty_rlist = None

def make_rlist(first, last = None):
	return [first, last]

def first(r):
	return r[0]
def rest(r):
	return r[1]

def set_first(r, new_first):
	r[0] = new_first
def set_rest(r, new_rest):
	r[1] = new_rest

def rlist(*items):
	"""A new rlist consisting of ITEMS."""
	result = empty_rlist
	for i in range(1, len(items)+1):
		result = make_rlist(items[-i], result)
	return result

def rlist_to_list(r):
	"""The standard Python list containing the same items as R."""
	result = []
	while r != empty_rlist:
		result.append(first(r))
		r = rest(r)
	return result

# Q5. 

def dfilter_rlist(pred, r):
	"""Remove all items in R for which PRED returns a false value, returning
	the rlist of the remaining items.  Destructive: does not use
	make_rlist (or create new lists by other means either).
	>>> L = rlist(0, 1, 2, 4, 5, 7)
	>>> R = dfilter_rlist(lambda x: x%2 == 0, L)
	>>> R
	[0, [2, [4, None]]]
	>>> L
	[0, [2, [4, None]]]
	"""
	
	
	if pred(first(r)) == False:
		if rest(r) is not empty_rlist:
			r[:] = rest(r)
			dfilter_rlist(pred, r)
		else:
			del r[:]
	elif pred(first(rest(r))) == False:
		
		if r[1] is not empty_rlist:
			r[1] = rest(rest(r))
			dfilter_rlist(pred, r)
	else:
		if rest(rest(r)) != None:
			dfilter_rlist(pred, rest(r))
	
		
	return r
		

# Q6. Extra for experts.

def dshuffle_rlist(r):
	"""Interleave the first half of rlist R with the second half.
	The resulting list starts with the first item of the original R,
	then the middle item, then the second item, then the item after 
	the middle, etc.  If R contains an odd number of items, the extra
	one is in the first half and goes on the end of the resulting list.
	Destructive: does not use make_rlist (or create new lists by 
	other means either).  Returns the modified list.
	>>> L = rlist(0, 1, 2, 3, 4, 5, 6, 7)
	>>> R = dshuffle_rlist(L)
	>>> rlist_to_list(L)
	[0, 4, 1, 5, 2, 6, 3, 7]
	>>> rlist_to_list(R)
	[0, 4, 1, 5, 2, 6, 3, 7]
	>>> L = rlist(0, 1, 2, 3, 4, 5, 6)
	>>> R = dshuffle_rlist(L)
	>>> rlist_to_list(L)
	[0, 4, 1, 5, 2, 6, 3]
	>>> rlist_to_list(R)
	[0, 4, 1, 5, 2, 6, 3]
	"""
	"*** YOUR CODE HERE ***"

@main
def run():
	interact()


