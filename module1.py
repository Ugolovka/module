def gcd(x, y): 
    if(y == 0): 
        return x  # вернуть x
    else: 
        return gcd(y, x % y) 
x =int(input("Введите первое число: ")) # первое число  
y =int(input("Введите второе число: ")) # второе число  
num = gcd(x, y) # вызов функции gcd, чтобы найти результат

def main():
    print("НОД из двух чисел равен: ") 
    print(num) # Вызов num
if __name__ == '__main__':
    main()