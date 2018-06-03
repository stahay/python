■演算子
+ - * / ... 四則演算
** ... n乗（a**b はaのb乗）
// ... 切り捨て除算
% ... 除算の余り


■ビット演算子
こんなのがあるらしい
~a            # ビット反転
a & b         # AND:論理積(aもbも1のビットが1)
a | b         # OR:論理和(aまたはbが1のビットが1)
a ^ b         # XOR:排他的論理和(aまたはbが1のビットが1)
a << b        # b ビット左シフト
a >> b        # b ビット右シフト


■代入演算子
value += 5 ... value = value + 5 と同じ
value -= 5 ... value = value - 5 と同じ
value *= 5 ... value = value * 5 と同じ
value /= 5 ... value = value / 5 と同じ
value **= 2 ... value = value ** 2 と同じ
value //= 2 ... value = value // 2 と同じ
value %= 2 ... value = value % 2 と同じ


■その他
a &= b        # a = a & b に同じ
a |= b        # a = a | b に同じ
a ^= b        # a = a ^ b に同じ
a <<= b       # a = a << b に同じ
a >>= b       # a = a >> b に同じ


■コメントアウト
# ... 1行コメント
""" ～ """ ... 複数行コメント 複数行文字列 。コメントアウトに使えるが専用ではない


■文字列
ただの文字列でも配列みたいな扱いができる
# その1
str = "Apples"
str[0]            # 'A'
# その2
"test"[2]        # 's'
# その3
ex = "Apples"
ex[:3]            # 'App'
ex[1:4]            # 'ppl'
ex[3:]            # 'les'


■比較演算子
a == b           # a が b と等しい
a != b           # a が b と異なる
a < b            # a が b よりも小さい
a > b            # a が b よりも大きい
a <= b           # a が b 以下である
a >= b           # a が b 以上である
a <> b           # a が b と異なる
a is b           # a が b と等しい
a is not b       # a が b と異なる
a in b           # a が b に含まれる
a not in b       # a が b に含まれない


■分岐
if 条件 :
    処理
elif 条件:
    処理
else:
    処理


■関数
def 関数名(引数, ...):
    処理
呼び出しは 関数名(引数) のようにする

def ex(value):
    print(value)

ex("テスト")    # 「テスト」が表示される



■モジュール
呼び出しの文法がいろいろある
# randomを読み込み
import random
# random.randintを読み込み
import random.randint
# random.randintを読み込み
from random import randint
# こういう書き方もできるらしい
from random import *


■リスト（配列）
#リストの値を操作する場合はindexで指定
list = ["a", "b", "c"]
追加
list = [1, 2, 3, 4]
list.append(5)        # 最後に要素が追加されて list = [1, 2, 3, 4, 5] になる

list = ["a", "c", "d"]
list.insert(1, "b")    # 2番目に値が追加されて list = ["a", "b", "c", "d"] になる


切り出し
list = [5, 6, 7, 8, 9]
slice = list[:2]        # slice = [5, 6]
slice = list[2:4]      # slice = [7, 8]
slice = list[1:]        # slice = [6, 7, 8, 9]


削除
# その1: 要素を指定
list = ["a", "b", "c", "d"]
list.remove("c")        # list = ["a", "b", "d"]

# その2: インデックスを指定
list = ["a", "b", "c", "d"]
list.pop(2)               # list = ["a", "b", "d"]

# その3: 末尾の要素
list = ["a", "b", "c", "d"]
list.pop()               # list = ["a", "b", "c"]

# 並び替え
apples = [310, 322, 292, 288, 300, 346]
print(sorted(apples))               # 昇順  [288, 292, 300, 310, 322, 346]
print(sorted(apples, reverse=True)) # 降順　[346, 322, 310, 300, 292, 288]



■2次元リスト
#2次元配列を作成する
team_c = ["勇者", "戦士", "魔法使い"]
team_d = ["盗賊", "忍者", "商人"]
team_e = ["スライム", "ドラゴン", "魔王"]

teams = [team_c, team_d, team_e]
print(teams)


#2次元配列を呼び出す
print(teams[0])
print(teams[0][0])
print(teams[0][1])
print(teams[0][2])


#2次元配列の要素を更新する
teams[0][0] = "魔導士"

#2次元配列の長さ
teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
print(len(teams))

#2次元配列の要素を追加する
teams.append(["メタルモンスター", "シルバーモンスター", "ブラックモンスター"])
teams[0].append("レッドドラゴン")

#2次元配列の要素を削除する
del teams[1]
del teams[0][1]

#for in でリストを作成
numbers = [1 for i in range(10)]
print(numbers)

#2次元配列をforで作成する
numbers2 = [[1 for i in range(3)] for j in range(4)]
print(numbers2)



■辞書
# key: value の形式。
# indexではなく、keyで辞書の値を操作する

states = {42: "Washington", 50: "Hawaii", 1: "Delaware"}
print(states[42])    # Washington
print(states[50])    # Hawaii
print(states[1])     # Delaware

# 削除
del states[42]    # 42: "Washington" を削除



■タプル
ほぼリストと同じだが内容更新不可
tuple1 = (1, "a", true)



■繰り返し
list = [1, 2, 3, 4, 5]
for elements in list:
    print(elements)

tuple = (1, 2, 3, 4, 5)
for elements in tuple:
    print(elements)


counter = 0
while counter < 5:
    print("something")
    counter += 1


■try～except
ex = input("Guess what my favorite integer is. :")

try:
    if int(ex) == 7:
        print("That is correct, 7 is my favorite integer.")
    else:
        print("That is not my favorite integer.")
except:
    print("Please run the program again and enter an integer.")


■標準入力
# 標準入力から1行読み込む
line = input()

# 標準入力から2行読み込む
line = input()
line2 = input()


# 標準入力とループ処理
# sys.stdin.readlines関数	ファイルを全て読み込み、1行毎に処理
#.rstrip()
# データの行末の改行を削除する。改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除しておく。
# list1にいれることでリスト数分ループする等が可能
import sys
array = []
for line in sys.stdin.readlines():
    array.append(line.rstrip())

