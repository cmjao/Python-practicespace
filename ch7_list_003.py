surprise = ['Groucho', 'Chico', 'Harpo']

# 最後一個元素改成小寫，將它反過來，再將它的第一個字母改成大寫

print('最後一個元素改成小寫，將它反過來，再將它的第一個字母改成大寫')
print(surprise)
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise)

# even list 包含 range(10) 之內的偶數

print('even list 包含 range(10) 之內的偶數')
even = [num for num in range(10) if num % 2 ==0]
print(even)