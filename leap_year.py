months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(month, year):
    month = month.capitalize()
    if month not in months:
        return None
    
    month_index = months.index(month)

    if month_index == 1:
        if leap_year(year):
            return 29
        else:
            return 28
    elif month_index in [3, 5, 8, 10]:
        return 30
    else:
        return 31    


year_input = int(input("Enter a year: "))
month_input = input("Enter month: ")
days = days_in_month(month_input, year_input)

# check if year is leap or not
if leap_year(year_input):
    print(year_input, "is a leap year")
else:
    print(year_input, "not a leap year")

# check number of days in a given month
if days is not None:
    print(month_input.capitalize(), "has", days, "days in", year_input)
else:
    print("Error Error")