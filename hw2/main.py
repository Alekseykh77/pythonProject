from hex_number import hex_number
from fractions_from_user import UserFractions

if __name__ == "__main__":

    # int to hex
    number: int = int(input("Введите число: "))
    print(f'''hex of number = {hex_number(number)}
test with hex() = {hex(number)}''')

    # fractions from user
    fraction_1, fraction_2 = [UserFractions(*[int(j) for j in i.split("/")])
                              for i in input("Введите две дроби формата a/b через пробел: ").split()]

    print(f"""Вы ввели дроби {fraction_1} и {fraction_2}
{fraction_1} + {fraction_2} = {fraction_1 + fraction_2}
{fraction_1} * {fraction_2} = {fraction_1 * fraction_2}""")