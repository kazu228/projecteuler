# 二乗和の差

def add(last_number):
    result = 0

    for i in range(1, last_number+1):
        result += i ** 2

    return result


def squaring(last_number):
    result = 0

    for i in range(1, last_number+1):
        result += i

    return result ** 2


num1 = add(100)
num2 = squaring(100)

answer = num2 - num1
print(answer)


