#讀取檔案
count = 0
data = []
with open('reviews.txt', 'r')as f:
    for x in f:
        data.append(x.strip())
        count += 1
        if count % 100000 == 0:
            print(len(data))
print(len(data))
print(data[0])
print('----------------------------------')
print(data[1])