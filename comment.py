#讀取檔案
count = 0
data = []
with open('reviews.txt', 'r')as f:
    for x in f:
        data.append(x.strip())
        count += 1
        if count % 100000 == 0:
            print(len(data))
print('總共有', len(data), '筆資料')
print(data[0])
print('----------------------------------')
print(data[1])

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言的平均長度', sum_len/len(d))
print('留言的平均長度', sum_len/len(data))

print(len(d))
print(len(data))