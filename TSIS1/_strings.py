''' Assign string to a variable '''
a = "Hello"
print(a)
''' Multiline Strings '''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

''' Strings are arrays'''
a = "Hello, World!"
print(a[1]) # e  

''' LOOPING THROUGH A STRING '''
for x in "banana":
    print(x)    # b
                # a
                # n
                # a
                # n
                # a
                
''' STRING LENGTH '''
a = "Hello, World!"
print(len(a)) # 13

''' CHECKING STRING '''
txt = "The best things in ife are free!"
# is the string -> "free" has inside of txt?!
print("free" in txt) # True
if "free" in txt:
    print("Yes, 'free' is present")

''' CHECK IF NOT '''
txt = "The best things in ife are free!"
print("expensive" not in txt) # True
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

''' SLICING '''
b = "Hello, World!"
print(b[2:5]) # llo
# slicing from the start
print(a[:5]) # Hello
# slicing to the end
print(a[2:]) # llo, World!
''' NEGATIVE INDEXING '''
b = "Hello, World!"
print(b[-5:-2]) #orl

''' MODIFY STRINGS '''
# Upper case
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!

# Lower case
print(a.lower()) # hello, world!

# Remove Whitespace
a = " Hello,World! "
print(a.strip()) # "Hello, World!"

# Replace string
a = "Hello, World!"
print(a.replace('H', 'J')) # Jello, World!
 
# Split string
a = "Hello, World!"
print(a.split(",")) # ['Hello', 'World!']


''' STRING CONCATENATION '''
a = "Hello"
b = "Nursat"
c = a + " " + b
print(c) # Hello Nursat  



