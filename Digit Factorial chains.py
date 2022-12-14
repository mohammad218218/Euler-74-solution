def factorial(n):
    s = 1
    while n > 1:
        s = (n * (n-1)) * s
        n = n-2
    return s


def number_show(number):
    sum = 0
    while number != 0:
        sum = factorial(number % 10) + sum
        number = number // 10
    return sum


def checking(number):
    l1 = []
    while number not in l1:
        l1.append(number)
        number = number_show(number)
        if number in l1:
            if len(l1) == 60:
                return True
            break


count = 0
for i in range(1, 1000000):
    if checking(i):
        count = count + 1
print(count)
