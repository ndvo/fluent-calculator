# Fluent calculator

A Python3 module implementing a Fluent Syntax calculator

This small module was built as an exercise for a job interview.

It is a calculator that uses the "fluent syntax" as instructed in the exercise.


## Syntax

Both numbers and opperations are attributes of the calculator. To use it, chain them together.


## Usage:

### Simple operations

- kata.Cal.new.two.plus.two # returns 4
- kata.Cal.new.three.times.three # returns 9
- kata.Cal.new.three

### Hundreds and Thousands

- kata.Cal.new.two.hundred.times.three # returns 600
- kata.Cal.new.one.times.two.thousand # returns 2000

### Concatenating more than one operation

- kata.Cal.one.plus.two.times.three # returns nine

### Obtaining and reseting the current result

- kata.Cal.result
- kata.Cal.new

### Splitting an operation

1. kata.Cal.one # Returns None
1. pass # do something
1. kata.Cal.plus # Returns None
1. pass # do some other thing
1. kata.Cal.two # Returns three

### Several operations with hundreds 

- kata.Cal.one.hundred.twenty.five.times.two.plus.three # Returns 253
