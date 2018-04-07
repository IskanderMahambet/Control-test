fio = input('Введите ФИО: ')


fioMas = fio.split(' ')

fName = fioMas[1].capitalize()
lName = fioMas[0].capitalize()
mName = fioMas[2].capitalize()

print(lName + ' ' + fName + ' ' + mName)
