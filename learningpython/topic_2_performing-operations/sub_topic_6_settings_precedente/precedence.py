# Start a new Python script by initializing three variables with integer
# values for precedence comparison:
a = 2
b = 4
c = 8
print('\na = 2')
print('b = 4')
print('c = 8')

# Next, add statements to display the results of default precedence and
# forcing addition before multiplication:
print( '\nDefault Order:\t', a, '*', c,'+', b, '=', a * c + b )
print( 'Forced Order:\t', a, '* (', c,'+', b, ') =', a * ( c + b ) )

# Now, add statements to display the results of default precedence and
# forcing subtraction before division:
print( '\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a )
print( 'Forced Order:\t', c, '// (', b,'-', a, ') =', c // ( b - a ) )

# Finally, add statements to display the results of default precedence and
# forcing addition before modulo operation and before exponent operation:
print( '\nDefault Order:\t', c, '%', a, '+', b, '=', c % a + b )
print( 'Forced Order:\t', c, '% (', a, '+', b, ') =', c % ( a + b ) )
print( '\nDefault Order:\t', c, '**', a, '+', b, '=', c ** a + b )
print( 'Forced Order:\t', c, '** (', a, '+', b, ') =', c ** ( a + b ) )
