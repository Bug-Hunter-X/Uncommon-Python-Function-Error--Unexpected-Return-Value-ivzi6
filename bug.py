def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  #Incorrect return statement for the function
    return a / b

result = function_with_uncommon_error(10, 0)
print(result)