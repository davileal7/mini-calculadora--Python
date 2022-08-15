from time import sleep

while True:
    print('Digite apenas uma das opções abaixo:')
    opção = input('\033[34m[1] para adição\033[m'
                      '\033[32m [2] para subtrair\033[m'
                      '\033[33m [3] para multiplicar\033[m'
                      '\033[35m [4] para dividir:\033[m').strip()

    if opção == '1':
        print('\033[34mADIÇÃO\033[m')
        a = int(input('número: '))
        b = int(input(f'{a} + '))
        s = a + b
        print(f'{a} + {b} = {s}')
        r = str(input('Quer encerrar? S/N ')).upper()

        while r not in 'S' 'N':
            print('\033[31mERRO\033[m')
            print('Digite apenas S ou N')
            r = str(input('Quer encerrar? S/N ')).upper()

        if r == 'N':
            print('OK')
            sleep(1)
        elif r == 'S':
            sleep(1)
            print('\033[36m--end is program--\033[m')
            break

    elif opção == '2':
        print('\033[32mSUBTRAÇÃO\033[m')
        a = int(input('número: '))
        b = int(input(f'{a} - '))
        s = a - b
        print(f'{a} - {b} = {s}')
        r = str(input('Quer encerrar? S/N ')).upper()

        while r not in 'S' 'N':
            print('\033[31mERRO\033[m')
            print('Digite apenas S ou N')
            r = str(input('Quer encerrar? S/N ')).upper()

        if r == 'N':
            print('OK')
            sleep(1)
        elif r == 'S':
            sleep(1)
            print('\033[36m--end is program--\033[m')
            break

    elif opção == '3':
        print('\033[33mMULTIPLICAÇÃO\033[m')
        a = int(input('número: '))
        b = int(input(f'{a} x '))
        s = a * b
        print(f'{a} x {b} = {s}')
        r = str(input('Quer encerrar? S/N ')).upper()

        while r not in 'S' 'N':
            print('\033[31mERRO\033[m')
            print('Digite apenas S ou N')
            r = str(input('Quer encerrar? S/N ')).upper()

        if r == 'N':
            print('OK')
            sleep(1)
        elif r == 'S':
            sleep(1)
            print('\033[36m--end is program--\033[m')
            break

    elif opção == '4':
        print('\033[35mDIVISÃO\033[m')
        a = float(input('número: '))
        b = float(input(f'{a:.0f} / '))
        s = a / b
        print(f'{a:.0f} / {b:.0f} = {s:.1f}')
        r = str(input('Quer encerrar? S/N ')).upper()

        while r not in 'S' 'N':
            print('\033[31mERRO\033[m')
            print('Digite apenas S ou N')
            r = str(input('Quer encerrar? S/N ')).upper()

        if r == 'N':
            print('OK')
            sleep(1)
        elif r == 'S':
            sleep(1)
            print('\033[36m--end is program--\033[m')
            break













