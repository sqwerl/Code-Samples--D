"""Submission for CS61A Homework 6.

Name: Lawrence Cao
Login: cs61a-gw
Collaborators:
"""

# Q1 (and part of Q2).

class Bank:
	"""A Bank capable of creating accounts."""

	
	def __init__(self):
		self.total = 0
	
	def make_account(self, balance):
		self.total += balance
		return Account(self, balance)
	
	def make_secure_account(self, balance, password):
		self.total += balance
		return SecureAccount(self, balance, password)
	
	def total_deposits(self):
		return self.total

class Account:
	""" An account in a particular bank.

	>>> third_national = Bank()
	>>> second_federal = Bank()
	>>> acct0 = third_national.make_account(1000)
	>>> acct0.withdraw(100)
	>>> acct1 = third_national.make_account(2000)
	>>> third_national.total_deposits()
	2900
	>>> second_federal.total_deposits()
	0
	>>> acct1.total_deposits()
	Traceback (most recent call last):
	   ...
	AttributeError: 'Account' object has no attribute 'total_deposits'
	>>> acct1.bank().total_deposits()
	2900
	"""


	def __init__(self, bank, initial_balance):
		self.__balance = initial_balance
		self.__parentBank = bank
	
	def withdraw(self, amount):
		self.__balance -= amount
		self.__parentBank.total -= amount
		
	def deposit(self, amount):
		self.__balance += amount
		self.__parentBank.total += amount
	
	def balance(self):
		return self.__balance
		
	def bank(self):
		return self.__parentBank
	

# Q2

class SecurityError(BaseException):
	"""Exception to raise if there is an attempted security violation."""
	pass

class SecureAccount(Account):
	"""An account that provides password security.
	>>> third_national = Bank()
	>>> acct3 = third_national.make_secure_account(1000, "The magic woid")
	>>> acct3.deposit(1000, 'The magic woid')
	>>> acct3.balance('The magic woid')
	2000
	>>> acct3.balance('Foobar')
	Traceback (most recent call last):
	   ...
	hw6.SecurityError: wrong passphrase or account
	>>> acct3.balance()
	Traceback (most recent call last):
	   ...
	hw6.SecurityError: passphrase missing
	"""
	def __init__(self, bank, initial_balance, password = None):
		super().__init__(bank, initial_balance)
		self.__password = password
		
	def balance(self, password = None):
		if password == self.__password:
			return super(SecureAccount, self).balance()
		elif password == None:
			raise SecurityError('passphrase missing')
		else:
			raise SecurityError('wrong passphrase or account')
			
	def withdraw(self, amount, password = None):
		if password == self.__password:
			super(SecureAccount, self).withdraw(amount)
		elif password == None:
			raise SecurityError('passphrase missing')
		else:
			raise SecurityError('wrong passphrase or account')
			
	def deposit(self, amount, password = None):
		if password == self.__password:
			super(SecureAccount, self).deposit(amount)
		elif password == None:
			raise SecurityError('passphrase missing')
		else:
			raise SecurityError('wrong passphrase or account')
	


	

# Q3 and Q4



		
	
	

class rlist:
	"""A recursive list consisting of a first element and the rest.
	
	>>> s = rlist(1, rlist(2, rlist(3)))
	>>> len(s)
	3
	>>> s[0]
	1
	>>> s[1]
	2
	>>> s[2]
	3
	>>> for x in s:
	...		print(x)
	1
	2
	3
	"""
	class empty:
		
		class empty_rlist:
			def __len__(self):
				return 0
			# def __getitem__(self, k):
			# 	raise StopIteration
			def __repr__(self):
				return 'rlist.empty()'
		def __new__(self):
			return self.one
		one = empty_rlist()
			

		
	
		
	def __repr__(self):
		"""A printed representation of self that resembles a Python
		expression that reproduces the same list.  The builtin function
		repr(x) calls x.__repr__().	 The Python interpreter uses __repr__
		to print the values of non-null expressions it evaluates."""
		f = repr(self.first())
		if self.rest() is rlist.empty():
			return 'rlist({0})'.format(f)
		else:
			return 'rlist({0}, {1})'.format(f, repr(self.rest()))
	
	def __init__(self, first, rest = empty()):
		self.__first = first
		self.__rest = rest
		
	def __iter__(self):
		iterable = []
		for i in range(len(self)):
			iterable.append(self[i])
		return iter(iterable)
		
	def __next__(self):
		
		if len(self) == 0:
			raise StopIteration
		else:
			return self.pop(0)
			
	def __getitem__(self, k):
		
		
		if k != 0:
			return self.rest().__getitem__(k-1)
		else:
			return self.first()
		
	def __len__(self):
		return 1 + self.rest().__len__()
		
	def first(self):
		return self.__first
		
	def rest(self):
		return self.__rest	
		

	

# Q5.

class Monitor:
	"""A general-purpose wrapper class that counts the number of times each
	attribute of a monitored object is accessed.

	>>> B = Bank()
	>>> acct = B.make_account(1000)
	>>> mon_acct = Monitor(acct)
	>>> mon_acct.balance()
	1000
	>>> for i in range(10): mon_acct.deposit(100)
	>>> mon_acct.withdraw(20)
	>>> mon_acct.balance()
	1980
	>>> mon_acct.access_count('balance')
	2
	>>> mon_acct.access_count('deposit')
	10
	>>> mon_acct.access_count('withdraw')
	1
	>>> mon_acct.access_count('clear')
	0
	>>> L = list(mon_acct.attributes_accessed())
	>>> L.sort()
	>>> L
	['balance', 'deposit', 'withdraw']
	"""
	def __init__(self, monitered_object):
		self.__object = monitered_object
		self.__counts = {}
	def __getattr__(self, attr):
		
		self.__counts[attr] = self.__counts.get(attr, 0) + 1
		return getattr(self.__object, attr)
		
	def access_count(self, attr):
		return self.__counts.get(attr, 0)
	
	def attributes_accessed(self):
		return self.__counts.keys()
		
	

# Q6.

class Abbrev:
	"""An abbreviation map."""

	def __init__(self, full_names):
		"""Initialize self to handle abbreviations for the words
		in the sequence of strings full_names.	It is an error if
		a name appears twice in full_names."""
		self.__full_names = full_names
		for x in self.__full_names:
			if self.__full_names.count(x) >1:
				raise NameError('\'{0}\' appears twice in sequence'.format(x))

	def complete(self, cmnd):
		"""The member of my word list that the string cmnd
		abbreviates, if it exists and is unique.  cmnd abbreviates
		a string S in my word list if cmnd == S, or cmnd is a
		prefix of S and of no other command in my word list.
		Raises ValueError if there is no such S.
		>>> a = Abbrev(['continue', 'catch', 'next', 
		...				'st', 'step', 'command'])
		>>> a.complete('ne')
		'next'
		>>> a.complete('co')
		Traceback (most recent call last):
		   ...
		ValueError: not unique: 'co'
		>>> a.complete('st')
		'st'
		>>> a.complete('foo')
		Traceback (most recent call last):
		   ...
		ValueError: unknown command: 'foo'
		"""
		times = 0
		for x in self.__full_names:
			if cmnd == x[:len(cmnd)]:
				times += 1
				abbreviation = x
		if times == 1:
			return abbreviation
		elif cmnd in self.__full_names:
			return cmnd 
		elif times>1:
			raise ValueError('not unique: \'{0}\''.format(cmnd))
		else:
			raise ValueError('unknown command: \'{0}\''.format(cmnd))

	def minimal_abbreviation(self, cmnd):
		"""The string, S, of shortest length such that
		self.complete(S) == cmnd.  
		>>> a = Abbrev(['continue', 'catch', 'next', 
		...				'st', 'step', 'command'])
		>>> a.minimal_abbreviation('continue')
		'con'
		>>> a.minimal_abbreviation('next')
		'n'
		>>> a.minimal_abbreviation('step')
		'ste'
		>>> a.minimal_abbreviation('ste')
		Traceback (most recent call last):
		   ...
		ValueError: unknown command: 'ste'
		"""
		if cmnd not in self.__full_names:
			raise ValueError('unknown command: \'{0}\''.format(cmnd))
		for i in range(1, len(cmnd)):
			try:
				if self.complete(cmnd[:i]) == cmnd:
					return cmnd[:i]
			except:
				pass
	

# # Q7 Extra for Experts.
# 
# class ArgumentMonitor:
# 	"""A general-purpose wrapper class that counts the number of times each
# 	method of a monitored object is called with each unique argument list.
# 
# 	>>> B = Bank()
# 	>>> acct = B.make_account(1000)
# 	>>> mon_acct = ArgumentMonitor(acct, ['balance', 'withdraw', 'deposit'])
# 	>>> mon_acct.balance()
# 	1000
# 	>>> for i in range(10): mon_acct.deposit(100)
# 	>>> mon_acct.withdraw(20)
# 	>>> mon_acct.withdraw(10)
# 	>>> mon_acct.balance()
# 	1970
# 	>>> d = mon_acct.argument_counts('balance')
# 	>>> d[()]
# 	2
# 	>>> d = mon_acct.argument_counts('deposit')
# 	>>> list(d.items())
# 	[((100,), 10)]
# 	>>> d = mon_acct.argument_counts('withdraw')
# 	>>> d[(10,)]
# 	1
# 	>>> d[(20,)]
# 	1
# 	"""
# 
# 	def __init__(self, obj, operations):
# 		"""An ArgumentMonitor that monitors the methods named in
# 		operations for obj."""
# 		"*** YOUR CODE HERE ***"
# 
# 	"*** YOUR CODE HERE ***"


