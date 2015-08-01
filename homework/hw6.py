# CS 61A Fall 2014
# Name:
# Login:

class VendingMachine(object):
	"""A vending machine that vends some product for some price.

	>>> v = VendingMachine('candy', 10)
	>>> v.vend()
	'Machine is out of stock.'
	>>> v.restock(2)
	'Current candy stock: 2'
	>>> v.vend()
	'You must deposit $10 more.'
	>>> v.deposit(7)
	'Current balance: $7'
	>>> v.vend()
	'You must deposit $3 more.'
	>>> v.deposit(5)
	'Current balance: $12'
	>>> v.vend()
	'Here is your candy and $2 change.'
	>>> v.deposit(10)
	'Current balance: $10'
	>>> v.vend()
	'Here is your candy.'
	>>> v.deposit(15)
	'Machine is out of stock. Here is your $15.'
	"""
	"*** YOUR CODE HERE ***"

	def __init__(self, item, price):
		self.item = item
		self.price = price
		self.number = 0
		self.balance = 0

	def restock(self, num):
		self.number += num
		return 'Current {0} stock: {1}'.format(self.item, self.number)

	def vend(self):
		if self.number == 0:
			return 'Machine is out of stock.'
		else:
			if self.balance < self.price:
				return 'You must deposit ${0} more.'.format(self.price-self.balance)
			else:
				change = self.balance-self.price
				self.balance = 0
				self.number -= 1
				if change > 0:
					return 'Here is your {0} and ${1} change.'.format(self.item, change)
				else:
					return 'Here is your {0}.'.format(self.item)

	def deposit(self, money):
		if self.number > 0:
			self.balance += money
			return 'Current balance: ${0}'.format(self.balance)
		else:
			return 'Machine is out of stock. Here is your ${0}.'.format(money)


class MissManners(object):
	"""A container class that only forward messages that say please.

	>>> v = VendingMachine('teaspoon', 10)
	>>> v.restock(2)
	'Current teaspoon stock: 2'
	>>> m = MissManners(v)
	>>> m.ask('vend')
	'You must learn to say please first.'
	>>> m.ask('please vend')
	'You must deposit $10 more.'
	>>> m.ask('please deposit', 20)
	'Current balance: $20'
	>>> m.ask('now will you vend?')
	'You must learn to say please first.'
	>>> m.ask('please hand over a teaspoon')
	'Thanks for asking, but I know not how to hand over a teaspoon'
	>>> m.ask('please vend')
	'Here is your teaspoon and $10 change.'
	>>> really_fussy = MissManners(m)
	>>> really_fussy.ask('deposit', 10)
	'You must learn to say please first.'
	>>> really_fussy.ask('please deposit', 10)
	'Thanks for asking, but I know not how to deposit'
	>>> really_fussy.ask('please please deposit', 10)
	'Thanks for asking, but I know not how to please deposit'
	>>> really_fussy.ask('please ask', 'please deposit', 10)
	'Current balance: $10'
	>>> fussy_three = MissManners(3)
	>>> fussy_three.ask('add', 4)
	'You must learn to say please first.'
	>>> fussy_three.ask('please add', 4)
	'Thanks for asking, but I know not how to add'
	>>> fussy_three.ask('please __add__', 4)
	7
	"""
	"*** YOUR CODE HERE ***"
	def __init__(self, obj):
		self.obj = obj
	def ask(self, words, *args):
		words = words.split()
		if words[0] != 'please':
			return 'You must learn to say please first.'
		elif len(words) != 2 or not hasattr(self.obj, words[1]):
			res = 'Thanks for asking, but I know not how to'
			words = words[1:]
			for i in words:
				res += ' '+i
			return res
		else:
			return getattr(self.obj, words[1])(*args)


##########################################
#           Challenge Problem            #
# (You can delete this part if you want) #
##########################################

def make_instance(some_class):
	"""Return a new object instance of some_class."""
	def get_value(name):
		if name in attributes:
			return attributes[name]
		else:
			value = some_class['get'](name)
			return bind_method(value, instance)

	def set_value(name, value):
		attributes[name] = value

	attributes = {}
	instance = {'get': get_value, 'set': set_value}
	return instance

def bind_method(value, instance):
	"""Return value or a bound method if value is callable."""
	if callable(value):
		def method(*args):
			return value(instance, *args)
		return method
	else:
		return value

def make_class(attributes, base_classes=()):
	"""Return a new class with attributes.

	attributes -- class attributes
	base_classes -- a sequence of classes
	"""
	"*** YOUR CODE HERE ***"
	def get_value(name):
		if name in attributes:
			return attributes[name]
		else:
			for c in mro():
				if c['has'](name):
					return c['get'](name)
	def set_value(name, value):
		attributes[name] = value
	def new(*args):
		return init_instance(cls, *args)
	def bases():
		return base_classes
	def has(name):
		return name in attributes

	def mro():
		res = base_classes
		now = base_classes
		tmp = []
		while not now:
			for i in now:
				tmp += [j for j in i['mro']() if j not in res]
			now = tmp
			res += tmp
			tmp = []
		return res

	cls = {'get': get_value, 'set': set_value, 'new': new, 'bases': bases, 'has': has}
	return cls


def init_instance(some_class, *args):
	"""Return a new instance of some_class, initialized with args."""
	instance = make_instance(some_class)
	init = some_class['get']('__init__')
	if init:
		init(instance, *args)
	return instance

# AsSeenOnTVAccount example from lecture.

def make_account_class():
	"""Return the Account class, which has deposit and withdraw methods."""

	interest = 0.02

	def __init__(self, account_holder):
		self['set']('holder', account_holder)
		self['set']('balance', 0)

	def deposit(self, amount):
		"""Increase the account balance by amount and return the new balance."""
		new_balance = self['get']('balance') + amount
		self['set']('balance', new_balance)
		return self['get']('balance')

	def withdraw(self, amount):
		"""Decrease the account balance by amount and return the new balance."""
		balance = self['get']('balance')
		if amount > balance:
			return 'Insufficient funds'
		self['set']('balance', balance - amount)
		return self['get']('balance')

	return make_class(locals())

Account = make_account_class()

def make_checking_account_class():
	"""Return the CheckingAccount class, which imposes a $1 withdrawal fee.

	>>> checking = CheckingAccount['new']('Jack')
	>>> checking['get']('interest')
	0.01
	>>> checking['get']('deposit')(20)
	20
	>>> checking['get']('withdraw')(5)
	14
	"""
	interest = 0.01
	withdraw_fee = 1

	def withdraw(self, amount):
		fee = self['get']('withdraw_fee')
		return Account['get']('withdraw')(self, amount + fee)

	return make_class(locals(), [Account])

CheckingAccount = make_checking_account_class()

def make_savings_account_class():
	"""Return the SavingsAccount class, which imposes a $2 deposit fee.

	>>> savings = SavingsAccount['new']('Jack')
	>>> savings['get']('interest')
	0.02
	>>> savings['get']('deposit')(20)
	18
	>>> savings['get']('withdraw')(5)
	13
	"""
	deposit_fee = 2

	def deposit(self, amount):
		fee = self['get']('deposit_fee')
		return Account['get']('deposit')(self, amount - fee)

	return make_class(locals(), [Account])

SavingsAccount = make_savings_account_class()

def make_as_seen_on_tv_account_class():
	"""Return an account with lots of fees and a free dollar.

	>>> such_a_deal = AsSeenOnTVAccount['new']('Jack')
	>>> such_a_deal['get']('balance')
	1
	>>> such_a_deal['get']('interest')
	0.01
	>>> such_a_deal['get']('deposit')(20)
	19
	>>> such_a_deal['get']('withdraw')(5)
	13
	"""
	def __init__(self, account_holder):
		self['set']('holder', account_holder)
		self['set']('balance', 1)

	return make_class(locals(), [CheckingAccount, SavingsAccount])

AsSeenOnTVAccount = make_as_seen_on_tv_account_class()



