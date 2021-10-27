class Rules:
    def __init__(self):
        self.rules = []

        self.aboveMaxRulenumFlag = False
        self.belowMinNumrulesFlag = False
        
    
    def __len__(self):
        return len(self.rules)

    @property
    def numrules(self):
        return len(self.rules)
        
class Rule:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs



