from pickle import FALSE, TRUE


class ImaginaryNumber():
    def __init__(self, r, c):
        self.realPart = r
        self.imaginaryPart = c
        if c < 0:
            self.number = str(r) + str(c) + 'i'
        elif c == 0:
            self.number = str(r)
        else:
            self.number = str(r) + '+' + str(c) + 'i'

    def conjugate(self):
        return ImaginaryNumber(self.realPart, 0-self.imaginaryPart)

    def __add__(self, iNumber):
        addedRealParts = self.realPart + iNumber.realPart
        addedImaginaryParts = self.imaginaryPart + iNumber.imaginaryPart
        return ImaginaryNumber(addedRealParts, addedImaginaryParts)

    def __sub__(self, iNumber):
        subRealParts = self.realPart - iNumber.realPart
        subImaginaryParts = self.imaginaryPart - iNumber.imaginaryPart
        return ImaginaryNumber(subRealParts, subImaginaryParts)

    def __mul__(self, iNumber):
        mulRealPart = self.realPart * iNumber.realPart - \
            self.imaginaryPart * iNumber.imaginaryPart
        mulImaginaryPart = self.realPart * iNumber.imaginaryPart + \
            self.imaginaryPart * iNumber.realPart
        return ImaginaryNumber(mulRealPart, mulImaginaryPart)

    def __truediv__(self, iNumber):
        if iNumber.realPart == 0 and iNumber.imaginaryPart==0:
            print ('DIVISION BY ZERO IS NOT POSSIBLE')
            quit()
        else:
            tDivRealPart = (self.realPart * iNumber.realPart - self.imaginaryPart *
                            (0-iNumber.imaginaryPart))/(iNumber.realPart**2 + iNumber.imaginaryPart**2)
            tDivImaginaryPart = (self.realPart * (0-iNumber.imaginaryPart) + self.imaginaryPart *
                                iNumber.realPart)/(iNumber.realPart**2 + iNumber.imaginaryPart**2)
            return ImaginaryNumber(tDivRealPart, tDivImaginaryPart)

    def __floordiv__(self, iNumber):
        if iNumber.realPart == 0 and iNumber.imaginaryPart==0:
            print ('DIVISION BY ZERO IS NOT POSSIBLE')
            quit()
        else:
            fDivRealPart = (self.realPart * iNumber.realPart - self.imaginaryPart *
                            (0-iNumber.imaginaryPart))//(iNumber.realPart**2 + iNumber.imaginaryPart**2)
            fDivImaginaryPart = (self.realPart * (0-iNumber.imaginaryPart) + self.imaginaryPart *
                                iNumber.realPart)//(iNumber.realPart**2 + iNumber.imaginaryPart**2)
            return ImaginaryNumber(fDivRealPart, fDivImaginaryPart)
    def __eq__(self, iNumber):
        if iNumber.realPart == self.realPart and iNumber.imaginaryPart == self.imaginaryPart:
            return TRUE
        else:
            return FALSE

    def __ne__(self, iNumber):
        if iNumber.realPart != self.realPart or iNumber.imaginaryPart != self.imaginaryPart:
            return TRUE
        else:
            return FALSE

    def __mod__(self, iNumber):
        print ('Mod Operator is not possible for imaginary numbers!!')
        quit()