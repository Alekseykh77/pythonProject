from typing import Callable
from random import randint
from counter_wrappers import counter_wrappers
from json_wrappers import json_wrappers


def game_wrappers(func) -> Callable[[], None]:
    def wrapper(num: int, count: int, *args, **kwargs):
        if 1 > num or num > 100:
            num = randint(1, 100)
        if 1 > count or num > 10:
            count = randint(1, 10)
        result = func(num, count, *args, **kwargs)
        return result

    return wrapper


@counter_wrappers(3)
@game_wrappers
@json_wrappers
def game(num: int, count: int):
    for i in range(1, count + 1):
        print(f"Попытка номер {i} ")
        user_num = int(input("Введите число от 1 до 100: \n >>> "))
        if user_num == num:
            print("Угадал!!!")
            break
        elif user_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")


if __name__ == '__main__':
    game(101, -15)
