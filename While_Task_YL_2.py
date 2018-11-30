# Question to Yura: don't understand how def works. As I try to use def algorithm always breaks...
# def ask_user(user_answer):

# answer: def is from word define. This tag means only that next part of a python code is function. Nothing more.


conv_dictionary = {
    'Хорошо': 'Отлично!',
    'Как дела?': 'Хорошо',
    'Что делаешь?': 'Программирую!'
}


def main():

    while True:
        user_answer = input('Как дела? ')

        if user_answer in conv_dictionary: # In this case Python will look for dict keys.
            return conv_dictionary[user_answer]
        else:
            print('Точно {}? Подумай еще раз!'.format(user_answer))
            continue


if __name__ == '__main__':
    print(main())
