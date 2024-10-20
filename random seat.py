import csv
import random
num = int(input('人數?: '))
x = int(input('寬?(x): '))
y = int(input('長?(y): '))
fc = input('輸入(f)快速抽籤，輸入(c)以抽數字方式抽籤: ')
if input('是否指定下載資料?(沒有就會直接顯示) 請輸入y或n: ') == 'y':
    user_input = input('指定路徑: ')
    output = user_input
else:output = False
nuum = []
lines = []
c = 1
v = ''
s = ''
lines.append('隨機座位表:')
for i in range(num):nuum.append(str(i + 1) + '號')
while len(nuum) == (x * y):nuum.append(' ')
random.shuffle(nuum)
for i in nuum:
    v = v + i + ','
    c += 1
    if fc == 'c':
        s = input('現在輪到' + i + '，請從' + str(random.randrange(0,6)) + '~' + str(random.randrange(6,10)) + '選一個: ')
    if c == x:
        lines.append(v)
        c = 0
        v = ''
if output != False:
    # 設定 CSV 文件的儲存路徑（在桌面上)
    csv_path = output
    # 創建 CSV 文件並寫入內容
    with open(csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for line in lines:
            writer.writerow(line.split(","))
else:
    for i in lines:print(i)
print('文件已儲存')
