"""Скрипт для возвращения максимальных и минимальных цен с учетом затрат и без них и прибьлей компаний и их продуктов,
id строк в БД с данными значениями."""
# Списка для записи компаний и их продуктов.
list_company, list_product = [], []
# Максимальная цена без учета затрат с ее id строки в БД и максимальная цена с учетом затрат с ее id строки в БД.
# (без учета количества товара).
max_price, max_price_id, max_price_with_expenses, max_price_with_expenses_id = 0, 0, 0, 0
# Компания и продукт с максимальной ценой с учотом затрат и без без учета затрат.
company_max_price, product_max_price, company_max_price_with_expenses, product_max_price_with_expenses = '', '', '', ''
# id строки в БД минимальной цены без учета затрат и id строки в БД минимальной цены с учетом затрат
# (без учета количества товара).
min_price_id, min_price_with_expenses_id = 0, 0
# Компания и продукт с минимальной ценой с учотом затрат и без без учета затрат.
(company_min_price, product_min_price, company_min_price_price_with_expenses,
 product_min_price_with_expenses) = '', '', '', ''
# Максимальная прибыль с ее id строки в БД и id строки в БД минимальной прибыли (с учетом количесвта товара).
max_profit, max_profit_id, min_profit_id = 0, 0, 0
# Компания и продукт с максимальной и минимальной прибылью.
company_max_profit, product_max_profit, company_min_profit, product_min_profit = '', '', '', ''


class Algorithm:
    """
    Класс для возвращения максимальых и минимальных цен с учетом затрат и без них и прибьлей компаний и их продуктов,
    id строк в БД с данными значениями.
    """
    def __str__(self):
        return ("Класс для возвращения максимальых и минимальных цен с учетом затрат и без них и прибьлей компаний "
                "и их продуктов, id строк в БД с данными значениями.")

    @staticmethod
    def conclusion_by_company_and_product(list_pricing_model):
        """
        Возвращает весь список данных из БД.
        :param list_pricing_model: Список данных из БД  по определенной компании и продутку.
        global: Глобальные значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        min_price: Минимальная цена без учета затрат.
        min_price_with_expenses: Минимальная цена с учетом затрат (без учета количества товара).
        min_profit: Минимальная прибыль (с учетом количесвта товара).
        :return: Возвращает значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        """
        global list_company, list_product, list_product, max_price, max_price_id, company_max_price, product_max_price
        global max_price_with_expenses, max_price_with_expenses_id, company_max_price_with_expenses
        global product_max_price_with_expenses, min_price_id, company_min_price, product_min_price, product_min_profit
        global min_price_with_expenses_id, company_min_price_price_with_expenses, product_min_price_with_expenses
        global max_profit, max_profit_id, company_max_profit, product_max_profit, min_profit_id, company_min_profit
        min_price = int(list_pricing_model[0][0])
        min_price_with_expenses = int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])
        min_profit = (int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])) * int(list_pricing_model[0][1])

        # Итерация по всем строкам списка 'list_pricing_model'.
        for item in range(0, len(list_pricing_model)):
            # Фильтр по выбранной компании.
            if list_pricing_model[item][3] not in list_company:
                list_company.append(list_pricing_model[item][3])

            # Фильтр по выбранному продукту.
            if list_pricing_model[item][4] not in list_product:
                list_product.append(list_pricing_model[item][4])

            # Поиск максимальной цены без учета затрат, запись принадлежащей ей компанию, продукт и id строки в БД.
            if max_price < int(list_pricing_model[item][0]):
                max_price = int(list_pricing_model[item][0])
                company_max_price = list_pricing_model[item][3]
                product_max_price = list_pricing_model[item][4]
                max_price_id = item

            # Поиск максимальной цены с учетом затрат, запись принадлежащей ей компанию, продукт и id строки в БД.
            if max_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                max_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                company_max_price_with_expenses = list_pricing_model[item][3]
                product_max_price_with_expenses = list_pricing_model[item][4]
                max_price_with_expenses_id = item

            # Поиск минимальной цены без учета затрат, запись принадлежащей ей компанию, продукт и id строки в БД.
            if min_price > int(list_pricing_model[item][0]):
                min_price = int(list_pricing_model[item][0])
                company_min_price = list_pricing_model[item][3]
                product_min_price = list_pricing_model[item][4]
                min_price_id = item

            # Поиск минимальной цены с учетом затрат, запись принадлежащей ей компанию, продукт и id строки в БД.
            if min_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                min_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                company_min_price_price_with_expenses = list_pricing_model[item][3]
                product_min_price_with_expenses = list_pricing_model[item][4]
                min_price_with_expenses_id = item

            # Поиск максимальной прибыли с учетом количества товара, запись принадлежащей ей компанию, продукт и
            # id строки в БД.
            if (max_profit < (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                max_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                company_max_profit = list_pricing_model[item][3]
                product_max_profit = list_pricing_model[item][4]
                max_profit_id = item

            # Поиск минимальной прибыли с учетом количества товара, запись принадлежащей ей компанию, продукт и
            # id строки в БД.
            if (min_profit > (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                min_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                company_min_profit = list_pricing_model[item][3]
                product_min_profit = list_pricing_model[item][4]
                min_profit_id = item

        return (list_company, list_product, max_price, max_price_id, company_max_price, product_max_price,
                max_price_with_expenses, max_price_with_expenses_id, company_max_price_with_expenses,
                product_max_price_with_expenses, min_price, min_price_id, company_min_price, product_min_price,
                min_price_with_expenses, min_price_with_expenses_id, company_min_price_price_with_expenses,
                product_min_price_with_expenses, max_profit, max_profit_id, company_max_profit, product_max_profit,
                min_profit, min_profit_id, company_min_profit, product_min_profit)

    @staticmethod
    def conclusion_by_product(list_pricing_model):
        """
        Возвращает весь список данных из БД.
        :param list_pricing_model: Список данных из БД по определенной компании.
        global: Глобальные значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        min_price: Минимальная цена без учета затрат.
        min_price_with_expenses: Минимальная цена с учетом затрат (без учета количества товара).
        min_profit: Минимальная прибыль (с учетом количесвта товара).
        :return: Возвращает значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        """
        global list_product, max_price, max_price_id, product_max_price, max_price_with_expenses
        global max_price_with_expenses_id, product_max_price_with_expenses, min_price_id, product_min_price
        global min_price_with_expenses_id, product_min_price_with_expenses, max_profit, max_profit_id
        global product_max_profit, min_profit_id, product_min_profit
        min_price = int(list_pricing_model[0][0])
        min_price_with_expenses = int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])
        min_profit = (int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])) * int(list_pricing_model[0][1])

        # Итерация по всем строкам списка 'list_pricing_model'.
        for item in range(0, len(list_pricing_model)):
            # Фильтр по выбранной компании.
            if list_pricing_model[item][4] not in list_product:
                list_product.append(list_pricing_model[item][4])

            # Поиск максимальной цены без учета затрат, запись принадлежащей ей продукт и id строки в БД.
            if max_price < int(list_pricing_model[item][0]):
                max_price = int(list_pricing_model[item][0])
                product_max_price = list_pricing_model[item][4]
                max_price_id = item

            # Поиск максимальной цены с учетом затрат, запись принадлежащей ей продукт и id строки в БД.
            if max_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                max_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                product_max_price_with_expenses = list_pricing_model[item][4]
                max_price_with_expenses_id = item

            # Поиск минимальной цены без учета затрат, запись принадлежащей ей продукт и id строки в БД.
            if min_price > int(list_pricing_model[item][0]):
                min_price = int(list_pricing_model[item][0])
                product_min_price = list_pricing_model[item][4]
                min_price_id = item

            # Поиск минимальной цены с учетом затрат, запись принадлежащей ей продукт и id строки в БД.
            if min_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                min_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                product_min_price_with_expenses = list_pricing_model[item][4]
                min_price_with_expenses_id = item

            # Поиск максимальной прибыли с учетом количества товара, запись принадлежащей ей продукт и id строки в БД.
            if (max_profit < (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                max_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                product_max_profit = list_pricing_model[item][4]
                max_profit_id = item

            # Поиск минимальной прибыли с учетом количества товара, запись принадлежащей ей продукт и id строки в БД.
            if (min_profit > (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                min_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                product_min_profit = list_pricing_model[item][4]
                min_profit_id = item

        return (list_product, max_price, max_price_id, product_max_price, max_price_with_expenses,
                max_price_with_expenses_id, product_max_price_with_expenses, min_price, min_price_id, product_min_price,
                min_price_with_expenses, min_price_with_expenses_id, product_min_price_with_expenses, max_profit,
                max_profit_id, product_max_profit, min_profit, min_profit_id, product_min_profit)

    @staticmethod
    def conclusion_by_company(list_pricing_model):
        """
        Возвращает весь список данных из БД.
        :param list_pricing_model: Список данных из БД по определенному продукту.
        global: Глобальные значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        min_price: Минимальная цена без учета затрат.
        min_price_with_expenses: Минимальная цена с учетом затрат (без учета количества товара).
        min_profit: Минимальная прибыль (с учетом количесвта товара).
        :return: Возвращает значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        """
        global list_company, max_price, max_price_id, company_max_price, max_price_with_expenses
        global max_price_with_expenses_id, company_max_price_with_expenses, min_price_id, company_min_price
        global min_price_with_expenses_id, company_min_price_price_with_expenses, max_profit, max_profit_id
        global company_max_profit, min_profit_id, company_min_profit
        min_price = int(list_pricing_model[0][0])
        min_price_with_expenses = int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])
        min_profit = (int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])) * int(list_pricing_model[0][1])

        # Итерация по всем строкам списка 'list_pricing_model'.
        for item in range(0, len(list_pricing_model)):
            # Фильтр по выбранному продукту.
            if list_pricing_model[item][3] not in list_company:
                list_company.append(list_pricing_model[item][3])

            # Поиск максимальной цены без учета затрат, запись принадлежащей ей компанию и id строки в БД.
            if max_price < int(list_pricing_model[item][0]):
                max_price = int(list_pricing_model[item][0])
                company_max_price = list_pricing_model[item][3]
                max_price_id = item

            # Поиск максимальной цены с учетом затрат, запись принадлежащей ей компанию и id строки в БД.
            if max_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                max_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                company_max_price_with_expenses = list_pricing_model[item][3]
                max_price_with_expenses_id = item

            # Поиск минимальной цены без учета затрат, запись принадлежащей ей компанию и id строки в БД.
            if min_price > int(list_pricing_model[item][0]):
                min_price = int(list_pricing_model[item][0])
                company_min_price = list_pricing_model[item][3]
                min_price_id = item

            # Поиск минимальной цены с учетом затрат, запись принадлежащей ей компанию и id строки в БД.
            if min_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                min_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                company_min_price_price_with_expenses = list_pricing_model[item][3]
                min_price_with_expenses_id = item

            # Поиск максимальной прибыли с учетом количества товара, запись принадлежащей ей компанию и id строки в БД.
            if (max_profit < (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                max_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                company_max_profit = list_pricing_model[item][3]
                max_profit_id = item

            # Поиск минимальной прибыли с учетом количества товара, запись принадлежащей ей компанию и id строки в БД.
            if (min_profit > (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                min_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                company_min_profit = list_pricing_model[item][3]
                min_profit_id = item

        return (list_company, max_price, max_price_id, company_max_price, max_price_with_expenses,
                max_price_with_expenses_id, company_max_price_with_expenses, min_price, min_price_id, company_min_price,
                min_price_with_expenses, min_price_with_expenses_id, company_min_price_price_with_expenses, max_profit,
                max_profit_id, company_max_profit, min_profit, min_profit_id, company_min_profit)

    @staticmethod
    def the_entire_output(list_pricing_model):
        """
        Возвращает весь список данных из БД.
        :param list_pricing_model: Список всех данных из БД.
        global: Глобальные значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        min_price: Минимальная цена без учета затрат.
        min_price_with_expenses: Минимальная цена с учетом затрат (без учета количества товара).
        min_profit: Минимальная прибыль (с учетом количесвта товара).
        :return: Возвращает значения с максимальными и минимальными ценами с учетом затрат и без них и прибьльб компаний
        и их продуктов, id строк в БД с данными значениями.
        """
        global max_price, max_price_id, max_price_with_expenses, max_price_with_expenses_id, min_price_id
        global min_price_with_expenses_id, max_profit, max_profit_id, min_profit_id
        min_price = int(list_pricing_model[0][0])
        min_price_with_expenses = int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])
        min_profit = (int(list_pricing_model[0][0]) - int(list_pricing_model[0][2])) * int(list_pricing_model[0][1])

        # Итерация по всем строкам списка 'list_pricing_model'.
        for item in range(0, len(list_pricing_model)):
            # Поиск максимальной цены без учета затрат и id строки в БД.
            if max_price < int(list_pricing_model[item][0]):
                max_price = int(list_pricing_model[item][0])
                max_price_id = item

            # Поиск максимальной цены с учетом затрат и id строки в БД.
            if max_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                max_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                max_price_with_expenses_id = item

            # Поиск минимальной цены без учета затрат и id строки в БД.
            if min_price > int(list_pricing_model[item][0]):
                min_price = int(list_pricing_model[item][0])
                min_price_id = item

            # Поиск минимальной цены с учетом затрат и id строки в БД.
            if min_price_with_expenses < int(list_pricing_model[item][0]) - int(list_pricing_model[item][2]):
                min_price_with_expenses = int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])
                min_price_with_expenses_id = item

            # Поиск максимальной прибыли с учетом количества товара и id строки в БД.
            if (max_profit < (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                max_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                max_profit_id = item

            # Поиск минимальной прибыли с учетом количества товара и id строки в БД.
            if (min_profit > (int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                    int(list_pricing_model[item][1])):
                min_profit = ((int(list_pricing_model[item][0]) - int(list_pricing_model[item][2])) *
                              int(list_pricing_model[item][1]))
                min_profit_id = item

        return (max_price, max_price_id, max_price_with_expenses, max_price_with_expenses_id, min_price, min_price_id,
                min_price_with_expenses, min_price_with_expenses_id, max_profit, max_profit_id, min_profit,
                min_profit_id,)
