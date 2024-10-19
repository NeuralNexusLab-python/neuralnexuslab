import csv
import random
import io

# 用戶輸入
num = int(input('人數?: '))
x = int(input('寬?(x): '))
y = int(input('長?(y): '))
fc = input('輸入(f)快速抽籤，輸入(c)以抽數字方式抽籤: ')

nuum = []
lines = []
c = 0
v = ''
s = ''
lines.append('隨機座位表:')
for i in range(num):
    nuum.append(str(i + 1) + '號')
while len(nuum) < (x * y):
    nuum.append(' ')
random.shuffle(nuum)
for i in nuum:
    if fc == 'c':
        s = input('現在輪到' + i + '，請從' + str(random.randrange(0, 6)) + '~' + str(random.randrange(6, 10)) + '選一個: ')
    if c == x:
        lines.append(v)
        c = 0
        v = i + ','
    else:
        v = v + i + ','
        c += 1

# 使用 StringIO 儲存 CSV 格式的內容
output = io.StringIO()
writer = csv.writer(output)

for line in lines:
    writer.writerow(line.split(","))

# 將 StringIO 中的內容寫入至 CSV 文件
csv_content = output.getvalue()

# 輸出結果，提示用戶可以下載 CSV
print('CSV 內容:\n', csv_content)

# 在這裡，您可以把這段程式碼嵌入到 Flask 或其他 Web 框架來直接提供下載功能
# 例如：Flask
# return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=隨機座位表.csv"})
