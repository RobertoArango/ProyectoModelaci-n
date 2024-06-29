class Vertex:
    def __init__(self, code, name, acc, predecesor):
        self.code = code
        self.name = name
        self.acc = acc
        self.predecesor = predecesor
        self.visited = False