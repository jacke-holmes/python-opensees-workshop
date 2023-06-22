import numpy as np
from typing import Optional, Any

import mouse as mouse

print('hello world')


i: int = 1
f: float = 5.

my_list: list[int] = []  # list()

my_list2: list[Any] = [1, 2.6, "hello", [1, 2]]


my_dict: dict[str, list[int]] = {
    "1": [1, 2, 3],
    "2": my_list2
}


class Mouse():

    # constructor
    def __init__(self, name: str):
        print(f"this is the constructor for {name}")

        self.mouse_name: str = name
        self.mouse_type: str | None = None

    def left_click(self):
        print(f"left clicking for {self.mouse_name}")
        if self.mouse_type is None:
            self.mouse_type = "logitech"

    @staticmethod
    def right_click():
        print("right clicking")

jacks_mouse = Mouse('jacks_mouse')
jacks_mouse.left_click()
jacks_mouse.right_click()

Mouse.right_click()
mouse.right_click_from_file()

print(0)
