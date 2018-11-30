list_names=[0,'Вася','Маша','Петя','Валера','Саша','Даша']

#def find_person(num):
#question to Yura: tried to create function that will look through each element of the list and compare it to Валера. The algorythm is working. When I add def it breaks.
 
# num = 0
# while num < (len(list_names)-1):
#     num += 1
#
#     name=list_names[num]
#
#     if name=='Валера':
#         print ('Валера нашелся')


# answer: Hope I've answered your question!
#         Python has a lot of specially prepared function for different jobs.
#         Best way to remember them is to use them!
#         Read about enumerate:
#         Docs: https://docs.python.org/3.6/library/functions.html

def find_person(names_list):
    for num, name in enumerate(names_list):
        if name == "Валера":
            return f"Валера нашелся! И его имя на {num} месте!"


def main():
    print(find_person(list_names))


if __name__ == '__main__':
    main()
