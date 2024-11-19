from decimal import Decimal
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        a, b = (b, a) if b < 0 or isinstance(b, (float, Decimal)) else (a, b)
        a, b = (-a, -b) if a < 0 and b < 0 else (a, b)
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if a == 0:
            return 0
        result = 0
        negative = (a < 0) != (b < 0)
        a,b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if negative else result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        while a >= b:
            a = a - b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))