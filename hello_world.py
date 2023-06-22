import numpy as np
from typing import Optional, Any

#from mouse import*
import mouse as mouse

print('hello world')
#h = {'d': [1, 2, 3]}

i: int = 5
f: float = 4.0

my_list: list[int] = list() # or []

my_list2: list[Any] = [1, 2.6, "hello", [1,2]]

my_dict: dict[str,list[int]] = {
    "1": [1, 2, 3],
    "2": my_list2
}

class Mouse():
    # constructor
    def __init__(self, name:str): # is the first thing that gets imported --- (self, name:str="")
        print(f"this is the constructor for {name}")
        self.mouse_name : str = name
        self.mouse_type : str | None = None

    #dynamic method (instantiated method)
    def left_click(self):
        print(f"left clicking {self.mouse_name}")
        if self.mouse_type is None:
            self.mouse_type = "logitech"
    
    #static method (not an instance function)
    @staticmethod
    def right_click():
        print(f"right clicking")
    
    # @property
    # def Color():
    #     ..

jacks_mouse = Mouse("Jack's Mouse")

jacks_mouse.left_click()
jacks_mouse.right_click()

mouse.right_click_from_file()
