x = 3    
while x == 3:
    password = input('請輸入密碼: ')
    if password == ('a123456'):
        print('登入成功')
        break
    elif password != ('a123456'):
        x = x - 1
        print('登入失敗您還有2次機會')
while x == 2:
    password = input('請輸入密碼: ')
    if password == ('a123456'):
        print('登入成功')
    elif password != ('a123456'):
        x = x - 1
        print('登入失敗您還有1次機會')
while x == 1:
    password = input('請輸入密碼: ')
    if password == ('a123456'):
        print('登入成功')
    elif password != ('a123456'):
        x = x - 1
        print('登入失敗您還有0次機會')        