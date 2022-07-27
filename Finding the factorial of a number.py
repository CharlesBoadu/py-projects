num = eval(input("Enter the number to find the factorial: "))

a = 1
result = 0
end_result = 1
for i in range(1, num + 1):
    result = a * i
    end_result *= result
    
print(f"The factorial of {num} is {end_result}")
