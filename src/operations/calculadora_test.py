from faker import Faker
from calculadora import Calculadora
from test.add import AddOperationSpy
from test.sub import SubOperationSpy

fake = Faker()

def test_add():
    addOperation = AddOperationSpy()
    calculadora = Calculadora(addOperation,addOperation)
    
    number1 = fake.random_number()
    number2 = fake.random_number()
    
    result = calculadora.add(number1, number2,True)
    
    # teste de entrada
    assert addOperation.soma_attributer['number1']== number1
    assert addOperation.soma_attributer['number2']== number2
    
    
    # testa de saida
    assert result is not None
    
    
def test_add_none():
    addOperation = AddOperationSpy()
    calculadora = Calculadora(addOperation,addOperation)
    
    number1 = fake.random_number()
    number2 = fake.random_number()
    
    result = calculadora.add(number1, number2,False)
    
    # teste de entrada
    assert addOperation.soma_attributer== {} # verificando se é None

    
    
    # testa de saida
    assert result is None