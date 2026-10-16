num = 12 #素因数分解する数を12に設定
list_s = [] 
s = 2 
while s <= num: #s が num 以下である間、繰り返す
    if num % s == 0: #num が s で割り切れるか判定
        num //= s #num を s で割った整数値で更新
        print(num) #割った後の num を出力
        if s not in list_s: #s がリストにまだ存在しないか確認
            list_s.append(s) #s をリストに追加
    else:
        s += 1 #割り切れなかった場合、調べる数を1増やす
print(list_s)

"""
計算欄
１回目：num = 12 list_s = [2] s = 2
２回目：num = 6 list_s = [2] s = 2 
３回目：num = 3 list_s = [2] s = 3
４回目：num = 1 list_s = [2, 3] s = 3
while 3 <= 1 は False なので終了
"""