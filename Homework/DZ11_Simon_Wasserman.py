class FormulaError(Exception):
    """
    Raised when the input data does not consists of 3 elements.
    """

    def __init__(self, message='Must be a number', *args, **kwargs):
        super().__init__(message, *args, **kwargs)


def parse_input(user_input):
    """
    Пытаемся конвертировать пользовательский ввод в float.
    :param user_input: str
    :return:  float, str, float
    """
    input_list = user_input.split()  # default - space
    if len(input_list) != 3:
        raise FormulaError('Input does not consist of 3 elements')
    number_1, operator, number_2 = input_list
    try:
        number_1, number_2 = float(number_1), float(number_2)
    except ValueError:
        raise FormulaError()
    return number_1, operator, number_2


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    if number2 == 0:
        raise ZeroDivisionError("Can not multiply a number by 0.")
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        raise ZeroDivisionError("Can not divide a number by 0.")
    return number1 / number2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculate(num1, operator, num2):
    operation = operations.get(operator)
    if operation:
        return operation(num1, num2)
    raise FormulaError(f'{operator} is not a valid operator!')


while True:
    user_input = input('Enter value for calculate ->')
    if user_input == 'exit':
        break
    number1, operator, number2 = parse_input(user_input)
    result = calculate(number1, operator, number2)
    print(result)