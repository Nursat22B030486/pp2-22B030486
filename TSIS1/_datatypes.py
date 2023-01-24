'''
    DATA TYPES
        text type: str;
        numeric types: int, float, complex;
        sequence types: list(["apple", "banana", "cherry"]), 
        tuple(("apple", "banana", "cherry")), range(6);
        Mapping types: dict ( {"name" : "John", "age" : 36});
        Set types: set({"apple", "banana", "cherry"}), 
        frozenset(frozenset({"apple", "banana", "cherry"}));
        Boolean type: bool;
        Binary type: bytes(b"Hello"), bytearray(bytearray(5)),
        memoryview(memoryview(bytes(5)));

'''
# GETTING THE DATA TYPE
x = 5
print(type(x)) # <class 'int'>

x = "Hello world " # str
x = 20	# int
x = 20.5	# float
x = 1j	# complex
x = ["apple", "banana", "cherry"]	# list
x = ("apple", "banana", "cherry")	# tuple
x = range(6)	# range 
x = {"name" : "John", "age" : 36}	# dict
x = {"apple", "banana", "cherry"}	# set
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = True	# bool
x = b"Hello"	# bytes
x = bytearray(5)	# bytearray	
x = memoryview(bytes(5))	# memoryview	
x = None	# NoneType

