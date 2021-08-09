print('\n\033[34mHello, world.\033[m\n')

ok = True
while ok:
    week = list()
    for c in range(0, 7):
        day = int(input(f'Day { c + 1 }˚: '))
        week += [day]
    
    numerator = sum(week)
    average = numerator / 7
    print(f'Average: {average:.2f}')
    answer = str(input('Do you want to continue: [\033[34mY\033[m | \033[31mN\033[m]]: ')).title()[0]

    if answer == 'Y':
        continue
    elif answer == 'N':
        ok = False
    else:
        continue

print('See you later.')