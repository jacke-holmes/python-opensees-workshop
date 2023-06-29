import numpy as np
from typing import Optional, Any

print('hello world')

l: int = 1
i: str = '0' # specifying the type (int) or (str) (dict) makes the understanding of the code easy, so do that! 
c: str = 'h'
d: str = c + i
print('d =', d)

string = 'I am a string'

#j: int|None
#if j is not None:
#    j+1

#k: Optional[int|float]


my_tuple = ("a", "b", "c") # a tuple cannot be mutated after it is created
my_list: list[int] = [1, 2, 3, 4] # a list can be mutated after it is created
my_dict: dict[str, int] = { #dict is the type, the key is a string and the value is an integer
    "key1": 1,
    "key2": 2 # the values can also be a list or another dictionary etc.
}

print(i)
print(c)
print(string)
print(my_tuple)
print(my_list)
print(my_dict)

# accessing an element in a list 
print(my_list[1]) # python is a 0 based language so it starts counting at 0, it is commen to need to loop through the whole list 

# accessing an element in a dictionary
print(my_dict["key2"]) # a dictionary is key based and not index based as the list is, so the key is linked to the item behind it

def func1():
    print('I am function 1')

def func2(a: int, b: str):
    print(a, b)

func1()
func2(b='hello', a=99) #the items do not necc have to be labeled but when they are labeled they can be put in the other way around and still come out as a b



class Mouse():
    

    
    def lift_click(self):
        print("left clicking")

    @staticmethod
    def right_click():
        print("right clicking")

amys_mouse = Mouse()

print(0)