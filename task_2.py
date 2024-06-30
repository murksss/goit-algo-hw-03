"""
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали
випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел
від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних
випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі
повинні бути унікальні.

Вимоги до завдання:

1.  Параметри функції:
        min - мінімальне можливе число у наборі (не менше 1).
        max - максимальне можливе число у наборі (не більше 1000).
        quantity - кількість чисел, які потрібно вибрати (значення між min і max).
2.  Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
3.  Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися.
    Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
"""

import random


def get_numbers_ticket(min_: int, max_: int, quantity: int) -> list:
    """
    :param min_: minimum value of the range (greater than 0)
    :param max_: maximum value of the range (inclusive | less than 1000)
    :param quantity: the number of numbers to be selected (values between min_ and max_)
    :return: returns a list of unique, randomly selected, sorted numbers
    If the parameters do not meet the specified restrictions, the function returns an empty list.
    """
    if min_ < 1:
        print('Min value must be greater than 0')
    elif max_ > 1000:
        print('Max value must be less than 1000')
    elif min_ >= max_:
        print('Min value must be less than Max value')
    elif quantity < 1:
        print('quantity must be greater than 1')
    elif quantity > max_ - min_:
        print('Quantity must be less than min-max range')
    else:
        numbers = range(min_, max_ + 1)
        return sorted(random.sample(numbers, quantity))

    return []


if __name__ == '__main__':
    print(get_numbers_ticket(min_=0, max_=1000, quantity=1))
    print(get_numbers_ticket(min_=1, max_=1001, quantity=1))
    print(get_numbers_ticket(min_=10, max_=10, quantity=1))
    print(get_numbers_ticket(min_=1, max_=10, quantity=0))
    print(get_numbers_ticket(min_=1, max_=10, quantity=10))
    print(get_numbers_ticket(min_=1, max_=36, quantity=5))
