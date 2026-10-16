a=[1,2,3,4]
id_a=id(a) # id()関数はオブジェクトaのidを取得し、id_aに代入する
b=a.copy() # aのcopyを作成し、bに代入する(aとは別のオブジェクトとなる)
id_b=id(b) # bのidを取得し、id_bに代入する

print(id_a) # aのidを出力する
print(id(a)) # aのidを出力する
print(type(id_a)) # id_aの型を出力する
if id_a==id(b): # False: aとbは別のオブジェクトなので、idも異なる
    result= 'A'
elif id(a)==id(b):#False: aとbは別のオブジェクトなので、idも異なる
    result= 'B'
elif id_a==id(a): #True: id_aはid(a)の戻り値が代入される。
    result= 'C'
else: #
    result= 'D'
print(result)

"""
pythonのid()関数は、オブジェクトの一意の識別子を返します。リストaをコピーしてbを作成すると、
bはaとは異なるオブジェクトとなるため、id_aとid_bは異なる値になります。

"""