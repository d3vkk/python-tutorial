#LEARNING PYTHON v3.7

print("LEARNING PYTHON v3.7")

print ("\n\nSTRINGS")
str = 'Hello World!'
print (str) # Prints complete string
print (str[0]) # Prints first character of the string
print (str[2:5]) # Prints characters starting from 3rd to 5th
print (str[2:]) # Prints string starting from 3rd character
print (str * 2) # Prints string two times
print (str + "TEST") # Prints concatenated string

print ("\n\nLISTS")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # Prints complete list
print (list[0]) # Prints first element 'of the list
print (list[1:3]) # Prints elements starting from 2nd till 3rd
print (list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (list + tinylist) # Prints concatenated lists

print ("\n\nTUPLES: Read-Only Lists")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (tuple) # Prints complete list
print (tuple[0]) # Prints first element of the list
print (tuple[1:3]) # Prints elements starting from 2nd till 3rd
print (tuple[2:]) # Prints elements starting from 3rd element
print (tinytuple * 2) # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

print ("\n\nDICTIONARY")
dictionary = {}
dictionary['one'] = "This is one"
dictionary[2] = "This is two"
tinydictionary = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydictionary) # Prints complete dictionary
print (tinydictionary.keys()) # Prints all the keys
print (tinydictionary.values()) # Prints all the values

print ("\n\nARITHMETIC")
a = 21
b = 10
c = 0
c = a + b
print ("Line 1 - Value of c is ", c)
c = a - b
print ("Line 2 - Value of c is ", c)
c = a * b
print ("Line 3 - Value of c is ", c)
c = a / b
print ("Line 4 - Value of c is ", c)
c = a % b
print ("Line 5 - Value of c is ", c)
a = 2
b = 3
c = a**b
print ("Line 6 - Value of c is ", c)
a = 10
b = 5
c = a//b
print ("Line 7 - Value of c is ", c)

print ("\n\nIF... ELSE STATEMENT")
a = 2
b = 3
if a == b:
    print ("Equal")
else:
    print ("Not Equal")

print("\n\nCHECK EDITOR FOR MORE DETAILS")