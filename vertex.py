class Vertex:
    def __init__(self, code, name, visaReq):
        self.code = code
        self.name = name
        self.visaReq = visaReq
        self.acc = 99999
        self.predecesor = None
        self.visited = False