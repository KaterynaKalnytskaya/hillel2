class Rational:
    def __init__(self, numerator=0, denominator=1):
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            raise ValueError("Illegal value of the denominator")
        self.__numerator = numerator
        self.__denominator = denominator
        self.__reduce()

    def __reduce(self):
        def great_common_divider(numerator, denominator):
            if numerator == 0:
                return denominator
            elif denominator == 0:
                return numerator
            elif numerator >= denominator:
                return great_common_divider(numerator % denominator, denominator)
            else:
                return great_common_divider(numerator, denominator % numerator)

        sign = 1
        if (self.__numerator > 0 > self.__denominator) or \
                (self.__numerator < 0 < self.__denominator):
            sign = -1
        numerator, denominator = abs(self.__numerator), abs(self.__denominator)
        c = great_common_divider(numerator, denominator)
        self.__numerator = sign * (numerator // c)
        self.__denominator = denominator // c

    def __clone(self):
        return Rational(self.__numerator, self.__denominator)

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = int(value)
        self.__reduce()

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        value = int(value)
        if value == 0:
            raise ValueError("Illegal value of the denominator")
        self.__denominator = value
        self.__reduce()

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

    def __repr__(self):
        return self.__str__()

    def __float__(self):
        if self.__denominator == 0:
            raise ZeroDivisionError()
        return self.__numerator / self.__denominator

    def __bool__(self):
        return self.__numerator != 0

    def __iadd__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            numerator = self.numerator * another_fraction.denominator + \
                self.denominator * another_fraction.numerator
            denominator = self.denominator * another_fraction.denominator
            self.__numerator, self.__denominator = numerator, denominator
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __add__(self, another_fraction):
        return self.__clone().__iadd__(another_fraction)

    def __isub__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            numerator = self.numerator * another_fraction.denominator - \
                self.denominator * another_fraction.numerator
            denominator = self.denominator * another_fraction.denominator
            self.__numerator, self.__denominator = numerator, denominator
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __sub__(self, another_fraction):
        return self.__clone().__isub__(another_fraction)

    def __imul__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            numerator = self.numerator * another_fraction.numerator
            denominator = self.denominator * another_fraction.denominator
            self.__numerator, self.__denominator = numerator, denominator
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __mul__(self, another_fraction):
        return self.__clone().__imul__(another_fraction)

    def __itruediv__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            numerator = self.numerator * another_fraction.denominator
            denominator = self.denominator * another_fraction.numerator
            if denominator == 0:
                raise ValueError("Illegal value of the denominator")
            self.__numerator, self.__denominator = numerator, denominator
            self.__reduce()
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __truediv__(self, another_fraction):
        return self.__clone().__itruediv__(another_fraction)

    def __eq__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            return (self.numerator == another_fraction.numerator) and \
                   (self.denominator == another_fraction.denominator)
        else:
            return False

    def __ne__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            return not self.__eq__(another_fraction)
        else:
            return False

    def __gt__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            return self.__float__() > another_fraction.__float__()
        else:
            return False

    def __lt__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            return self.__float__() < another_fraction.__float__()
        else:
            return False

    def __ge__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            return not self.__lt__(another_fraction)
        else:
            return False

    def __le__(self, another_fraction):
        if isinstance(another_fraction, Rational):
            return not self.__gt__(another_fraction)
        else:
            return False


if __name__ == '__main__':
    r1 = Rational(3, 4)
    print(float(r1))
    print(r1)
    print(f"r1 = {r1}")
    r2 = Rational(5, 6)
    print(r1)
    print(f"r2 = {r2}")
    print(f"{r1} + {r2} = {r1 + r2}")
    print(f"{r1} - {r2} = {r1 - r2}")
    print(f"{r1} * {r2} = {r1 * r2}")
    print(f"{r1} / {r2} = {r1 / r2}")
    print(f"{r1} == {r2} {r1 == r2}")
    print(f"{r1} != {r2} {r1 != r2}")
    print(f"{r1} > {r2} {r1 > r2}")
    print(f"{r1} < {r2} {r1 < r2}")
    print(f"{r1} >= {r2} {r1 >= r2}")
    print(f"{r1} <= {r2} {r1 <= r2}")
