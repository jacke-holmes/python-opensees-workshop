print('hello world')
i = int
c = str
string = str


i = 0
c= 'h'
string = "I am a string"

my_tuple = ("a", "b", "c")
my_list:list[int] = [1,2,3,4]

my_dict = {
    "key1" : 1 ,
    "key2" : 2
}

print(i)
print(c)
print(string)
print(my_tuple)
print(my_list)
print(my_dict)

print(my_list[1])

def func1():
    print ('I am function 1 - big woops')

def func2(a: int, b: string):
    print(a, b)

func1()
func2(999, 'hello')