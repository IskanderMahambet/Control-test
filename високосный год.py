god = int(input('Введите год: '))

if god % 4 ==0 and god % 400 ==0 and god % 100 ==0:
    print('Это високосный год')
elif god % 4 ==0 and god % 100 !=0:
    print('Это високосный год')
else:
    print('Это не високосный год')

