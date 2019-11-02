year = input("Enter a number: ")

def leap_year(year):
    if type(year) == str:
        return False
    else:
        return True
    if year % 4 == 0:
        return True
    else: 
        return False
    if year % 100 == 0:
         return True
    else: 
        return False
    if year % 400 == 0:
        return True
    else: 
        return False

assert leap_year("") == False, "not an even number"
assert leap_year("somthing") == False, "Please enter a number"
assert leap_year([1,2,3,4,5]) >= False,"numbers exceed number limit"
assert leap_year(-1567) ==
print("all tests passed!")