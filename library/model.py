from library.nodes import Node
from library.bars import Bar

class Model():

    # constructor
    def __init__(self, model_name: str):
        self.name = model_name

        self.nodes: dict[int, Node] = dict()
        self.bars: dict[int, Bar] = dict()

    def print_name(self):
        print(self.name)

    @property
    def p_node_count(self):
        return len(self.nodes)

    @p_node_count.setter
    def p_node_count(self, number: int):
        raise Exception("you should not modify the node count directly")

    @property
    def p_bar_count(self):
        return len(self.bars)



####################################### test  #################################

class DemoClass():

    def __init__(self, name: str = "default"):
        self.my_name = name

    def print_name(self):
        print(self.my_name)

    @staticmethod
    def print_this_name(name: str):
        print(name)

    # basic getter
    def get_name(self):
        print(self.my_name)

    @property # getter
    def name(self):
        return self.my_name + "_" + "2"

    # basic setter
    def set_name(self, new_name: str):
        self.my_name = new_name

    @name.setter
    def name(self, new_name: str):
        self.my_name = new_name



if __name__ == "__main__":

    demo = DemoClass("jake") # instantiation / creating an instance

    # demo.set_name('Jelmer')

    # print("name property: ", demo.name)

    demo.name = "jake_3"


    DemoClass.print_this_name("maria")
