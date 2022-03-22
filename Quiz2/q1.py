cipher = 'ECDTMECAERAUOOLEDSAMMERNENASSODYTNRVBNLCRLTIQLAETRIGAWEBAAEIHOR'

size = len(cipher)

# 7*9
list1 = [0,0,0,0,0,0,0] # 有七個橫排，所以一開始放七個零，代表每排的母音數量
vowel1 = 9*0.4 # 一排有九個字母，是母音的機率為40%，所以一排應該有9*0.4個母音

# 因為要寫成直排，所以%7之後的餘數代表那個字母在第幾排，接著判斷是否為母音，如果是，那排的母音數量加一
for i in range(size):
    if cipher[i] == 'A' or cipher[i] == 'E' or cipher[i] == 'I' or cipher[i] == 'O' or cipher[i] == 'U':
        list1[i%7] += 1

total1 = 0 # 計算答案的值

# 七個橫排分別算出真正有的和該有的絕對值，並且加總
for i in range(7):
    total1 += abs(list1[i]-vowel1)

# 9*7
list2 = [0,0,0,0,0,0,0,0,0] # 九個橫排，代表每排的母音數量，初始值為零
vowel2 = 7*0.4 # 一排有七個字母，是母音的機率為40%，所以一排應該有7*0.4個母音

# 因為要寫成直排，所以%9之後的餘數代表那個字母在第幾排，接著判斷是否為母音，如果是，那排的母音數量加一
for i in range(size):
    if cipher[i] == 'A' or cipher[i] == 'E' or cipher[i] == 'I' or cipher[i] == 'O' or cipher[i] == 'U':
        list2[i%9] += 1

total2 = 0 # 計算答案的值

# 九個橫排分別算出真正有的和該有的絕對值並加總
for i in range(9):
    total2 += abs(list2[i]-vowel2)
    
# 比較何者較小，找出其dimension
if(total1<total2):
    print('dimension is 7*9')
elif(total1>total2):
    print('dimension is 9*7')
else:
    print('both 7*9 or 9*7 is ok')
