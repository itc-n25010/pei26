animals = ['Dog','Cat','Rabbit','Horse','Dolphin']
total = 0
print(f"totalの値は{total}") #totalの初期値を出力する
for animal in animals: #animalsから動物の名前を1つずつ取り出して、繰り返し処理する
    from_D = animal.startswith('D') #動物の名前が'D'で始まるか判定する
    is_long = len(animal) > 5 #動物の名前が5文字より長いか判定する
    if from_D and is_long: #動物の名前が'D'で始まり、5文字より長い場合
        break
    elif not from_D and is_long: #動物の名前が'D'で始まらず、5文字より長い場合
        total += animal.find('b') #文字列内から 'b' の位置を検索し、total に加算する
        print(f"totalの値は{total}") #totalの値を出力する
    else:
        total += len(animal) #それ以外の場合、動物の名前の文字数をtotal に加算する
        print(f"totalの値は{total}") #totalの値を出力する
print(total)

""""
startswithメソッド：文字列が指定した文字列で始まるか判定する
find('b')：文字列内から指定した文字列の最初の位置を検索する

animal      from_D      is_long     total
Dog         True        False       3
Cat         False       False       6
Rabbit      False       True        6 + 2 = 8
Horse       False       False       8 + 5 = 13
Dolphin     True        True        break
"""