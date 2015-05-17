class Dog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "A dog named {}".format(self.name)


dominic = Dog("Dominic")

print dominic