letters = ["a","b","c"]
for index, letter in enumerate(letters):
    print(index,letter)

letters.insert(0, -2)
print(letters)

#remove methods
letters.pop(1) # by default it removes the last item unless you specify the index
print (letters) 
letters.remove("b")# you can use this method if you dont know the index but the item
del letters[1:2] #removes a range of items fromt the list
print(letters)

letters.clear()# deletes all the objects
print(letters)

#find methods
letters = ["a","b","c"]
print(letters.count("z"))
if "d" in letters:
    print (letters.index("d"))

#sorting
numbers = [3, 51, 2, 8, 6]

numbers.sort(reverse=True) #This function modifies the original list
sorted(numbers)#This function does nots modify the original list
print (numbers)

#lets look at tuples

items = [
    ("product2",25),
    ("product1",5),
    ("product3",2)
]

def sort_item(item):
    return item[0]

items.sort(key=sort_item) #In this instance we are not calling the defined method we are only passing the method through"""
print (items)

#refractoring the above code
items = [
    ("product2",25),
    ("product1",5),
    ("product3",2)
]
#lambda parameter:expression
items.sort(key=lambda item:item[0] ) #In this instance we are not calling the defined method we are only passing the method through"""
print (items)

#mapping transforming our list list into a different list
#say we want to get a price list from items
items = [
    ("product2",25),
    ("product1",5),
    ("product3",2)
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

#refactor
prices= list(map(lambda item:item[1], items))
print (prices)

#filter

filtered= list(filter(lambda price:price[1]>=10,items))
print(filtered)

#list comprehension
#list_comprehension=[expression for item in items]

prices = [item[1] for item in items]
print(prices)
filtered= [item for item in items if item[1]>=10] #['expression we want to return' 'for item in item' condition(if)]
print(filtered)

#zip functions

list1 = [1,2,3]
list2 = [10,20,30]

print(list(zip("abc",list1,list2)))

#stacks
#LIFO last in first out


browsing_session =[]
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print (browsing_session)
browsing_session.pop()
print (browsing_session)
if not browsing_session:
    print("redirect",browsing_session[-1])

#Queue
#FIFO first in first out
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
if not queue: #that means we have an empty list
    print("empty")

#Tuples is basically a read only list let say you are writing a program and you dont want anyone to accidentally add or remove from your list then tuple comes in handy
point = (1,2)
point = 1,

#swapping variable
x = 10
y = 11

#to swap this you need a 3rd variable

z = x
x = y
y = z

print("x",x)
print("y",y)

#refactor

x , y = y, x

print("x",x)
print("y",y)


"""Arrays are a data type very similar to list but can take large sequence of numbers
they also take less memory and performs a bit faster"""

from array import array

numbers=array("i",[1,2,3,4])
numbers.append(5)
print (numbers)

#set are unordered collection unique items we cannot have duplicates and 
# because they are unordered we cant access them using an index

numbers = [1,1,2,4,6,7,9]
first = set(numbers)
second ={1,3,5}
print(first | second) # union set
print(first & second) #intersection set
print(first - second) #difference set
print(first ^ second) #either in the first or the second but not both set

# Dictionaries are a collection of key-value pairs. a phone book

point = {"x":1, "y":2}
point = dict(x=1,y=2)
point["x"]
print (point["x"])
#To check the existance of a value in a dictionary we use
point["z"]=25

if "b" in point:
    print(point["b"])

# we can also use the get method

print(point.get("b"))

# to delete a key in dict
del point["x"]
print (point)

for key in point:
    print(key,point[key])

# this give us a tuple
for key in point.items():
    print(key)

# we can unpack the ("y",2) into a key,value pair.  key, value = ("y", 2) therefore

for key,value in point.items():
    print (key, value)

# Dictionary comprehensions
# say we have 
value = []
for x in range(5):
    value.append(x*2)

# remember list comprehension [expression for item in items(the iritable)]

value = [x*2 for x in range(5)]
print (value)
# same for sets and dictionaries and what they have in common is {}

# so 
value = {x*2 for x in range(5)}
print (value)

# so to get a dictionary comprehension we only need to introduce a key

# value = {x"key":x*2"value" for x"key" in range(5)}
value = {x:x*2 for x in range(5)}
print (value)

# Generator expression. list take up memory space of the computer so when dealing with large data sets that dont reqiure 
# we store them using a generator will be better because each time it generates the data needed without storing them
# hence generator objects dont have a defined len

values = [x*2 for x in range(10)] #this is a list
print (values)
for x in values:
    print (x)


values = (x*2 for x in range(10)) #this is a generator object because we changed [] to ()
print (values)
for x in values:
    print (x)

# generator objects are very small so to check the size

from sys import getsizeof

values = (x*2 for x in range(10000000)) #this is a generator object because we changed [] to ()
print("gen:",getsizeof(values))

values = [x*2 for x in range(10000000)] #this is a generator object because we changed [] to ()
print("list:",getsizeof(values))

# unpacking operator

numbers = [1, 2, 3]
print (numbers)
print(1,2,3)
print(*numbers)

# unpack a dictionary too

one = {'x':1}
two = {'x':10,'y':20}
combined = {**one,**two, "z":30 }
print(combined)

from pprint import pprint
sentence = "This is a common interview question"
# create a an empty dict
most_frequent_char = {} 
# itirate through the string
for key in sentence.lower():
    if key not in most_frequent_char:
        most_frequent_char[key] = 1
    elif key in most_frequent_char:
        most_frequent_char[key] +=1
pprint(most_frequent_char,width=1)
most_frequent_char_sorted =(sorted(most_frequent_char.items(),
                                   key=lambda kv: kv[1], 
                                   reverse=True))
print(most_frequent_char_sorted[0])
# store the char as key and the frequency as the values in the empty dict
# if char already in dict increase the count +1 else start count at 0
# itirate the the values to find the highest occuring number
# rearrange the dict with the highest values first

# Exception

