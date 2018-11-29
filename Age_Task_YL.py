user_age=int(input('Enter your age: '))

if user_age<7:
    print ('User is '+ str(user_age) + ' years old.'+ 
           ' User is definitely a pre-school kid.')
elif 7<=user_age<18:
    print ('User is '+ str(user_age) + ' years old.'+
        ' User is a school child.')
elif user_age>=18 and user_age<22:
    print ('User is '+ str(user_age) + ' years old.'+
           ' User is a student.')
elif user_age>=22 and user_age<61:
    print ('User is '+ str(user_age) + ' years old.'+
        ' User is highly likely a part of the workforce.')