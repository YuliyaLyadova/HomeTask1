# question to Yuri: It doesn't make sense to me how to create a function.
# I don't understand what is function supposed to return.

# question to Yuri: no sence to check the type of str_1 and str_2 as by design variables are of string type
# answer: by design user could enter anything, what he or she wants but your script has to check out that those
# entered variables are truly strings.


def is_strings(first_string, second_string):
    if type(first_string) == str and type(second_string) == str:
        return '\nBoth variables are strings.'
    else:
        return 0


def main(first_string, second_string):

    check_strings = is_strings(first_string, second_string)

    if check_strings == 0:
        return 0
    else:
        print(check_strings)

    if len(first_string) == len(second_string):
        return 1
    elif len(first_string) > len(second_string):
        return 2
    elif len(first_string) != len(second_string) and second_string == 'learn':
        return 3
    elif len(first_string) < len(second_string):
        return 4


if __name__ == '__main__':
    str_1 = input('Enter the 1st string: ')
    str_2 = input('Enter the 2nd string: ')
    print(main(str_1, str_2))
