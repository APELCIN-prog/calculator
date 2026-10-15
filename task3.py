def print_pack_report(num):
    if num < 1:
        print('Такое не фасуем')
        return

    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} - расфасуем по 3 или по 5')
    elif num % 5 == 0:
        print(f'{num} - расфасуем по 5')
    elif num % 3 == 0:
        print(f'{num} - расфасуем по 3')
    else:
        print(f'{num} - не заказываем!')

n = int(input())
print_pack_report(n)