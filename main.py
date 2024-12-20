import re
from datetime import datetime


def is_valid_date(date_string):
    # Регулярное выражение для проверки формата даты (с русскими месяцами)
    pattern = r'^\d{1,2} (Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Ноя|Дек), \d{4}$'
    
    if not re.match(pattern, date_string):
        return False
    
    # Преобразуем строку в дату с учетом русских месяцев
    months = {
        'Янв': 'Jan', 'Фев': 'Feb', 'Мар': 'Mar', 'Апр': 'Apr', 'Май': 'May', 'Июн': 'Jun',
        'Июл': 'Jul', 'Авг': 'Aug', 'Сен': 'Sep', 'Окт': 'Oct', 'Ноя': 'Nov', 'Дек': 'Dec'
    }
    
    # Заменяем русские месяцы на английские
    for rus_month, eng_month in months.items():
        date_string = date_string.replace(rus_month, eng_month)
    
    # Преобразуем строку в дату с английскими месяцами
    try:
        date_obj = datetime.strptime(date_string, '%d %b, %Y')
        return True
    except ValueError:
        return False


def main():
    print('Введите проверяемую дату: ')
    date_str = input()
    print(f"{date_str}: {'Корректная' if is_valid_date(date_str) else 'Некорректная'}")


if __name__ == "__main__":
    main()
