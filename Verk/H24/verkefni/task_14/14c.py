def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


user = int(input("settu inn tolu: "))
print(f"nidurstadan er = {factorial(user)}")
