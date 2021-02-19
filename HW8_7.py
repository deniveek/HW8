class Complex:
    def __init__(self, a, b):
        self.Z_re = a
        self.Z_im = b

    def __add__(self, other):
        return Complex(self.Z_re + other.Z_re, self.Z_im + other.Z_im)

    def __mul__(self, other):
        return Complex(self.Z_re * other.Z_re - self.Z_im * other.Z_im, self.Z_re * other.Z_im + self.Z_im * other.Z_re)

    def __str__(self):
        out = ""
        if self.Z_re != 0:
            out += f"{self.Z_re}"
            if self.Z_im > 0:
                out += f" + {self.Z_im}i"
            elif self.Z_im < 0:
                out += f" - {abs(self.Z_im)}i"
        else:
            out += f"{self.Z_im}i" if self.Z_im != 0 else "0"
        return out


x1 = Complex(1, 1)
x2 = Complex(2, 2)
x3 = x1*x2
print(x3)
