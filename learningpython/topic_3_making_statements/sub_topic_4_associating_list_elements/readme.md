# Associating list elements

In Python programming a "dictionary" is a data container that can store multiple
items of data as a list of key:value pairs. Unlike regular list container values,
which are referenced by their index number, values stored in dictionaries are
referenced by their associated key. The key must be unique within that
dictionary, and is typically a string name although numbers may be used.
Creating a dictionary is simply a matter of assigning the key:value pairs as a
comma-separated list between curly brackets (braces) to a name of your choice.
Strings must be enclosed within quotes, as usual, and a : colon character must
come between the key and its associated value.
A key:value pair can be deleted from a dictionary by specifying the dictionary
name and the pair’s key to the `del` keyword. Conversely, a key:value pair can be
added to a dictionary by assigning a value to the dictionary’s name and a new
key.

Python dictionaries have a `keys()` method that can be dot-suffixed to the dictionary
name to return a list, in random order, of all the keys in that dictionary. If you
prefer the keys to be sorted into alphanumeric order, simply enclose the
statement within the parentheses of the Python `sorted()` function.
A dictionary can be searched to see if it contains a particular key with the Python
in operator, using the syntax `key in dictionary`. The search will return a Boolean `True`
value when the key is found in the specified dictionary, otherwise it will return
`False`.

Dictionaries are the final type of data container available in Python
programming. In summary, the various types are:

• **Variable** – stores a single value.

• **List** – stores multiple values in an ordered index.

• **Tuple** – stores multiple fixed values in a sequence.

• **Set** – stores multiple unique values in an unordered collection.

• **Dictionary** – stores multiple unordered key:value pairs.

## Hot tip

In other programming languages a list is often called an "array" and a dictionary
is often called an "associative array".

Data is frequently associated as key:value pairs – for example, when you submit
a web form, a text value typed into an input field is typically associated with that
text field’s name as its key.
