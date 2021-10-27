class Condset:
    def __init__(self, items ):
        self.items = sorted(list(items))
        self.condsupCount = 0
        self.rulesupCount = 0