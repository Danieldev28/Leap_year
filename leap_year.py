year = input("Enter a number: ")

def leap_year(year):
    if type(year) == str:
        if year.isnumeric() == True:
            if int(year) % 4 == 0:
                return True
            else: 
                return False
        else:
            return False
    else: 
        return False
    
print(leap_year(year))