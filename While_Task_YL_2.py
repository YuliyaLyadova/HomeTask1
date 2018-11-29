#Question to Yura: don't understand how def works. As I try to use def algorithm always breaks...
#def ask_user(user_answer):

conv_dictionary={'Как дела?':'Хорошо','Что делаешь?':'Программирую!'}

while True: 
    user_answer=input('Как дела? ')
    
    if user_answer==conv_dictionary['Как дела?']:
        user_answer_2=input('Что делаешь? ')
        while True:
            if user_answer_2==conv_dictionary['Что делаешь?']:
                break 

            else:
                 user_answer_2=input('Что делаешь? ')

    else:
        print('Точно {}? Подумай еще раз!'.format(user_answer))
        