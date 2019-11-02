# # test to check if two values are equal
# def test(actual,expected):
#     assert actual == expected, "So here {} was not equal to {} as expected".format(actual,expected)
# print("passed all tests!")

assert leap_year("") == False, "not an even number"
assert leap_year("somthing") == False, "Please enter a number"
assert leap_year([1,2,3,4,5]) == False,"numbers exceed number limit"
assert leap_year(-1567) == False, "This is a negeative number"
assert leap_year(1234.5) == False, "No decimals allowed"
print("all tests passed!")