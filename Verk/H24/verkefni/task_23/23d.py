import random

class Snowflake():
    def __init__(self):
        self.shape = "+"
        self.position = " "*random.choice(range(1, 100))

    def __str__(self):
        return "Shape is {} , Position is {} .".format(self.shape, self.position)
    
    def print_snowflake(self):
        print(self.position, end="")
        print(self.shape)

def main():
    christmas_snow = []
    for i in range(0, 20):
        snow = Snowflake()
        christmas_snow.append(snow)
    while True:
        for flake in christmas_snow:
            flake.print_snowflake()
main()