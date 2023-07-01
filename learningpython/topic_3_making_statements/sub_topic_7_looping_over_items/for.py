# 1 - Start a new Python script by initializing a list, a tuple, and a dictionary:

chars = [ 'A' , 'B', 'C' ]
fruit = ( 'Apple' , 'Banana' , 'Cherry' )
dict = { 'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' }

# 2 - Next, add statements to display all list element values:
print( '\nElements:\t' , end = ' ' )
for item in chars :
    print( item , end = ' ' )

# 3 - Now, add statements to display all list element values and their relative
# index number:
print( '\nEnumerated:\t' , end = ' ' )
for item in enumerate( chars ) :
    print( item , end = ' ' )

# 4 - Then, add statements to display all list and tuple elements:
print( '\nZipped:\t' , end = ' ' )
for item in zip( chars , fruit ) :
    print( item , end = ' ' )

# 5 - Finally, add statements to display all dictionary key names and associated
# element values:
print( '\nPaired:' )
for key , value in dict.items() :
    print( key , '=' , value )