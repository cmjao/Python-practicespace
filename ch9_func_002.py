# 產生器函式 : 回傳範圍內的奇數

def get_odds(n):
    for num in range(n):
        if num % 2 == 1:
            yield num

# 使用 for 迴圈印出第三個回傳值

t = 1
for x in get_odds(10):
    if t == 3:
        print(x)
    t += 1