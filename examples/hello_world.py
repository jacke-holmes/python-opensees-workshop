# TYPE HINTING

age: int = 5

height: float = 180.0

name: str = 'jack'

my_list: list[int] = [1, 2, 5]
my_tuple: tuple[int, int, int] = (1, 2, 5)

my_dict: dict[str, float] = {
    "key1": 5.0,
    "key2": 10.0
}

my_dict2: dict[str, list[int]] = {
    "key1": [1, 2, 3],
    "key2": [4, 5, 6]
}


def get_2x_age(age: int) -> float:
    return float(2 * age)



# looping through a list
for number in my_list:
    print(number)

for i in range(len(my_list)):
    my_list[i]


# looping through a dictionary
for k, v in my_dict.items():
    print(k, v)

for k in my_dict.keys():
    print(k)

for v in my_dict.values():
    print(v)


class Mouse():

    def __init__(self, name: str):
        self.mouse_name = name

    def print_name(self):
        print(self.mouse_name)

jacks_mouse = Mouse('jack')
reiners_mouse = Mouse('reiner')

jacks_mouse.print_name()

print(0)
