things = ["mozzarella", "cinderella", "salmonella"]

#01 人名首字母大寫

things[things.index("cinderella")] = things[things.index("cinderella")].capitalize()
print("01 人名首字母大寫")
print(things)

#02 乳酪全大寫

things[things.index("mozzarella")] = things[things.index("mozzarella")].upper()
print("02 乳酪全大寫")
print(things)

#03 移除致病元素

things.remove("salmonella")
print("03 移除致病元素")
print(things)

