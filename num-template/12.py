for n in range(3, 10_000):
    N = '8' + '4' * n

    while '4444' in N or '844' in N or '84' in N:
        if '4444' in N:
            N = N.replace('4444', '844', 1)
        if '844' in N:
            N = N.replace('844', '448', 1)
        if '84' in N:
            N = N.replace('84', '3343')

