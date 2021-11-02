class Association:
    def __init__(self, l, r, c, s):
        self.left = l
        self.right = r
        self.c = c
        self.C = c
        self.s = s
        self.S = s
        self.score = 0
        
    def __str__(self):
        return "Conf: {:.2f}\tSupp: {:.2f}\t".format(self.C, self.S) + \
            " {" + ", ".join(map(str, self.left)) + \
            "} => {" + ", ".join(map(str, self.right)) + "}"
