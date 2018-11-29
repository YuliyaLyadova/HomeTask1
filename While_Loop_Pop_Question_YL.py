mylist=['Вася','Маша','Петя','Валера', 'Саша', 'Даша']
if 'Валера' in mylist:
    print('Валера нашелся')
# question to Yura: variant #2 algoritm doesn't work as I ask to return x back to the list otherwise I get an error that my list is empty
#
#
#
#mylist=['Вася','Маша','Петя','Валера', 'Саша', 'Даша']
#while True:
#    x=mylist.pop(-len(mylist)+1)
#    
#    if x!='Валера' mylist.append('x'):
#    break

#    else: 
#        print('Валера нашелся #2')

#Question to Yura: below is my variant #1. Doesn't work as list is considered to be empty
mylist=['Вася','Маша','Петя','Валера', 'Саша', 'Даша']
while True:
    x=mylist.pop(-len(mylist)+1)
    
    if x!='Валера':
        print (x)
    
    else: 
        print('Валера нашелся #2')