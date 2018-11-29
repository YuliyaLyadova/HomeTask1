#question to Yuri: doesn't make sense for me to create fuction. don't understand waht fucntion is supposed to return
def comp_str(str_1,str_2, delimeter=' '):
    return str_1+delimeter+str_2

# question to Yuri: no sence to check the type of str_1 and str_2 as by design variables are of string type

str_1=input('Enter the 1st string: ')
str_2=input('Enter the 2nd string: ')

if (type(str_1)==str and type(str_2)==str):
    print ('Both variables are of str type') 

    if len(str_1)==len(str_2):
        print ('1')
    elif len(str_1)>len(str_2):
            print ('2')
    elif len(str_1)!=len(str_2) and str_2=='learn':
        print ('3')
    elif len(str_1)<len(str_2):
        print ('4')

else:
    print ('0')
