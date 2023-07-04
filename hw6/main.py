import hw6.check_date as chd
import hw6.queens as qns

_NEED_OK_POSITIONS = 4  # Необходимое кол-во успешных расстановок

if __name__ == "__main__":
    data: str = '24.10.2016'
    queens_positions = [
        [(0, 6), (7, 2), (4, 5), (2, 2), (7, 7), (6, 1), (3, 7), (5, 4)],
        [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]
    print(data)
    print(chd.date_validator(data))

    for list_position in queens_positions:
        print(list_position)
        if qns.check_queen_8x8(list_position):
            print("Ферзи не бьют друг друга")
        else:
            print("Есть ферзи под ударом")

    # генерация позиций
    total_case_generate = 0  # всего расстановок сгенерировано
    case_ok = 0  # удачных расстановок из всего сгенерированных
    list_ok_positions = []  # список удачных расстановок

    while case_ok < _NEED_OK_POSITIONS:
        generated_position = qns.gen_positions()
        total_case_generate += 1
        if qns.check_queen_8x8(generated_position):
            case_ok += 1
            list_ok_positions.append(generated_position)

    print(f" Всего сгенерировано комбинаций {total_case_generate}, ферзи не бьют друг друга:")
    for pos in list_ok_positions:
        print(pos)
