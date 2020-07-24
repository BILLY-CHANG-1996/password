password = 'a123456'
i = 3
while i > 0:
    i = i - 1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break
    else:
        print('登入失敗')
        if i > 0:
            print('還有', i ,'次機會')
        else:
            print('嘗試次數過多帳號已遭凍結')
     