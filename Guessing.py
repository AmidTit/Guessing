import random
import math

class GuessNumber:

    def generate_number(self):

        return random.randint(self.lower, self.upper)
    
    
    def __init__(self, lower = 0, upper = 10):

        self.lower, self.upper = lower, upper
        self.win_number = self.generate_number()


    def play_game(self):

        while True:

            rand = self.generate_number()
            print("угадай число от %d до %d: " % (lower, upper))

            while True:

                number = int(input())

                if number == rand:
                    print("╰(▔∀▔)╯")
                    self.greeting(i=1)

                else:

                    if number < lower or number > upper:
                        print("Читать не умеешь?")

                    elif abs(number - rand) > 5:
                        print("Холодно")

                    elif abs(number - rand) > 2:
                        print("Тепло")

                    else:
                        print("Жгётся!")
                         

    def greeting(self, i=0):

        answers_list = ["Привет!\nБудешь угадывать? (да/нет): ", "Поиграем еще? (да/нет): "]
        answer = input(answers_list[i]).lower()

        if answer == "нет":

            print("(x__x)")
            return 
        
        elif answer != "да":

            print("(︶︹︺)\n непонятно, давай до свидания")
            return
        
        else:
            print("(⌒‿⌒)")
            self.play_game()

    
if __name__ == "__main__":
    lower, upper = 0, 10
    guess_num = GuessNumber()
    guess_num.greeting()



