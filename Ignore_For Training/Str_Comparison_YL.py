str_1=input('Enter the 1st string: ')
str_2=input('Enter the 2nd string: ')
if type(str_1)==str and type(str_2)==str and len(str_1)==len(str_2):
    print ('1')
elif type(str_1)==str and type(str_2)==str and len(str_1)>len(str_2):
    print ('2')
elif type(str_1)==str and type(str_2)==str and len(str_1)!=len(str_2) and str_2=='learn':
    print ('3')
elif type(str_1)==str and type(str_2)==str and len(str_1)<len(str_2):
        print ('4')
elif type(str_1)!=str or type(str_2)!=str:
    print ('0')
# question to Yuri: no sence to check the type of str_1 and str_2 as by design variables are of string type