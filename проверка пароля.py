pas= input()
digit=('1','2','3','4','5','6','7','8','9','0')
letters= ('q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m')
symbols = ('!','@','#','$','%','^','&','*','(',')','-','_','=','+','/' )
has_digit=False
has_letter=False
has_symbol=False

for sym in pas:
    if sym in digit:
        has_digit = True
    if sym in letters:
        has_letter= True
    if sym in symbols:
        has_symbol=True
if len(pas) >= 8 and has_digit == True and has_letters == True and has_symbol == True:
    print('Пароль годный!')
else:
    print('Пароль плохой')
