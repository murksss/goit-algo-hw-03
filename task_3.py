"""
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату,
залишаючи тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у
будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не
містить міжнародного коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть
придатними для відправлення SMS.

Вимоги до завдання:

1.  Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
2.  Функція видаляє всі символи, крім цифр та символу '+'.
3.  Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380'
    (додається лише '+') та коли номер починається без коду (додається '+38').
4.  Функція повертає нормалізований телефонний номер у вигляді рядка.
"""

import re


def normalize_phone(phone_number: str) -> str:
    """
    :param phone_number: phone number
    :return: normilized phone number (format: +380XXXXXXXXX)
    """

    # delete all symbols all characters except numbers and '+' from the number.
    normalized_number = re.sub(r'[^\d+]', '', phone_number)

    if not normalized_number.startswith('+'):
        if not normalized_number.startswith('38'):
            normalized_number = '+38' + normalized_number
        else:
            normalized_number = '+' + normalized_number

    return normalized_number


if __name__ == '__main__':
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print(f"Нормалізовані номери телефонів для SMS-розсилки:\n{'\n'.join(sanitized_numbers)}")
