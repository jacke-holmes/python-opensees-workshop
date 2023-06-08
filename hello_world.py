# Fast way of opening visual studio, type cmd on directory box, and then in terminal type code . (didn't work for me)
from typing import Any # ,Dict
print('hello world')


i = 0 #integer
c = 'h' #character
string = "I am a string" #string
print(i,c)

my_list = [1,2,3,4] 
my_tuple = ("a","b","c") #immutable - can't be changed laterc
my_dict: dict[str, Any] = {
    "key1": [1,2,3],
    "key2": 2
}

print(i)
print(c)
print(string)
print(my_tuple)
print(my_list)
print(my_dict)

# accessing element in a list 
print(my_list[0])
print(my_list[-4])

# accessing element in a dictionary
print(my_dict["key1"])
print(my_dict["key1"][0])

print(type(c))

def func1():
    print("I am Marianthi")

func1()

def func2(a: int, b: str):
    print(a,b)

func2(245,"woohoo")
func2(a=245, b="dummy")
func2(b="woohoo",a=475)