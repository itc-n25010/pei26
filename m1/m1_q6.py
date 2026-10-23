# ひらがな1文字を受け取り、表の行番号と列番号を返す関数
# 表に文字がない場合はNoneを返す
def search_kana_idx(kana): 
    idx_1 = 0  # 
    for gyou in hiragana_hyou:  # 表の行を上から順に調べる
        idx_2 = 0  # 
        for ka in gyou: 
            if ka == kana:  # 調べている文字がkanaと同じか確認する
                return (idx_1,idx_2)  # 一致した文字の行番号と列番号を返す
            else:
                idx_2 += 1  # 一致しなければ次の列へ進む
        idx_1 += 1  # 行の確認が終わったら次の行へ進む
    return None  # 表の中に文字がなければNoneを返す


hiragana_hyou = [
    ['あ', 'い', 'う', 'え', 'お'],  
    ['か', 'き', 'く', 'け', 'こ'],  
    ['さ', 'し', 'す', 'せ', 'そ'],  
    ['た', 'ち', 'つ', 'て', 'と'],
    ['な', 'に', 'ぬ', 'ね', 'の'],
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],
    ['ま', 'み', 'む', 'め', 'も'],
    ['や', '゛', 'ゆ', '゜', 'よ'], 
    ['ら', 'り', 'る', 'れ', 'ろ'],
    ['わ', 'っ', 'を', 'ー', 'ん']]

hirabun = input('ひらがなの文を入力してください')  # 暗号化する文を入力する
codes = ''  # 変換結果をためる文字列
for kana in hirabun:  # 文を1文字ずつ取り出す
    idxs = search_kana_idx(kana)  # 文字の行番号と列番号を調べる
    codes += '？' if idxs is None else f'{idxs[0]}{idxs[1]}'
print(codes)  # 暗号化した結果を表示する

ango = input('暗号を入力してください：')  # 復号する暗号を入力する
kanas = ''  # 復号した文字をためる文字列
if len(ango) % 2 == 0:  # 暗号の文字数が偶数か確認する
    for i in range(len(ango) // 2):  # 2文字ずつの組を順に処理する
        index_1 = int(ango[2 * i])  # 組の1文字目を行番号にする
        index_2 = int(ango[2 * i + 1])  # 組の2文字目を列番号にする
        kanas += '？' if index_2 > 4 else hiragana_hyou[index_1][index_2] 
    print(kanas)
else:
    print('暗号の文字数は偶数でなければなりません')


'''
・条件式（三項演算子）について
codes += '？' if idxs is None else f'{idxs[0]}{idxs[1]}'
この処理は、以下のif/else文と同じ処理
if idxs is None: # idxsがNoneなら
    codes += '？' # '？'を連結する
else:
    codes += f'{idxs[0]}{idxs[1]}' 
    # idxs[0]とidxs[1]を文字列にして、続けてcodesに連結する

kanas += '？' if index_2 > 4 else hiragana_hyou[index_1][index_2]
について、
index_2は内側のリストのインデックスで、有効なのは0から4まで。
index_2が5以上だと範囲外になりエラーとなるので、その場合は'？'を連結する
このときelse側のhiragana_hyou[index_1][index_2]は表示されないのでエラーにならない。
(index_1は1桁の数字なので0〜9で、リストの行数10に収まる。そのため確認は不要)

'''