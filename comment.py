#讀取檔案

data = []
with open('reviews.txt', 'r')as f:
    for x in f:
        data.append(x.strip())
print(len(data))
print(data[0])
print('----------------------------------')
print(data[1])