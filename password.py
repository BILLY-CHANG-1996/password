password = 'a123456'
i = 3
while i > 0:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break
    else:
        i = i - 1
        print('登入失敗您還有' ,i ,'次機會')
     