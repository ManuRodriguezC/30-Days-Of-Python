class Fruit:

    def __init__(self, fruits):
        self.fruits = fruits

    def __sub__(self, other):
        return "{} fruits - {} fruits = {} fruits".format(self.fruits, other.fruits, self.fruits - other.fruits)      

frut1 = Fruit(10)
frut2 = Fruit(5)

print(frut1 - frut2)