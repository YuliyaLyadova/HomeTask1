from itertools import chain


def get_mean(numbers_list):
    return float(sum(numbers_list)/len(numbers_list))


def get_average_grade_for_every_cls(grades_list):
    result = {}

    for school_cls in grades_list:
        result[school_cls["school_class"]] = get_mean(school_cls["grades"])

    return result


def main():
    grades_dictionary=[
        {'school_class': '4a', 'grades': [3, 4, 4, 5, 2]},
        {'school_class': '4b', 'grades': [5, 5, 2, 3, 2]},
        {'school_class': '4c', 'grades': [5, 5, 4, 4, 5]}
    ]

    grades_list = [item['grades'] for item in grades_dictionary]

    # mergedlist=grades_list[0]+grades_list[1]+grades_list[2]
    # print(mergedlist)
    # Bad decision because there could be more lists. More universal way further.

    merged_list = list(chain(*grades_list))
    average_grade = get_mean(merged_list)
    print(f'The average grade in school is {average_grade:.2f}.')

    # The {average_grade:.2f} will give you 2 number after dot.
    # More info here: https://www.python.org/dev/peps/pep-0498/#format-specifiers
    # Or you can use round() function from python. https://docs.python.org/3.6/library/functions.html

    result = get_average_grade_for_every_cls(grades_dictionary)

    for item in result.items():
        print(f"Average result for class {item[0]} is {item[1]}.")

    # Question to Yuri: how to use 'for' to automate calculation of average grade in each class.
    # Should I use function 'def' that I create?

if __name__ == '__main__':
    main()
