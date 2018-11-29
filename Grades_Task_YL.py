grades_dictionary=[{'school_class': '4a', 'grades': [3,4,4,5,2]}, {'school_class': '4b', 'grades': [5,5,2,3,2]},{'school_class': '4c', 'grades': [5,5,4,4,5]}]
grades_list=[item['grades'] for item in grades_dictionary]
print(grades_list)
mergedlist=grades_list[0]+grades_list[1]+grades_list[2]
print(mergedlist)
average_grade=float(sum(mergedlist)/len(mergedlist))
print('The average grade in school is '+ str(average_grade))

#average grade for each of three classes below

grades_list_4a=grades_dictionary[0]['grades']
average_grade_4a=float(sum(grades_list_4a)/len(grades_list_4a))
print('The average grade in 4a is '+str(average_grade_4a))

grades_list_4b=grades_dictionary[1]['grades']
average_grade_4b=float(sum(grades_list_4b)/len(grades_list_4b))
print('The average grade in 4b is '+str(average_grade_4b))

grades_list_4c=grades_dictionary[2]['grades']
average_grade_4c=float(sum(grades_list_4c)/len(grades_list_4c))
print('The average grade in 4c is '+str(average_grade_4c))

# Question to Yuri: how to use 'for' to automate calculation of average grade in each class. Should I use function 'def' that I create?