base = int(input("Введите основание: ")) # Основание
number = int(input("Введите  число: ")) # Число

def convert_to_base(number, base):
    if number < base:
        return "0123456789ABCDEF"[number]  # Возвращаем символ для числа < base
    else:
        return convert_to_base(number // base, base) + "0123456789ABCDEF"[number % base]

def main():
    print("Результат: ", convert_to_base(number, base)) 
if __name__ == '__main__':
    main()