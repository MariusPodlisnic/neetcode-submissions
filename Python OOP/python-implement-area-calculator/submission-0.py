import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self,*args:int) -> float:
        if len(args) == 1:
            circle_area = 1
            for x in args:
                circle_area = math.pi * pow(x,2)
            return round(circle_area,2)
        if len(args) == 2:
            product = 1
            for x in args:
                product *= x
            return product


    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))