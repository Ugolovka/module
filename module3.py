x = int(input("Номер уровня-" ))
# Вызов рекурсии
def combination(n, k):
    if k == 0 or k == n: # условие
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k) #вернуть комбо

def pascals_triangle(rows): #функция 
    for row in range( rows):
        answer = ""
        for column in range( row + 1):
            answer = answer + str(combination(row, column)) + "\t"
            print(answer)

def main():
    print("Треугольник Паскаля: ")
    pascals_triangle(x) # Вызов
if __name__ == '__main__':
    main()