#!/usr/bin/python3

class Number():
    """ An enriched number to allow for a more intuitive syntax."""
    mmethods = ['add', 'sub', 'mul', 'floordiv', 'truediv', 'mod', 'pow']
    boolmmethods = [ 'lt', 'le', 'eq', 'ne', 'ge', 'gt' ]

    def __init__(self, value):
        self.value = value
    
    @property
    def hundred(self):
        return Number(self.value * 100)

    @property
    def thousand(self):
        return Number(self.value * 1000)
    
    def __str__(self):
        return str(self.value)

    def operation(self, mmethod):
        op = mmethod
        def do_operation(s, o):
            try:
                return Number(op(s.value, o.value))
            except AttributeError:
                return Number(op(s.value, o))
        return do_operation

    def bool_op(self, mmethod):
        op = mmethod
        def do_operation(s, o):
            try:
                return op(s.value, o.value)
            except AttributeError:
                return op(s.value, o)
        return do_operation
    
    def __repr__(self):
        return self.__str__()


for m in Number.mmethods:
    setattr(Number, "__"+m+"__", Number.operation(Number, int.__dict__["__"+m+"__"]))
for m in Number.boolmmethods:
    setattr(Number, "__"+m+"__", Number.bool_op(Number, int.__dict__["__"+m+"__"]))


class Calculator():
    """ A calculator that uses fluent syntax.

    There are only four operations that are supported (plus, minus, times,
    divided_by) and 10 digits (zero, one, two, three, four, five, six, seven,
    eight, nine).

    Each calculation consists of one operation only and will return an
    integer.
    
    """
    numbers = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14,
        'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
        'twenty':20, 'thirty':30, 'fourty':40, 'fifty':50, 'sixty':60,
        'seventy':70, 'eighty':80, 'ninety':90, } 

    def __init__(self):
        self.new

    def __print__(self):
        return str(self.result)

    def __repr__(self):
        return str(self.result)

    def __lt__(self, other):
        return self.result < other

    def __le__(self, other):
        return self.result <= other

    def __eq__(self, other):
        return self.result == other

    def __ne__(self, other):
        return self.result != other

    def __ge__(self, other):
        return self.result >= other

    def __gt__(self, other):
        return self.result > other

    @property
    def result(self):
        if self.operand and self.operation and self.operator:
            return self.operation()
        if self.operation is None:
            return self.operand

    @property
    def new(self):
        """ resets the calculator """
        self.clean()
        return self

    def clean(self):
        self.operand = None
        self.operator = None
        self.operation = None

    def back(self):
        if self.operator:
            self.operator = None
            return
        if self.operation:
            self.operation = None
            return
        self.operand = None

    def compose_number(self, value):
        if self.operation is None:
            if self.operand != None and (self.operand%10 == 0) and value < self.operand:
                self.operand += value
                return
        else:
            if self.operator != None and self.operator %10 == 0 and value < self.operator:
                self.operator += value
                return
        raise FluentSyntaxError({
            'message': "You may only set one operand and one operator. Perhaps there is a missing 'new'.",
            'operand': self.operand,
            'operator': self.operator,
            'new number': value
            })
            

    def number(value):
        """ Creates a function for each number."""
        def n(self):
            """ Number function.
            
            This is the core of the calculator.  It returns either the
            calculator itself or the resulting number if all operand, operator
            and operation are set.  It raises custom errors upon failed
            validation of the fluent syntax.

            We have one of these functions for each number.
            """
            if self.operation is None:
                if self.operand is None:
                    self.operand = value
                    return self
            else:
                if self.operator is None:
                    self.operator = value
                    return self
            self.compose_number(value)
            return self
        return n
    
    def accumulate(self):
        self.operand = self.result
        self.operation = None
        self.operator = None
    
    @property
    def plus(self):
        """ Sets the operation to addition. """
        if self.operator is not None:
            self.accumulate()
        if self.operation is None:
            self.operation = self.addition
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operation': self.operation, 'new operation': 'plus'})

    @property
    def minus(self):
        """ Sets the operation to subtraction. """
        if self.operator is not None:
            self.accumulate()
        if self.operation is None:
            self.operation = self.subtraction
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operator': self.operator, 'operation': self.operation, 'new operation': 'minus'})

    @property
    def times(self):
        """ Sets the operation to multiplication. """
        if self.operator is not None:
            self.accumulate()
        if self.operation is None:
            self.operation = self.multiplication
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operation': self.operation, 'new operation': 'times'})

    @property
    def divided_by(self):
        """ Sets the operation to division. """
        if self.operator is not None:
            self.accumulate()
        if self.operation is None:
            self.operation = self.division
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operation': self.operation, 'new operation': 'divided_by'})

    def addition(self):
        return self.operand + self.operator

    def subtraction(self):
        return self.operand - self.operator

    def multiplication(self):
        return self.operand * self.operator
    
    def division(self):
        """ allows for division by zero errors.

        This will have the sambe behaviour of a regular calculator"""
        return self.operand // self.operator

    @property
    def hundred(self):
        if self.operator:
            self.operator *= 100
        else:
            self.operand *= 100
        return self

    @property
    def thousand(self):
        if self.operator:
            self.operator *= 1000
        else:
            self.operand *= 1000
        return self

for name, value in Calculator.numbers.items():
    setattr(Calculator, name, Calculator.number(Number(value)))
    setattr(Calculator, name, property(Calculator.__dict__[name]))




class FluentSyntaxError(Exception):
    """ A custom error for fluent syntax calculator errors."""
    pass



Cal = Calculator()

