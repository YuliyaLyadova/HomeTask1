mylist=['Вася','Маша','Петя','Валера', 'Саша', 'Даша']
while True:
    x=mylist.pop()
    if x!='Валера':
        mylist.insert(0,x)
        
else:
    print('Валера нашелся')