class Arithmetics:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        print(f"The addition of {self.num_1} and {self.num_2} is {self.num_1 + self.num_2}")

    def mul(self):
        print(f"The multiplication of {self.num_1} and {self.num_2} is {self.num_1 * self.num_2}")

    def div(self):
        print(f"The division of {self.num_1} and {self.num_2} is {self.num_1 / self.num_2}")

    def sub(self):
        print(f"The subtraction of {self.num_1} and {self.num_2} is {self.num_1 - self.num_2}")
