# 命名規則 Boaty McBoatface, Horsey McHorseface, Trainy McTrainface

a = 'duck'
b = 'gourd'
c = 'spitz'

# 舊式 %

naming_old = '%sy Mc%sface'

print(naming_old %(a.capitalize(), a.capitalize()))

# 新式 .format() & {}

naming_new = '{}y Mc{}face'

print(naming_new.format(b.capitalize(), b.capitalize()))

print(f'{c.capitalize()}y Mc{c.capitalize()}face')