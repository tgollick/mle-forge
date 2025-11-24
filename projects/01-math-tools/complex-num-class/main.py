
class Complex:
    __slots__ = ('real', 'imag')

    def __init__(self, r, i):
        self.real = r 
        self.imag = i

    def __repr__(self):
        return f"Complex({self.real!r}, {self.imag!r}i)"

    def __add__(self, other):
        return Complex((self.real + other.real), (self.imag + other.imag))

    def __mul__(self, other):
        # Formula is (ac - bd) + (ad + bc)i
        a, b, c, d, = self.real, self.imag, other.real, other.imag

        real = (a * c) - (b * d)
        imag = (a * d) + (b * c)

        return Complex(real, imag)

    def __eq__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented

        return self.real == other.real and self.imag == other.imag
