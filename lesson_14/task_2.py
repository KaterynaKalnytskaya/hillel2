class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def __repr__(self):
        return f"Car('{self.name}', {self.price})"

    def __add__(self, other):
        if isinstance(other, Car):
            return self.price + other.price
        elif isinstance(other, (int, float)):
            if other > 0:
                return self.price + other
            else:
                raise ValueError("Price should be a positive number.")
        else:
            raise ValueError("Unsupported operand types")

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.price == other.price
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.price < other.price
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Car):
            return self.price <= other.price
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.price > other.price
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Car):
            return self.price >= other.price
        else:
            return False


toyota = Car("Camry", 123456)
bmw = Car("X5", 321654)

print(toyota == bmw)
print(toyota < bmw)
print(toyota <= bmw)
print(toyota > bmw)
print(toyota >= bmw)
