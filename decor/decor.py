"""
Декораторы в Python - это специальная конструкция, которая позволяет изменить/модифицировать/расширить функциональность других функций или методов без изменения исходного кода
"""
"""
Декораторы в Python пишутся с использованием символа @ перед определением функции, которую нужно декорировать. Декораторы могут принимать аргументы.
"""

def func(): # <- функция
    pass

class Human():
    def add_heatl(self): # <- это метод класса
        pass

human = Human()
"""
@human.add_heatl()
def primer():
    pass
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # func = фунция generator
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Время работы функции {result_time}, {func.__name__}")
        return result   
    return wrapper


def message(func):
    def wreapper(*args, **kwargs):
        print(f'До вызыва функции {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Фунция {func.__name__} выполнена, мы снова в декораторе')
        return result
    return wreapper

@message
def generator(start, end):
    time.sleep(2)
    print(f'выполняется фунция generator')
    result = []
    for value in range(start, end):
        result.append(value)
    return result




@timer
def sum_num(value_one, value_two):
    return value_one + value_two



# generator = timer(generator(start, end))


