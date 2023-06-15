class Model():

    #constructor
    def __init__(self, model_name: str):
        self.name = model_name

        self.nodes: dict[int, list[float]] = dict()
        # self.nodes: list[Node] = list() # this is were we are getting to
        self.bars: dict[int, list[int]] = dict()

    def print_name(self):
        print(self.name)


