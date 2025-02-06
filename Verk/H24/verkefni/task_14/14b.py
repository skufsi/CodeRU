def test_range(num, start_range, end_range):
    if num >= start_range and num <= end_range:
        return True
    else:
        return False

user_num = int(input("settu inn tolu: "))
user_start = int(input("settu inn byrjun talnabils: "))
user_end = int(input("settu inn enda talnabils: "))

if test_range(user_num, user_start, user_end):
    print("talan er i talnabilinu")
else:
    print("talan er ekki i talnabilinu")
    