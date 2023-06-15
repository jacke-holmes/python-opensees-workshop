print('hello world')


i: int = 0
c: str = 'h'
string = 'Ik ben een string'
my_list = [1,2,3,4]
my_tuple = ("a","b","c")
my_dict: dict[str,int] = {
    "key1": 1,
    "key2": 2
}

print(i)
print(c)
print(string)
print(my_tuple)
print(my_list)
print(my_dict)

#accessing an element in a list 
print(my_list[-1])

#accessing an element in a dictionary
print(my_dict["key2"])

def func1 ():
    print('I am function 1')

def func2(a:int, b:string):
    print (a, b)    

func1()    
func2(999, "holly")