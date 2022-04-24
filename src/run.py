from operations.calculadora import Calculadora
from operations.add import AddOperation
from operations.sub import SubOperation

calc = Calculadora(AddOperation(),SubOperation())

op1 = calc.add(2,5, True)
op2 = calc.add(5,3, True)

print(op1)
print(op2)