import random


def get_random_number():
    x = random.randint(1, 10)

    return int(x)


def get_guess():
    x = input('Raad een getal tussen de 1 en 10: ')

    return x


def check_if_int(number):
    x = number

    try:
        int(x)

    except:
        print('Verkeerde invoer, probeer opnieuw.')
        return False
    
    else:
        return int(x)


def guess_number():
    y = False
    while y == False:
        x = get_guess()
        y = check_if_int(x)

        if type(y) is int:
            return y


def check_number(number, guess):
    x = guess
    y = number

    if x == y:
        return True
    else: 
        return False


def amount_guesses():
    y = False
    
    while y == False:
        x = input('Hoeveel keer wil je raden? ')
        y = check_if_int(x)

        if type(y) is int:
            return y


def guess_game():
    rn = get_random_number()
    print(rn)
    x = amount_guesses()

    while x > 0:
        guess = guess_number()
        cn = check_number(rn, guess)
        if x >= 1:
            if cn == False:
                print('Verkeerd getal, probeer nog eens.')
                x -= 1
            elif cn == True:
                print('Gefeliciteerd! Je hebt het getal geraden!')
                break
        else:
            print('Helaas. Je beurten zijn op.')
            break


if __name__ == '__main__':
    guess_game()