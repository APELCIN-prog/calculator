d1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
d2 = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
    10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
    60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
    100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
    600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
    1000: 'M'
}


def rim_to_num(num):
    res = 0
    for i in range(len(num) - 1):
        if d1[num[i]] < d1[num[i + 1]]:
            res -= d1[num[i]]
        else:
            res += d1[num[i]]
    res += d1[num[-1]]
    return res


def num_to_rim(num):
    res = ''
    place = 1
    while num > 0:
        n = (num % 10) * place
        print(n)
        for k in sorted(d2.keys(), reverse=True):
            if n % k == 0:
                res = (d2[k] * (n // k)) + res
                break
        num //= 10
        place *= 10
    print(res)


num_to_rim(5237)
