# 預設參數值於函式被定義的時候計算，而非執行的時候
# 可變的資料型態(串列、字典)不適合當作預設參數

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

# 正確做法

def buggy(arg):
    result = []
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

# 修正做法

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')

# 遞迴呼叫函式

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

lol = [1, 2, [3, 4, 5], [6, [7, 8, [9], []]]]
print(list(flatten(lol)))

# 例外處理

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index :', position)
    except Exception as other:
        print('Something else broke :', other)

