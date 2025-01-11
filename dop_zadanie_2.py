import random


def password():
    n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n1 = random.choice(n)
    result = []
    for i in range(1, 20):
        for j in range(i + 1, 21):
            if n1 % (i + j) == 0:
                result.append(f"{i}+{j}")
    return n1, result


n1, pas = password()
print("Число из первой встваки:", n1)
print("Нужный пароль:", pas)
