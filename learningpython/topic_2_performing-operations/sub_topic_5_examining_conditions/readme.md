# Examining conditions

Many programming languages, such as C++ or Java, have a ?: “ternary” operator
that evaluates an expression for a True or False condition then returns
one of two specified values depending on the result of the evaluation.
A `?:` ternary operator has this syntax:
```java
( test-expression ) ? if-true-return-this : if-false-return-this
```
Unlike other programming languages, Python does not have a ?: ternary operator
but has instead a “conditional expression” that works in a similar way using
if and else keywords with this syntax:
```py
if-true-return-this if ( test-expression ) else if-false-return-this
```
Although the conditional expression syntax can initially appear confusing,
it is well worth becoming familiar with this expression as it can execute
powerful program branching with minimal code. For example, to branch when
a variable is not a value of one:
```py
if-true-do-this if ( var != 1 ) else if-false-do-this
```
The conditional expression can be used in Python programming to assign the
maximum or minimum value of two variables to a third variable. For example,
to assign a minimum like this:
```py
c = a if ( a < b ) else b
```
The expression in parentheses returns True when the value of variable `a` is
less than that of variable `b` – so in this case the lesser value of variable
a gets assigned to variable `c`.
Similarly, replacing the `<` less than operator in the test expression with
the `>` greater than operator would assign the greater value of variable `b`
to variable c.
Another common use of the conditional expression incorporates the `%` modulo
operator in the test expression to determine if the value of a variable is an
odd number or an even number:
```py
if-true(odd)-do-this if ( var % 2 != 0 ) else if-false(even)-do-this
```
Where the result of dividing the variable value by two does leave a remainder,
the number is odd – where there is no remainder, the number is even. The test
expression ( var % 2 == 1 ) would have the same effect but it is preferable to test for
inequality – it’s easier to spot when something is different than when it’s
identical.

## Hot tip
In general programming terms an “expression” always returns a value whereas a
“statement” need not – but a statement may include one or more expressions.

## Don't forget
The conditional expression has in effect three operands – the test expression and
two possible return values.

## Beware
You may find that some Python programmers dislike conditional expressions as
they consider their syntax contradicts the principle of easy readability.
