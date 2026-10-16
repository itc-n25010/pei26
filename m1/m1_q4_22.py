a = 17
b =5
dm = divmod(a, b) #aをbで割った商と余りをタプルで返す
p = pow(dm[0], dm[1]) #dmの商をdmの余り乗した結果をpに代入  
all_num = [a, b, dm[0], dm[1], p] #a,b,商,余り,pをリストにまとめる
min_all = min(all_num) #リストの中で最小値をmin_allに代入
max_all = max(all_num) #リストの中で最大値をmax_allに代入
sum_all = sum(all_num) #リストの中の合計をsum_allに代入
print(all_num) #リストの中身を出力
print(f'{min_all}, {max_all}, {sum_all}') #f文字列を使ってmin_all,max_all,sum_allの値を出力

"""
divmod関数：商と余りをタプルで返す
pow関数：累乗を計算する
max関数：最大値を返す
min関数：最小値を返す
sum関数：合計を返す

"""