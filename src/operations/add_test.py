from add import AddOperation
from faker import Faker
fake = Faker()



def test_some():
    addOperation= AddOperation()
    
    result = addOperation.soma(4,2)
    number1 = fake.random_number()
    number2 = fake.random_number()
    
    expect = number1 + number2
    result = addOperation.soma(number1, number2)
    print('\n')
    print('Valor esperado {}'.format(expect))
    print('resultado {}'.format(result))
    assert result == expect
    
    