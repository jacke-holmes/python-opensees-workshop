#                       0    1   2   3   4   5
my_list: list[float] = [10, 20, 30, 40, 50, 60]
my_list2: list[float] = [70, 80, 90, 100, 110, 120]

# for loop

# element looping
for e in my_list:
    print(e)

print("-------------------------------------------------")

for e in reversed(my_list):
    print(e)

print("-------------------------------------------------")

# index based looping
for i in range(0, len(my_list)):
    print(i, ": ", my_list[i])

print("-------------------------------------------------")

for i in range(len(my_list), 0, -2):
    print(i - 1)

print("-------------------------------------------------")

for i in range(0, len(my_list) - 1):
    print(my_list[i] + my_list[i+1])

print("-------------------------------------------------")

# enumeration
for i, e in enumerate(my_list):
    print(i, ": ", e)

print("-------------------------------------------------")

# list comprehension
new_list = [i + 5 for i in my_list]
print(new_list)

print("-------------------------------------------------")

number: float = 1.0
for e in my_list:
    number *= e
    print(number)

print("-------------------------------------------------")

assert len(my_list) == len(my_list2), "lists are not the same length"
for i, j in zip(my_list, my_list2):
    print("i: ", i, " | ", "j: ", j)

print("-------------------------------------------------")
print("-------------------------------------------------")

# looping through dictionaries
my_dict: dict[str, float] = {
    "node1": 1.0,
    "node4": 4.0,
    "node3": 3.0
}

for k in my_dict.keys():
    print(k)

for v in my_dict.values():
    print(v)

for k, v in my_dict.items():
    print(k, v)

keys = list(my_dict.keys())

print(0)

