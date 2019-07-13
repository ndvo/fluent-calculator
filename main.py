#!/usr/bin/python3



class Calculator():
    """ A calculator that uses fluent syntax.

    There are only four operations that are supported (plus, minus, times,
    divided_by) and 10 digits (zero, one, two, three, four, five, six, seven,
    eight, nine).

    Each calculation consists of one operation only and will return an
    integer.
    
    """
    numbers = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
            }

    def __init__(self):
        self.new

    @property
    def new(self):
        """ resets the calculator """
        self.operand = None
        self.operator = None
        self.operation = None
        return self

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
            if not (self.operand is None or self.operator is None):
                raise FluentSyntaxError({
                    'message': "You may only set one operand and one operator. Perhaps there is a missing 'new'.",
                    'operand': self.operand,
                    'operator': self.operator,
                    'new number': value
                    })
            if not self.operand is None and self.operation is None:
                raise FluentSyntaxError({
                    'message': "You may only set the operator once the operation is set.",
                    'operand' : self.operand,
                    'new number': value
                    })
            if self.operand is None and self.operation is None and self.operator is None:
                self.operand = value
            if not self.operand is None and not self.operation is None and self.operator is None:
                self.operator = value
                # resets the calculator to improve usability, making the new
                # operator optional except inside a chain
                result = self.operation()
                self.new
                return result
            return self
        return n

    @property
    def plus(self):
        """ Sets the operation to addition. """
        if self.operation is None:
            self.operation = self.addition
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operation': self.operation, 'new operation': 'plus'})

    @property
    def minus(self):
        """ Sets the operation to subtraction. """
        if self.operation is None:
            self.operation = self.subtraction
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operation': self.operation, 'new operation': 'minus'})

    @property
    def times(self):
        """ Sets the operation to multiplication. """
        if self.operation is None:
            self.operation = self.multiplication
            return self
        raise FluentSyntaxError({'message': 'Operation was already set', 'operation': self.operation, 'new operation': 'times'})

    @property
    def divided_by(self):
        """ Sets the operation to division. """
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


for name, value in Calculator.numbers.items():
    setattr(Calculator, name, Calculator.number(value))
    setattr(Calculator, name, property(Calculator.__dict__[name]))


class FluentSyntaxError(Exception):
    """ A custom error for fluent syntax calculator errors."""
    pass



Cal = Calculator()

