import random
from math import *

# Тут, короче, наскоряк накиданная клёвая игра в угадайку.
#  * Оно число загадывает, а пользователь потом угадывает.
#  * Есть подсказки, на сколько далеко.
#  * todo: DRY, KISS, SOLID (точно можно на ООП-шить), и опечатки по мелочи
#  */

def main():
    answer = input("Привет!\nБудешь угадывать? (да/нет): ")
    if answer == "нет":
        print("(x__x)")
        exit()
    elif answer != "да":
        print("(︶︹︺)\n непонятно, давай до свидания")
        exit()
    print("(⌒‿⌒)")

    while True:
        rand = random.randint(0, 10) + 1
        print("угадай число от 1 до 10")
        while True:
            number = int(input())
            if number == rand:
                print("╰(▔∀▔)╯")
                answer = input("Будешь угадывать? (да/нет): ")
                if answer == "нет":
                    print("(¬_¬)")
                    exit()
                elif answer != "да":
                    print("(︶︹︺)\n непонятно, давай до свидания")
                    exit()
                else:    
                    main()
            else:
                if number < 1 or number > 10:
                    print("Читать не умеешь?")
                elif abs(number - rand) > 5:
                    print("Холодно")
                elif abs(number - rand) > 2:
                    print("Тепло")
                else:
                    print("Жгётся!")      


if __name__ == "__main__":

    main()




