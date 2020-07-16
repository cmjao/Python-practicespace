# 將m開頭的單字改為首字大寫

song = '''When an eel grabs your arm,
And it causes great harm,
That's - a moray!'''

song_list = song.split()
song_list_new = []

for w in song_list:
    if w.startswith('m'):
        song_list_new.append(w.title())
    else:
        song_list_new.append(w)

print(' '.join(song_list_new))
