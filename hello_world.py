print('hello world')


i: int = 0
c: str = 'h'

string = "I am a string"

my_tuple = ("a", "b", "c")
my_list = [1, 2, 3, 4] # 0, 1, 2, 3

my_dict: dict[str, int] = {
    "key1": 1,
    "key2": 2
}

print(i)
print(c)
print(string)
print(my_tuple)
print(my_list)
print(my_dict)


# accessing an element in a list
print(my_list[0])

# accessing an element in a dictionary
print(my_dict["key2"])


def func1():
    print('I am function 1')

def func2(a: int, b: str):
    print(a, b)

func1()
func2("hello", 55)
