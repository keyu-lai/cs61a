## Extra Object-Oriented Programming questions ##

from lab06 import *

# Q6
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven’s money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
        money = check.withdraw(self.holder)
        if money is not None:
            return self.deposit(money)


class Check(object):
    "*** YOUR CODE HERE ***"
    def __init__(self, name, amount):
        self.deposited = False
        self.balance = amount
        self.holder = name

    def withdraw(self, name):
        if name == self.holder and self.deposited == False:
            tmp = self.balance
            self.balance = 0
            self.deposited = True
            return tmp
        else:
            print('The police have been notified.')

# Q7
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        "*** YOUR CODE HERE ***"
        self.buttons = {}
        for button in args:
            self.buttons[button.pos] = button

    def press(self, info):
        """Takes in a position of the button pressed, and 
        returns that button's output"""
        "*** YOUR CODE HERE ***"
        return self.buttons[info].press()

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and 
        returns the total output"""
        "*** YOUR CODE HERE ***"
        res = ''
        for i in typing_input:
            res += self.buttons[i].press()
        return res

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0

    def press(self):
        self.pressed += 1
        return self.key
