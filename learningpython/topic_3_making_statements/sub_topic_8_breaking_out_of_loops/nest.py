# 1 - Start a new Python script with a statement creating a loop that iterates
# three times:

for i in range( 1, 4 ) :

# 2 - Next, add an indented statement creating a “nested” inner loop that also
# iterates three times:

    for j in range( 1, 4 ) :

# 3 - Now, add a further-indented statement in the inner loop to display the
# counter numbers (of both the outer loop and the inner loop) on each:
# iteration of the inner loop:

        print( 'Running i=' , i , ' j=' , j )

# 4 - Save the file in your scripts directory, then open a Command Prompt
# window there and run this program – to see the counter values on each
# loop iteration.

# Hot tip
# Compare these nested for loops with the nested while loops example here.


# 5 - Now, insert this break statement at the very beginning of the inner loop
# block, to break out of the inner loop – then save the file and run the
# program once more:
    if i == 2 and j == 1 :
        print( 'Breaks inner loop at i=2 j=1' )
        break

# The Python continue keyword can be used to skip a single iteration of a loop when
# a specified condition is met. The continue statement is situated inside the loop
# statement block and is preceded by a test expression. When the test returns True,
# that one iteration ends and the program proceeds to the next iteration.


# 6 - Insert this continue statement at the beginning of the inner loop block, to
# skip the first iteration of the inner loop – then save the file and run the
# program again:
    if i == 1 and j == 1 :
        print( 'Continues inner loop at i=1 j=1' )
        continue

# Don't forget
# Here, the break statement halts all three iterations of the inner loop when the
# outer loop tries to run it the second time.

# Here, the continue statement just skips the first iteration of the inner loop whenthe outer loop tries to run it for the first time.