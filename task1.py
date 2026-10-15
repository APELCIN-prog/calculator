def shifr(word, step):
    res = ''
    for s in word:
        if s in eng_alf:
            res += eng_alf[(eng_alf.index(s) + step) % len(eng_alf)]
        else:
            res += rus_alf[(rus_alf.index(s) + step) % len(rus_alf)]

    return res

def deshifr(word, step):
    res = ''
    for s in word:
        if s in eng_alf:
            res += eng_alf[(eng_alf.index(s) - step) % len(eng_alf)]
        else:
            res += rus_alf[(rus_alf.index(s) - step) % len(rus_alf)]

    return res


eng_alf = 'abcdefghijklmnopqrstuvwxyz'
rus_alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = input().lower()
step = int(input())

sh = shifr(word, step)
print(sh)
print(deshifr(sh, step))