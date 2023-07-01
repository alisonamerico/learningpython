# Looping over items

In Python programming, the `for` keyword loops over all items in any list specified
to the in keyword. This statement must end with a `:` colon character, and
statements to be executed on each iteration of the loop must be indented below,
like this:

```py
for each-item in list-name :
statements-to-execute-on-each-iteration
statements-to-execute-on-each-iteration
```
As a string is simply a list of characters, the `for in` statement can loop over each
character. Similarly, a `for in` statement can loop over each element in a list, each
item in a tuple, each member of a set, or each key in a dictionary.

A `for in` loop iterates over the items of any list or string in the order that they
appear in the sequence, but you cannot directly specify the number of iterations
to make, a halting condition, or the size of iteration step. You can, however, use
the Python `range()` function to iterate over a sequence of numbers by specifying a
numeric end value within its parameters. This will generate a sequence that starts
at zero and continues up to, but not including, the specified end value. For
example, `range(5)` generates 0,1,2,3,4.

Optionally, you can specify both a start and end value within the parentheses of
the `range()` function, separated by a comma. For example, `range(1,5)` generates
1,2,3,4. Also, you can specify a start value, end value, and a step value to the
`range()` function as a comma-separated list within its parentheses. For example,
`range(1,14,4)` generates 1,5,9,13.

You can specify the list’s name within the parentheses of Python’s `enumerate()`
function to display each element’s index number and its associated value.
When looping through multiple lists simultaneously, the element values of the
same index number in each list can be displayed together by specifying the list
names as a comma-separated list within the parentheses of Python’s `zip()`
function.

When looping through a dictionary you can display each key and its associated
value using the dictionary `items()` method and specifying two comma-separatedvariable names to the `for` keyword – one for the key name and the other for its
value.

## Don't forget
The `range()` function can generate a sequence that decreases, counting down, as
well as those that count upward.

## Beware
The for loop in Python is unlike that in other languages such as C, as it does not
allow step size and end to be specified.

## Hot tip
