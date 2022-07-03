def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 8
    two_sum(lst, target)
    two_sum_hashed(lst, target)


def two_sum(lst, target):
    print("Результат сложности О(n^2):")
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] == target - lst[i]:
                print("({0},{1})".format(i, j))


def two_sum_hashed(lst, target):
    slovarF = {}
    otricatslovar = {}
    dict = {}
    for k in range(len(lst)):
        slovarF[k] = lst[k]
    for k in range(len(lst)):
        otricatslovar[k] = target - slovarF[k]
    for k in range(len(lst)):
        num = otricatslovar.get(k)
        znachenie = list(slovarF.values())
        kluch = list(slovarF.keys())
        if num in znachenie[k + 1:len(lst)]:
            num = znachenie.index(num, k + 1, len(lst))
            kluchZnach = kluch.pop(num)
            dict.setdefault(k, [kluchZnach])
    itog = dict.items()
    print(itog)


main()