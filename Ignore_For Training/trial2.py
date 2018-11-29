month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def days_in_month(month):
    if not 1<=month<=12:
        return 'Invalid month'

    if month==2:
        return 29

    else:
        return 'Not February'

    return month_days[month]

print (days_in_month(13))
print (days_in_month(2))
print (days_in_month(7))
print (days_in_month(9))

