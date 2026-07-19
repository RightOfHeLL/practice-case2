import datetime
import calendar

# День недели
def get_weekday(day, month, year):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    date_obj = datetime.date(year, month, day)
    return days[date_obj.weekday()]

# Високосный год
def is_leap_year(year):
    return calendar.isleap(year)

# Расчёт годиков
def get_age(day, month, year):
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Склонения слова
def get_age_word(age):
    age = int(age)
    last_two_digits = age % 100
    last_digit = age % 10

    if 11 <= last_two_digits <= 14:
        return "лет"
    # Смотрим ласт цифру
    if last_digit == 1:
        return "год"
    if last_digit in (2, 3, 4):
        return "года"
    return "лет"

# ВВод даты звездочками в формате ДД ММ ГГГГ
def print_date_ascii(day, month, year):
    date_str = f"{day:02d} {month:02d} {year:04d}"
    
    digits = {
        '0': [" *** ", 
              "*   *", 
              "*   *", 
              "*   *", 
              " *** "],
        '1': ["  *  ", 
              " **  ", 
              "  *  ", 
              "  *  ", 
              " *** "],
        '2': [" *** ", 
              "*   *", 
              "  *  ", 
              " *   ", 
              "*****"],
        '3': [" *** ", 
              "    *", 
              "  ** ", 
              "    *", 
              " *** "],
        '4': ["   * ", 
              "  ** ", 
              " * * ", 
              "*****", 
              "   * "],
        '5': ["*****", 
              "*    ", 
              "**** ", 
              "    *", 
              "**** "],
        '6': [" *** ", 
              "*    ", 
              "**** ", 
              "*   *", 
              " *** "],
        '7': ["*****", 
              "    *", 
              "   * ", 
              "  *  ", 
              "  *  "],
        '8': [" *** ", 
              "*   *", 
              " *** ", 
              "*   *", 
              " *** "],
        '9': [" *** ", 
              "*   *", 
              " ****", 
              "    *", 
              " *** "],
        ' ': ["     ", 
              "     ", 
              "     ", 
              "     ", 
              "     "] # Пробел
    }

    print("\nДата рождения на электронном табло:")
    for i in range(5):
        line = ""
        for char in date_str:
            line += digits[char][i] + "  "
        print(line)


def main():
    print("Добро пожаловать в программу анализа даты рождения!")
    
    # цикл
    while True:
        
        # ВВод
        while True:
            try:
                day = int(input("\nВведите день рождения: "))
                month = int(input("Введите месяц рождения: "))
                year = int(input("Введите год рождения: "))
                
                current_year = datetime.date.today().year
                if year < 1900 or year > current_year:
                    print("Пожалуйста, введите реальный год рождения.")
                    continue
                
                datetime.date(year, month, day)
                break 
                
            except ValueError:
                print("Ошибка! Введена несуществующая дата. Пожалуйста, попробуйте снова.")

        # Ответ
        print(f"\nДень недели: {get_weekday(day, month, year)}")
        
        if is_leap_year(year):
            print(f"Год {year} был високосным.")
        else:
            print(f"Год {year} не был високосным.")
            
        age = get_age(day, month, year)
        age_word = get_age_word(age)
        print(f"Ваш текущий возраст: {age} {age_word}.")
        
        print_date_ascii(day, month, year)
        
        # Выбор
        choice = input("\nХотите проверить еще одну дату? (введите 'да' или 'нет'): ").strip().lower()
        
        if choice == 'нет' or choice == 'n' or choice == 'no':
            print("Завершение работы программы. До свидания!")
            input("Нажмите Enter для выхода...")
            break
        else:
            print("\n" + "="*50)

if __name__ == "__main__":
    main()