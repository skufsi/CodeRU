def sum_of_three(a, b, c):
    calc = a + b + c
    return calc

num1 = int(input("settu inn fyrstu toluna: "))
num2 = int(input("settu inn seinni toluna: "))
num3 = int(input("settu inn thridju toluna: "))

print(f"summan er {sum_of_three(num1, num2, num3)}")