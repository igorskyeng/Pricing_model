from data.config import create_base, drop_data_base
from src.algorithm import Algorithm
from src.db_manager import DBManager


def main():
    """Опрос пользователя для рабыты с БД и алгоритмом цоновой модели"""
    # Создание базы данных и таблицы.
    create_base()
    # Список всех данных из БД.
    list_pricing_model = []
    # Переменная для записи выбора пользоветелем.
    choice = ''
    # Переменная для записи выбора пользоветелем о выводе списка в консоль.
    output_choice = ''
    # Предыдущий выбор пользователя (нужен для работы алгоритма).
    previous_choice = ''
    # Для полноценной работы нужно запустить в первую очередь 1 пункт.
    exit_script = 0

    # Опрос пользователя для работы с БД.
    while exit_script == 0:
        previous_choice = choice
        choice = input('\nВыберите нужное действие:\n'
                       '1 - Записать значения из "csv" файла в базу данных "PostgreSQL";\n'
                       '2 - Запись всех значений из базы данных в список;\n'
                       '3 - Запись всех значений из базы данных в список по определенному продукту;\n'
                       '4 - Запись всех значений из базы данных в список по определенной компании;\n'
                       '5 - Запись всех значений из базы данных в список по определенной компании и продукту;\n'
                       '6 - Работа алгоритма;\n'
                       '7 - Удалить базу данных;\n'
                       '8 - Закончить скрипт.\n\n')

        # Запись данных в БД.
        if choice == '1':
            DBManager.checking_completeness_database()
            input('Далее.')

        # Вывод списка из БД.
        elif choice == '2':
            list_pricing_model = DBManager.the_entire_output(name_database='pricing_model')
            output_choice = input('\nВывести все записанные значения:\n'
                                  '1 - Да;\n'
                                  '2 - Нет.\n')

            # Вывод списка в консоль по желанию пользователя.
            if output_choice == '1':
                for line in list_pricing_model:
                    print(line)

            print(f'\nКоличество значений: {len(list_pricing_model)}.\n')
            input('Далее.')

        # Вывод списка из БД по определенному продукту.
        elif choice == '3':
            product = input('\nВведите продукт:\n')
            list_pricing_model = DBManager.conclusion_by_product(name_database='pricing_model', product=product)
            output_choice = input('\nВывести все записанные значения:\n'
                                  '1 - Да;\n'
                                  '2 - Нет.\n')

            # Вывод списка в консоль по желанию пользователя.
            if output_choice == '1':
                for line in list_pricing_model:
                    print(line)

            print(f'\nКоличество значений: {len(list_pricing_model)}.\n')
            input('Далее.')

        # Вывод списка из БД по определенной компании.
        elif choice == '4':
            company = input('\nВведите компанию:\n')
            list_pricing_model = DBManager.conclusion_by_company(name_database='pricing_model', company=company)
            output_choice = input('\nВывести все записанные значения:\n'
                                  '1 - Да;\n'
                                  '2 - Нет.\n')

            # Вывод списка в консоль по желанию пользователя.
            if output_choice == '1':
                for line in list_pricing_model:
                    print(line)

            print(f'\nКоличество значений: {len(list_pricing_model)}.\n')
            input('Далее.')

        # Вывод списка из БД по определенной компании и продукту.
        elif choice == '5':
            company = input('\nВведите компанию:\n')
            product = input('\nВведите продукт:\n')
            list_pricing_model = DBManager.conclusion_by_company_and_product(name_database='pricing_model',
                                                                             company=company, product=product)
            output_choice = input('\nВывести все записанные значения:\n'
                                  '1 - Да;\n'
                                  '2 - Нет.\n')

            # Вывод списка в консоль по желанию пользователя.
            if output_choice == '1':
                for line in list_pricing_model:
                    print(line)

            print(f'\nКоличество значений: {len(list_pricing_model)}.\n')
            input('Далее.')

        # Работа алгоритма для возвращения максимальных и минимальных цен с учетом затрат и без них и
        # прибьлей компаний и их продуктов, id строк в БД с данными значениями.
        elif choice == '6':
            if len(list_pricing_model) == 0:
                print('\nНет значений для алгоритма (нужно выполнить один из пунктов: 2-5).\n')
                input('Далее.')

            else:
                # Работа алгоритма по всем компаниям и продуктам.
                if previous_choice == '2':
                    algorithm = Algorithm.conclusion_by_company_and_product(list_pricing_model)
                    print(f'\nВсе компании: {sorted(algorithm[0])};')
                    print(f'\nВсе продукты: {sorted(algorithm[1])};')
                    print(f'\nМаксимальная цена за продукт {algorithm[5]} без учета затрат: {algorithm[2]} '
                          f'у компании {algorithm[4]}')
                    print(f'Цена: {list_pricing_model[algorithm[3]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[3]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[3]][2]};')
                    print(f'Максимальная цена за продукт {algorithm[9]} с учетом затрат: {algorithm[6]} '
                          f'у компании {algorithm[8]}')
                    print(f'Цена: {list_pricing_model[algorithm[7]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[7]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[7]][2]};')
                    print(f'\nМинимальная цена за продукт {algorithm[13]} без учета затрат: {algorithm[10]} '
                          f'у компании {algorithm[12]}')
                    print(f'Цена: {list_pricing_model[algorithm[11]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[11]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[11]][2]};')
                    print(f'Минимальная цена за продукт {algorithm[17]} с учетом затрат: {algorithm[14]} '
                          f'у компании {algorithm[16]}')
                    print(f'Цена: {list_pricing_model[algorithm[15]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[15]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[15]][2]};')
                    print(f'\nМаксимальная прибыль за продукт {algorithm[21]}: {algorithm[18]} '
                          f'у компании {algorithm[20]}')
                    print(f'Цена: {list_pricing_model[algorithm[19]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[19]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[19]][2]};')
                    print(f'Минимальная прибыль за продукт {algorithm[25]}: {algorithm[22]} '
                          f'у компании {algorithm[24]}')
                    print(f'Цена: {list_pricing_model[algorithm[23]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[23]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[23]][2]}.\n')
                    input('Далее.')

                # Работа алгоритма по определенной продукту.
                elif previous_choice == '3':
                    algorithm = Algorithm.conclusion_by_product(list_pricing_model)
                    print(f'\nВсе компании с данным продуктом: {sorted(algorithm[0])}')
                    print(f'\nМаксимальная цена за данный продукт без учета затрат: {algorithm[1]} '
                          f'у компании {algorithm[3]};')
                    print(f'Цена: {list_pricing_model[algorithm[2]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[2]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[2]][2]};')
                    print(f'Максимальная цена за данный продукт с учетом затрат: {algorithm[4]} '
                          f'у компании  {algorithm[6]}')
                    print(f'Цена: {list_pricing_model[algorithm[5]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[5]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[5]][2]};')
                    print(f'\nМинимальная цена за данный продукт без учета затрат: {algorithm[7]} '
                          f'у компании {algorithm[9]}')
                    print(f'Цена: {list_pricing_model[algorithm[8]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[8]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[8]][2]};')
                    print(f'Минимальная цена за данный продукт с учетом затрат: {algorithm[10]} '
                          f'у компании  {algorithm[12]}')
                    print(f'Цена: {list_pricing_model[algorithm[11]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[11]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[11]][2]};')
                    print(f'\nМаксимальная прибыль за данный продукт: {algorithm[13]} '
                          f'у компании {algorithm[15]}')
                    print(f'Цена: {list_pricing_model[algorithm[14]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[14]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[14]][2]};')
                    print(f'Минимальная прибыль за данный продукт: {algorithm[16]} '
                          f'у компании {algorithm[18]}')
                    print(f'Цена: {list_pricing_model[algorithm[17]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[17]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[17]][2]}.\n')
                    input('Далее.')

                # Работа алгоритма по определенной компании.
                elif previous_choice == '4':
                    algorithm = Algorithm.conclusion_by_company(list_pricing_model)
                    print(f'\nВсе продукты компании: {sorted(algorithm[0])};')
                    print(f'\nМаксимальная цена у данной компании - {algorithm[1]} '
                          f'без учета затрат на продукт: {algorithm[3]}')
                    print(f'Цена: {list_pricing_model[algorithm[2]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[2]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[2]][2]};')
                    print(f'Максимальная цена у данной компании - {algorithm[4]} '
                          f'с учетом затрат на продукт: {algorithm[6]}')
                    print(f'Цена: {list_pricing_model[algorithm[5]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[5]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[5]][2]};')
                    print(f'\nМинамальная цена у данной компании - {algorithm[7]} '
                          f'без учета затрат на продукт: {algorithm[9]}')
                    print(f'Цена: {list_pricing_model[algorithm[8]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[8]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[8]][2]};')
                    print(f'Минамальная цена у данной компании - {algorithm[10]} '
                          f'с учетом затрат на продукт: {algorithm[12]}')
                    print(f'Цена: {list_pricing_model[algorithm[11]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[11]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[11]][2]};')
                    print(f'\nМаксимальная прибыль у данной компании - {algorithm[13]} '
                          f'на продукт: {algorithm[15]}')
                    print(f'Цена: {list_pricing_model[algorithm[14]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[14]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[14]][2]};')
                    print(f'Минимальная прибыль у данной компании - {algorithm[16]} '
                          f'на продукт: {algorithm[18]}')
                    print(f'Цена: {list_pricing_model[algorithm[17]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[17]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[17]][2]}.\n')
                    input('Далее.')

                # Работа алгоритма по определенной компании и продукту.
                elif previous_choice == '5':
                    algorithm = Algorithm.the_entire_output(list_pricing_model)
                    print(f'\nМаксимальная цена у данной компании - {algorithm[0]} '
                          f'без учета затрат на выбранный продукт')
                    print(f'Цена: {list_pricing_model[algorithm[1]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[1]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[1]][2]};')
                    print(f'Максимальная цена у данной компании - {algorithm[2]} '
                          f'с учетом затрат на выбранный продукт')
                    print(f'Цена: {list_pricing_model[algorithm[3]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[3]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[3]][2]};')
                    print(f'\nМинамальная цена у данной компании - {algorithm[4]} '
                          f'без учета затрат на выбранный продукт')
                    print(f'Цена: {list_pricing_model[algorithm[5]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[5]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[5]][2]};')
                    print(f'Минамальная цена у данной компании - {algorithm[6]} '
                          f'с учетом затрат на выбранный продукт')
                    print(f'Цена: {list_pricing_model[algorithm[7]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[7]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[7]][2]};')
                    print(f'\nМаксимальная прибыль у данной компании - {algorithm[8]} '
                          f'на выбранный продукт')
                    print(f'Цена: {list_pricing_model[algorithm[9]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[9]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[9]][2]};')
                    print(f'Минимальная прибыль у данной компании - {algorithm[10]} '
                          f'на выбранный продукт')
                    print(f'Цена: {list_pricing_model[algorithm[11]][0]}, '
                          f'Количество: {list_pricing_model[algorithm[11]][1]}, '
                          f'Затраты: {list_pricing_model[algorithm[11]][2]}.\n')
                    input('Далее.')

        # Удалить БД.
        elif choice == '7':
            drop_data_base()
            input('Далее.')

        # Закончить скрипт.
        elif choice == '8':
            exit_script = 1


main()
