# Start a new Python script by initializing two variables with integer values
# for conditional evaluation:
a = 1
b = 2
print('\na = 1')
print('b = 2')

# Next, add statements to display the results of conditional evaluation –
# describing the first variable’s value:
print( '\nVariable a Is :' , 'One' if ( a == 1 ) else 'Not One' )
print( 'Variable a Is :' , 'Even' if ( a % 2 == 0 ) else 'Odd' )

# Now, add statements to display the results of conditional evaluation –
# describing the second variable’s value:
print( '\nVariable b Is :' , 'One' if ( b == 1 ) else 'Not One' )
print( 'Variable b Is :' , 'Even' if ( b % 2 == 0 ) else 'Odd' )

# Then, add a statement to assign the result of a conditional evaluation to a
# new variable:
max = a if ( a > b ) else b

# Finally, add a statement to display the assigned result – identifying the
# greater of the two variable values:
print( '\nGreater Value Is:' , max )
