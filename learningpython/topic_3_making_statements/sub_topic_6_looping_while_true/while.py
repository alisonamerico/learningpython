# 1 - Start a new Python script by initializing a “counter” variable and define
# an outer loop using that variable in its test expression

i=1
while i < 4:

# 2 - Next, add indented statements to display the counter’s value and
# increment its value on each iteration of the loop

    print('\nOuter Loop Iteration:' , i)
    i += 1

# 3 - Now, (still indented) initialize a second “counter” variable and define an
# inner loop using this variable in its test expression

j=1
while j < 4 :

# 4 - Finally, add further-indented statements to display this counter’s value
# and increment its value on each iteration

    print('\tInner Loop Iteration:' , j)
    j += 1