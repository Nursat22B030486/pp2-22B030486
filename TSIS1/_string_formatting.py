''' USING format() '''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) # My name is John, and I am 36


quantity = 3
itemno = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars"
myorder = "I want {2} pieces of item {0} for {1} dollars"
print(my_order.format(quantity, itemno, price))
# and we can control order
print(myorder.format(quantity, itemno, price))

''' ESCAPE CHARACTER '''
txt = "We are the so-called \" Viking \" from the north"
''' other escape characters:
        \'
        \\
        \n
        \r
        \t
        \b
        \f
        \ooo
        \xhh

'''