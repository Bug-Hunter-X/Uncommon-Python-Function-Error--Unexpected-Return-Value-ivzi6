def function_with_uncommon_error(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    result = function_with_uncommon_error(10, 0)
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)

result2 = function_with_uncommon_error(10,2)
print(result2)