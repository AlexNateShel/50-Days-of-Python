# Day 46

### Create a _DataFrame_ using pandas. You are going to create code to put the following into a DataFrame. You will use the information in the table below. Basically, you are going to recreate this table using pandas. Use the information in the table to recreate the table.
|year          |Title        |genre         |
| :---         | :---        | :---         |
|2009          |Brothers     |Drama         |
|2002          |Spider-Man   |Sci-fi        |
|2009          |WatchMen     |Drame         |
|2010          |Inception    |Sci-fi        |
|2009          |Avatar       |Fantasy       |
# Extra Challenge: Website Data with Pandas

### Create a code that extracts data from a website. You will extract a table from the website. And from that table, you will extract comlumns about the data types in Python and their mutability. You will extract information from the following website:
### https://en.wikipedia.org/wiki/Python_(programming_language)
### The following table is what you will extract from the website.
|Type                     | Mutability |   Description                                                                          |Syntax examples           |
| :---                    | :---       | :---                                                                                   | :---                      
|bool                     |immmutable  |Boolean Value |True  False |
|bytearray                |mutable     |Sequnce of bytes | bytearray(b'Some ASCII')
bytearray(b"Some ASCII")
bytearray([119, 105, 107, 105])
|bytes                    |immutable   |Sequence of bytes |
|complex                  |immutable   |Complex number with real and imaginary parts |
|dict                     |mutable     |Associative array (or dictionary) of key and value pairs; can contain mixed types (keys and values), keys must be a hashable type |
|types.EllipsisType       |immutable   |An ellipsis placeholder to be used as an index in NumPy arrays |
|float                    |immutable   |Double-precision floating-point number. The precision is machine-dependent but in practice is generally implemented as a 64-bit IEEE 754 number with 53 bits of precision.[107] |
|frozenset                |immutable   |Unordered set, contains no duplicates; can contain mixed types, if hashable |
|int                      |immutable   |Integer of unlimited magnitude[108] |
|list                     |mutable     |List, can contain mixed types |
|types.NoneType           |immutable   |An object representing the absence of a value, often called null in other languages |
|types.NotImplementedType |Immutable   |A placeholder that can be returned from overloaded operators to indicate unsupported operand types. |
|range                    |immutable   |An immutable sequence of numbers commonly used for looping a specific number of times in for loops[109] |
|set                      |mutable     |Unordered set, contains no duplicates; can contain mixed types, if hashable |
|str                      |immutable   |A character string: sequence of Unicode codepoints |
|tuple                    |immutable   |Can contain mixed types |
### Once you extract this table, you will write a code that will extract the data types and their mutability (Two columns). Here is how your ouput should look: