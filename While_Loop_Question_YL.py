list_names=[0,'Вася','Маша','Петя','Валера','Саша','Даша']

#def find_person(num):
#question to Yura: tried to create function that will look through each element of the list and compare it to Валера. The algorythm is working. When I add def it breaks.
 
num = 0
while num < (len(list_names)-1):
    num += 1
   
    name=list_names[num]
    
    if name=='Валера':
        print ('Валера нашелся')

       
