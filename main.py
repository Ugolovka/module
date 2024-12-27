import module1 as m1
import module2 as m2


from complex_module import module4 as m4
import complex_module.module4 as m4

def main():
    user_choise = input("Choose Y "
            "if you want to convert euclid, else choose N: ")
    if user_choise.lower() == 'y':
        user_temp = float(input("Input number in"
                            "..."))
        print("sf" , m1.gcd())
    else:

        m4.hello4()
        main()

if __name__ == "__main__":
    main()