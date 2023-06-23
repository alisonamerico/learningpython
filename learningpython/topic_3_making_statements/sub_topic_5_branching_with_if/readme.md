# Branching with if

The Python if keyword performs the basic conditional test that evaluates a given
expression for a Boolean value of True or False. This allows a program to proceed
in different directions according to the result of the test, and is known as
'conditional branching'.
The tested expression must be followed by a : colon, then statements to be
executed when the test succeeds should follow below on separate lines, and each
line must be indented from the if test line. The size of the indentation is not
important, but it must be the same for each line. So the syntax looks like this:

```py
if test-expression :
statements-to-execute-when-test-expression-is-True
statements-to-execute-when-test-expression-is-True
```
Optionally, an if test can offer alternative statements to execute when the test
fails by appending an else keyword after the statements to be executed when the
test succeeds. The else keyword must be followed by a : colon and aligned with
the if keyword, but its statements must be indented in a likewise manner, so its
syntax looks like this:

```py
if test-expression :
    statements-to-execute-when-test-expression-is-True
    statements-to-execute-when-test-expression-is-True
else :
    statements-to-execute-when-test-expression-is-False
    statements-to-execute-when-test-expression-is-False
```
An if test block can be followed by an alternative test using the elif keyword
('else if ') that offers statements to be executed when the alternative test
succeeds. This too must be aligned with the if keyword, followed by a : colon,
and its statements indented. A final else keyword can then be added to offeralternative
 statements to execute when the test fails. The syntax for the complete
if-elif-else structure looks like this:

```py
if test-expression-1 :
    statements-to-execute-when-test-expression-1-is-True
    statements-to-execute-when-test-expression-1-is-True
elif test-expression-2 :
    statements-to-execute-when-test-expression-2-is-True
    statements-to-execute-when-test-expression-2-is-True
else :
    statements-to-execute-when-test-expressions-are-False
    statements-to-execute-when-test-expressions-are-False
```
## Beware
Indentation of code is very important in Python as it identifies code blocks to the
interpreter – other programming languages use braces.

## Don't forget
The `if: elif: else:` sequence is the Python equivalent of the switch or case
statements found in other languages.