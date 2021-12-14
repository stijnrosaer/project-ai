class Association:
    def __init__(self, l, r, c, s, lift, z):
        self.left = l
        self.right = r
        self.c = c
        self.s = s
        self.lift = lift
        self.z = z
        
    def __str__(self):
        return "Conf: {:.2f}\tSupp: {:.2f}\tLift: {:.5f}Z: {:.5f}\n\t".format(self.c, self.s, self.lift, self.z) + \
            " {" + ", ".join(map(str, self.left)) + \
            "} => {" + ", ".join(map(str, self.right)) + "}"
