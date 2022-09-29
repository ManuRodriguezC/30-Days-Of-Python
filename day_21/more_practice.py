class Robot:
    pass
if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)

class Robot:
    pass
x = Robot()
y = Robot()
x.name = "Marvin"
x.build_year = 1995
y.name = "Lola"
y.build_year = 1998
print(x.name)
print(x.__dict__)
print(y.__dict__)
print(Robot.__dict__)