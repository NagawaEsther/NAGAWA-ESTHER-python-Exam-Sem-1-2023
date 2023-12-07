#i)
def calculate_area(radius):
    return 3.14 * radius**2

area = calculate_area(5)
print(area)


#ii)
def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n-1)

# Testing the function with n = 4
print(calculate_sum(4))

#iii)
# Remove element at index 2 and insert value 10 at the end of the list
numbers = [1, 3, 5, 7, 9]
del numbers[2] 
numbers.append(10)
print(numbers)


#iv)
# using list comprehension ,create a new list that contains only the even numbers from the original list.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in list if num % 2 == 0]
print(even_numbers)


#v)
# Given the dictionary below,Update the value of "age" to 25 and add a new key-value pair ()"city":"New York")
dict = {"name": "Alice", "age": 20, "grade": "A"}
dict["age"] = 25
dict["city"] = "New York"
print(dict)


#vi)
# Using dictionary comprehension ,create a new dictionary with only key-value pairs where the value is greater than 5.original_dict={"a":3,"b":8,"c":2,"d":7}
original_dict = {"a": 3, "b": 8, "c": 2, "d": 7}
new_dict = {key: value for key, value in original_dict.items() if value > 5}
print(new_dict)







