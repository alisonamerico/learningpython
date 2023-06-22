# 1 - Start a new Python script by initializing a dictionary then display its
# key:value contents:

dict = { 'name' : 'Bob' , 'ref' : 'Python' , 'sys' : 'Win' }
print( 'Dictionary:' , dict )

# 2 - Next, display a single value referenced by its key
print( '\nReference:' , dict[ 'ref' ] )

# Now, display all keys within the dictionary
print( '\nKeys:' , dict.keys() )

# 3 - Delete one pair from the dictionary and add a replacement pair then
# display the new key:value contents:
del dict[ 'name' ]
dict[ 'user' ] = 'Tom'
print( '\nDictionary:' , dict )

# 4 - Finally, search the dictionary for a specific key and display the result of
# the search:

print( '\nIs There A name Key?:' ,'name' in dict )