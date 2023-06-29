from nodes import Node

class Model():
    
    # constructor
    def __init__(self, model_name: str):
        self.name = model_name

        self.nodes: dict[int, Node] = dict()
        self.bars: dict[int, list[int]] = dict()

    def print_name(self):
        print(self.name)

    @property # watch out: this runs every time -> just simple calculations
    def node_count(self):
        return len(self.nodes)
    
    @property
    def bar_count(self):
        return len(self.bars)
    
    @node_count.setter
    def node_count(self, number: int):
        raise Exception("Don't modify the number of nodes!")

class DemoClass():

    def __init__(self, name: str = "default"):
        self.my_name = name
        pass

    def print_name(self): # function in a class = method
        print (self.my_name)

    @staticmethod   
    def print_this_name(name: str):
        print(name)

    # basic getter
    def get_name(self): # getter
        print(self.my_name)

    # python getter
    @property
    def name(self):
        return self.my_name + "_" + "2"

    # basic setter
    def set_name(self, name: str): # setter
        self.my_name = name

    @name.setter
    def name(self, new_name: str):
        self.my_name = new_name

if __name__ == "__main__":

    demo = DemoClass("jake") #instantiation / creating an instance
    demo2 = DemoClass("jelmer")

    #demo.print_name()

    #DemoClass.print_this_name("Maria")

    # demo.set_name("Jake")
    # demo.print_name()

    demo.name = "Jake_3"

    print(demo.name)

    