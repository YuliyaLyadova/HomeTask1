

def main():
    user_age = int(input('Enter your age: '))

    if user_age < 7:
        print(f'User is {user_age} years old.\nUser is definitely a pre-school kid.')
    elif 7 <= user_age < 18:
        print(f'User is {user_age} years old.\nUser is a school child.')
    elif 18 <= user_age < 22:
        print(f'User is {user_age} years old.\nUser is a student.')
    elif 22 <= user_age < 61:
        print(f'User is {user_age} years old.\nUser is highly likely a part of the workforce.')
    else:
        print(f'User is {user_age} years old.\nUser is probably retired.')


if __name__ == '__main__':
    main()
