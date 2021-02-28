import tkinter as tk
import tkinter.messagebox as tkm
import random

# キャンバスサイズ
xcanvas = 1200
ycanvas = 600

# マスの数
ymasu = 19
xmasu = 6

# マスのサイズ
xsize = 200
ysize = 100

# キャラクター画像
# p1
cha1 = "p1.png"
# p2
cha2 = "p2.png"

# 初期位置
p1 = 1
p2 = 1

# 初期座標
p1x = 1
p1y = 1
p2x = 1
p2y = 1

# サイコロ
r = 0

# 順番
junban = 1

# いったん止まるマス
p1juken = 0
p2juken = 0

p1syukatu = 0
p2syukatu = 0

# キー入力
key = ""

# コイン
coin = 0
cadd = 0
coin1 = 1000
coin2 = 1000

# 学力
gaku = 0
gadd = 0
gaku1 = 40
gaku2 = 40

# 就活力
syukatu = 0
sadd = 0
syukatu1 = 50
syukatu2 = 50

# 位置
n = 0

haikei = "skyblue"
mojiiro = "blue"
fontsize = 12
font = "system"
text = "空"

# テキスト位置
t = 1
tx = 1
ty = 1

def text_place():
    global xmasu, t, tx, ty
    # y座標判定
    if t % xmasu != 0:
        ty = (t // xmasu) + 1
    else:
        ty = (t // xmasu)
    # x座標判定
    tx = t - (ty - 1) * xmasu
    # x座標判定 偶数なら逆順
    if ty % 2 == 0:
        tx = (xmasu + 1) - tx


# サイコロを振る
def saikoro():
    global r
    r = random.randint(1, 4)

def saikoro1():
    global r
    r = random.randint(1, 3)


# キー入力管理
def key_down(e):
    global key
    key = e.keycode
def key_up(e):
    global key
    key = ""

# 位置p1から座標p1x,p1yに変換
def p1_place():
    global xmasu, p1, p1x, p1y
    # y座標判定
    if p1 % xmasu != 0:
        p1y = (p1 // xmasu) + 1
    else:
        p1y = (p1 // xmasu)
    # x座標判定
    p1x = p1 - (p1y - 1) * xmasu
    # x座標判定 偶数なら逆順
    if p1y % 2 == 0:
        p1x = (xmasu + 1) - p1x

# 位置p2から座標p2x,p2yに変換
def p2_place():
    global xmasu, p2, p2x, p2y
    # y座標判定
    if p2 % xmasu != 0:
        p2y = (p2 // xmasu) + 1
    else:
        p2y = (p2 // xmasu)
    # x座標判定
    p2x = p2 - (p2y - 1) * xmasu
    # x座標判定 偶数なら逆順
    if p2y % 2 == 0:
        p2x = (xmasu + 1) - p2x

# キャラクター画像表示
def cha_show():
    global p1x, p1y, p2x, p2y
    canvas.coords("MYCHR", p1x * xsize - xsize / 4, p1y * ysize - ysize / 2)
    canvas.coords("MYCHR2", p2x * xsize - xsize / 4 * 3, p2y * ysize - ysize / 2)
    canvas.update()

def junjo1():
    global p2, xmasu, ymasu, junban, p1x, p1y, p2x, p2y
    # 次の順序管理
    if p2 == xmasu * ymasu:
        junban = 1
    elif p1 == xmasu * ymasu:
        tkm.showinfo("ゴール!!", "player1 がゴールしました。")
        junban = 2
    else:
        junban = 2

def junjo2():
    global p1, xmasu, ymasu, junban
    # 次の順序管理
    if p1 == xmasu * ymasu:
        junban = 2
    elif p2 == xmasu * ymasu:
        tkm.showinfo("ゴール!!", "player2 がゴールしました。")
        junban = 1
    else:
        junban = 1

def p1_event():
    global n, p1, syukatu, syukatu1, gaku, gaku1, coin, coin1
    n = p1
    syukatu = syukatu1
    gaku = gaku1
    coin = coin1

    masu_jouhou()

    syukatu1 = syukatu
    gaku1 = gaku
    coin1 = coin

def p2_event():
    global n, p2, syukatu, syukatu2, gaku, gaku2, coin, coin2
    n = p2
    syukatu = syukatu2
    gaku = gaku2
    coin = coin2

    masu_jouhou()

    syukatu2 = syukatu
    gaku2 = gaku
    coin2 = coin

def main_proc():
    global junban, key, p1, p2, xmasu, ymasu, coin, coin1, coin2, n,\
        p1juken, p2juken, gaku, gaku1, gaku2, p1syukatu, p2syukatu, syukatu, syukatu1, syukatu2

    # １を押した場合実行（player1）
    if key == 49:
        # 順序判定
        if junban == 2:
            tkm.showinfo("注意", "player2 の番です。")
            key = ""
        # ゴール判定
        elif p1 == xmasu * ymasu:
            tkm.showinfo("player1", "player1 は既にゴールしています")
            key = ""
        else:
            # 出た目の分だけ進む
            if (72 >> p1 and p1 >= 53) or (113 >> p1 and p1 >= 98):
                saikoro1()
                p1 += r
            else:
                saikoro()
                p1 += r

            if p1 > xmasu * ymasu:
                p1 = xmasu * ymasu

            # 受験分岐
            if p1 >= 53 and p1juken == 0:
                p1 = 53
                p1juken = 1

            # 受験結果分岐
            if p1 >= 72 and p1juken == 1:
                p1 = 72
                p1_place()
                cha_show()
                n = p1
                masu_jouhou()
                p1juken = 2
                if gaku1 >= 70:
                    p1 = 73
                elif gaku1 < 70:
                    p1 = 85

            # 就活分岐
            if p1 >= 98 and p1syukatu == 0:
                p1 = 98
                p1syukatu = 1

            # 就活結果分岐
            if p1 >= 113 and p1syukatu == 1:
                p1 = 113
                p1_place()
                cha_show()
                n = p1
                masu_jouhou()
                p1syukatu = 2
                if syukatu1 >= 80:
                    p1 = 114
                elif 80 >> syukatu1 and syukatu1 >= 70:
                    p1 = 114
                elif 70 >> syukatu1 and syukatu1 >= 60:
                    p1 = 114
                else:
                    p1 = 114

            p1_place()
            cha_show()
            junjo1()
            key = ""

            # ますイベント
            p1_event()

    # 2を押した場合実行（player2）
    elif key == 50:
        # 順序判定
        if junban == 1:
            tkm.showinfo("注意", "player1 の番です。")
            key = ""
        # ゴール判定
        elif p2 == xmasu * ymasu:
            tkm.showinfo("player2", "player2 は既にゴールしています")
            key = ""
        else:
            # 出た目の分だけ進む
            if (72 >> p2 and p2 >= 53) or (113 >> p2 and p2 >= 98):
                saikoro1()
                p2 += r
            else:
                saikoro()
                p2 += r

            if p2 > xmasu * ymasu:
                p2 = xmasu * ymasu

            # 受験分岐
            if p2 >= 53 and p2juken == 0:
                p2 = 53
                p2juken = 1

            # 受験結果分岐
            if p2 >= 72 and p2juken == 0:
                p2 = 72
                p2_place()
                cha_show()
                n = p2
                masu_jouhou()
                p1juken = 1
                if gaku2 >= 70:
                    p2 = 73
                elif gaku2 < 70:
                    p2 = 85

            # 就活分岐
            if p2 >= 98 and p2syukatu == 0:
                p2 = 98
                p2syukatu = 1

            # 就活結果分岐
            if p2 >= 113 and p2syukatu == 1:
                p2 = 113
                p2_place()
                cha_show()
                n = p2
                masu_jouhou()
                p2syukatu = 2
                if syukatu2 >= 80:
                    p2 = 114
                elif 80 >> syukatu2 and syukatu2 >= 70:
                    p2 = 114
                elif 70 >> syukatu2 and syukatu2 >= 60:
                    p2 = 114
                else:
                    p2 = 114

            p2_place()
            cha_show()
            key = ""
            junjo2()
            # ますイベント
            p2_event()

    if p1 == xmasu * ymasu and p2 == xmasu * ymasu:
        tkm.showinfo("全員ゴール！！", "全員ゴールしました。")
        if coin1 > coin2:
            canvas.update()
            message = "所持金は\nplayer1: " + str(coin1) + "コイン\nplayer2: " + str(coin2) + "コイン\nよってplayer1の勝利!!"
            tkm.showinfo("全員ゴールしました", message)
            print("###############\n所持金は\nplayer1:", coin1, "コイン\nplayer2:", coin2,
                  "コイン\nよってplayer1の勝利です\n###############")
        if coin1 < coin2:
            canvas.update()
            message = "所持金は\nplayer1: " + str(coin1) + "コイン\nplayer2: " + str(coin2) + "コイン\nよってplayer2の勝利!!"
            tkm.showinfo("全員ゴールしました", message)
            print("###############\n所持金は\nplayer1: ", coin1, "コイン\nplayer2: ", coin2,
                  "コイン\nよってplayer2の勝利です\n###############")
        if coin1 == coin2:
            canvas.update()
            message = "所持金は\nplayer1: " + str(coin1) + "コイン\nplayer2: " + str(coin2) + "コイン\nよって引き分けです。"
            tkm.showinfo("全員ゴールしました", message)
            print("###############\n所持金は\nplayer1:", coin1, "コイン\nplayer2:", coin2,
                  "コイン\nよって引き分けです\n###############")

    else:
        root.after(100, main_proc)

def masu_jouhou():
    global n, coin, cadd, gaku, gadd, syukatu, sadd
    if n == 2:
        cadd = 1000
        coin += cadd
        canvas.update()
        message = "お七夜\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 3:
        cadd = 1000
        coin += cadd
        canvas.update()
        message = "1歳の誕生日\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 4:
        cadd = 3000
        coin += cadd
        canvas.update()
        message = "3歳　七五三\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 5:
        cadd = 4000
        coin += cadd
        canvas.update()
        message = "幼稚園　入園祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 6:
        cadd = 5000
        coin += cadd
        canvas.update()
        message = "5歳　七五三\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 7:
        cadd = -2000
        coin += cadd
        canvas.update()
        message = "初の夏祭り\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 8:
        cadd = 5000
        coin += cadd
        canvas.update()
        message = "お年玉\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 9:
        cadd = 5000
        coin += cadd
        canvas.update()
        message = "小学校入学祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 10:
        cadd = -3000
        coin += cadd
        canvas.update()
        message = "友達と遊ぶ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 11:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "ゲームソフトを買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 12:
        cadd = -3000
        coin += cadd
        canvas.update()
        message = "友達と遊ぶ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 13:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "十歳の祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 14:
        cadd = 2000
        coin += cadd
        canvas.update()
        message = "初めてのお使い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 15:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "ゲームソフトを買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 16:
        cadd = 3000
        coin += cadd
        canvas.update()
        message = "3教科テストで満点\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)
                     
    elif n == 17:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "全国模試でTop100以内\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 18:
        cadd = -1000
        coin += cadd
        canvas.update()
        message = "少年サッカーに加入\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 19:
        cadd = -30000
        coin += cadd
        canvas.update()
        message = "修学旅行に行く\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 20:
        cadd = 20000
        coin += cadd
        canvas.update()
        message = "小学校卒業祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 21:
        cadd = -1000
        coin += cadd
        canvas.update()
        message = "中学校入学祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 22:
        cadd = 2000
        coin -= cadd
        canvas.update()
        message = "将棋部に加入\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 23:
        cadd = -1000
        coin += cadd
        canvas.update()
        message = " 卓球部に加入\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 24:
        cadd = 2000
        coin += cadd
        canvas.update()
        message = "テストで2教科満点 \n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 25:
        cadd = -4000
        coin += cadd
        canvas.update()
        message = " 友達と遊ぶ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 26:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "定期テストでTOP10に入る\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 27:
        cadd = 3000
        coin += cadd
        canvas.update()
        message = "大会で3位！\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 28:
        cadd = -4000
        coin += cadd
        canvas.update()
        message = "参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 29:
        cadd = -30000
        coin += cadd
        canvas.update()
        message = "修学旅行に行く\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 30:
        cadd = 20000
        coin += cadd
        canvas.update()
        message = "中学最後の定期テストでTOP50\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 31:
        cadd = 20000
        coin += cadd
        canvas.update()
        message = "中学最後の定期テストでTOP50\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 32:
        cadd = 50000
        coin += cadd
        canvas.update()
        message = "中学校卒業祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 33:
        cadd = 50000
        coin += cadd
        canvas.update()
        message = "高校第一志望に合格\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 34:
        cadd = -3000
        coin += cadd
        canvas.update()
        message = "文化祭を楽しむ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)
                     
    elif n == 35:
        cadd = -4000
        coin += cadd
        canvas.update()
        message = " 友達と遊ぶ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 36:
        cadd = -5000
        coin += cadd
        canvas.update()
        message = "体育祭を満喫する \n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 37:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "定期テストでworst100 \n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 38:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "定期テストでtop100 \n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 39:
        cadd = -20000
        coin += cadd
        canvas.update()
        message = "家族旅行に行く\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 40:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "誕生日だ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 41:
        cadd = 15000
        coin += cadd
        canvas.update()
        message = "クリスマスプレゼントを貰う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 42:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "クリスマスデートをする\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 43:
        cadd = 2000
        coin += cadd
        canvas.update()
        message = "お正月お年玉を貰う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 44:
        cadd = -15000
        coin += cadd
        canvas.update()
        message = "受験に備えて参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 45:
        cadd = -4000
        coin += cadd
        canvas.update()
        message = "カラオケに行く\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 46:
        cadd = 5000
        coin -= cadd
        canvas.update()
        message = "友達と遊ぶ\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 47:
        cadd = -1000
        coin += cadd
        canvas.update()
        message = "タピオカジュースを買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 48:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "定期テストでtop100\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 49:
        cadd = -15000
        coin += cadd
        canvas.update()
        message = "英会話スクールに通う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 50:
        cadd = -100000
        coin += cadd
        canvas.update()
        message = "1週間の短期留学する\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 51:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "体育祭で入賞する\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 52:
        cadd = -15000
        coin += cadd
        canvas.update()
        message = "塾に入塾する\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 53:
        gadd = 40
        gaku += gadd
        canvas.update()
        message = "受験期に突入/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 54:
        gadd = 20
        gaku += gadd
        canvas.update()
        message = "一日8時間勉強する/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 55:
        gadd = 20
        gaku += gadd
        canvas.update()
        message = "苦手を集中的に解く/\n " + str(gaku) +"学力が上がった。\n学力は"  + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 56:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "ゲームをする/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 57:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "勉強するやる気がでなかった/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 58:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "問題集をこなす/\n " + str(gaku) + "学力が上がった。\n学力は"+ str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 59:
        gadd = 20
        gaku += gadd
        canvas.update()
        message = "志望校の過去問を解く/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 60:
        gadd = 20
        gaku += gadd
        canvas.update()
        message = "赤本を解く/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 61:
        gadd = 10
        gaku += gadd
        canvas.update()
        message = "参考書を読む/\n " + str(gaku) +"学力が上がった。\n学力は"  + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 62:
        gadd = -10
        gaku += gadd
        canvas.update()
        message = "ゲームをする/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 63:
        gadd = 10
        gaku += gadd
        canvas.update()
        message = "問題集をする/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 64:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "勉強するやる気がでなかった/\n " + str(gaku) +"学力が上がった。\n学力は"  + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 65:
        gadd = 10
        gaku += gadd
        canvas.update()
        message = "参考書を読む/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("p1所持額", message)

    elif n == 66:
        gadd = -10
        gaku += gadd
        canvas.update()
        message = "一日中寝ていた/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 67:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "勉強するやる気がでなかった/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 68:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "センター過去問を解く/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 69:
        gadd = -10
        gaku += gadd
        canvas.update()
        message = "勉強するやる気がでなかった/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 70:
        gadd = -10
        gaku += gadd
        canvas.update()
        message = "友達と遊んだ/\n " + str(gaku) + "学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 71:
        gadd = -20
        gaku += gadd
        canvas.update()
        message = "一日中動画を見ていた/\n " + str(gaku) +"学力が上がった。\n学力は" + str(gadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 72:
        cadd = 20000
        coin += cadd
        canvas.update()
        message = "受験終了！！\n学力70以上で志望校合格。学力70以下で浪人ルートへ。\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 73:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "浪人期間に突入！！\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 74:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "問題集を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 75:
        cadd = -5000
        coin += cadd
        canvas.update()
        message = "参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 76:
        cadd = -3000
        coin += cadd
        canvas.update()
        message = "問題集を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 77:
        cadd = -7000
        coin += cadd
        canvas.update()
        message = "試験を申し込む\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 78:
        cadd = -2000
        coin += cadd
        canvas.update()
        message = "問題集を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 79:
        cadd = -2000
        coin += cadd
        canvas.update()
        message = "問題集を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 80:
        cadd = -5000
        coin += cadd
        canvas.update()
        message = "参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)
    elif n == 81:
        cadd = -5000
        coin += cadd
        canvas.update()
        message = "問題集を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 82:
        cadd = -7000
        coin += cadd
        canvas.update()
        message = "試験を申し込む\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 83:
        cadd = -4000
        coin += cadd
        canvas.update()
        message = "参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 84:
        cadd = -4000
        coin += cadd
        canvas.update()
        message = "過去問集を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 85:
        cadd = -20000
        coin += cadd
        canvas.update()
        message = "大学入学準備をする\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 86:
        cadd = 50000
        coin += cadd
        canvas.update()
        message = "大学入学祝い\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 87:
        cadd = -20000
        coin += cadd
        canvas.update()
        message = "教科書の購入する\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 88:
        cadd = 8000
        coin += cadd
        canvas.update()
        message = "バイトする\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 89:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "学祭を満喫する\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 90:
        cadd = -5000
        coin += cadd
        canvas.update()
        message = "デートをする\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 91:
        cadd = 10000
        coin += cadd
        canvas.update()
        message = "帰省し、お金をもらう\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 92:
        cadd = 5000
        coin += cadd
        canvas.update()
        message = "バイトする\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 93:
        cadd = -2000
        coin += cadd
        canvas.update()
        message = "参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 94:
        cadd = -2000
        coin += cadd
        canvas.update()
        message = "参考書を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 95:
        cadd = -8000
        coin += cadd
        canvas.update()
        message = "服を買う\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 96:
        cadd = -10000
        coin += cadd
        canvas.update()
        message = "サークル合宿に参加\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 97:
        cadd = 20000
        coin += cadd
        canvas.update()
        message = "帰省し、お金をもらう\n " + str(coin) + "コインを入手した。\n現在の所持額は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 98:
        sadd = 40
        syukatu += sadd
        canvas.update()
        message = "就活に突入\n " + str(syukatu) + "就活力を上げよ！。\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 99:
        sadd = 20
        syukatu += sadd
        canvas.update()
        message = "企業調べを行う！！\n " + str(syukatu) + "就活力を身に付けた。\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 100:
        sadd = 10
        syukatu += sadd
        canvas.update()
        message = "SPIを解く！！\n " + str(syukatu) +"就活力を身に付けた。\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 101:
        sadd = -10
        syukatu += sadd
        canvas.update()
        message = "やる気が出ない\n " + str(coin) +"就活力を身に付けた。\n就活力は"  + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 102:
        sadd = -10
        syukatu += sadd
        canvas.update()
        message = "遊んでしまった\n " + str(syukatu) + "就活力を身に付けた。\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 103:
        sadd = -10
        syukatu += sadd
        canvas.update()
        message = "動画を一日中見る\n " + str(syukatu) +"就活力を身に付けた。\n就活力は"  + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 104:
        sadd = 20
        syukatu += sadd
        canvas.update()
        message = "SPIを解く\n " + str(syukatu) + "就活力を身に付けた。\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 105:
        sadd = 20
        syukatu += sadd
        canvas.update()
        message = "インターンシップに参加する\n " + str(syukatu) +"就活力を身に付けた\n就活力は。" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 106:
        sadd = 20
        syukatu += sadd
        canvas.update()
        message = "就活の情報交換を行う\n " + str(syukatu) +"就活力を身に付けた\n就活力は。"  + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 107:
        sadd = -10
        syukatu += sadd
        canvas.update()
        message = "二日酔い\n " + str(syukatu) + "就活力を身に付けた\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 108:
        sadd = 10
        syukatu += sadd
        canvas.update()
        message = "ESを書く\n " + str(syukatu) +"就活力を身に付けた\n就活力は"  + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 109:
        sadd = 10
        syukatu += sadd
        canvas.update()
        message = "面接対策をする\n " + str(syukatu) +"就活力を身に付けた\n就活力は"  + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 110:
        sadd = -10
        syukatu += sadd
        canvas.update()
        message = "やる気がない\n " + str(syukatu) +"就活力を身に付けた\n就活力は"+ str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 111:
        sadd = -10
        syukatu += sadd
        canvas.update()
        message = "一日中寝てしまった\n " + str(syukatu) +"就活力を身に付けた\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 112:
        sadd = 10
        syukatu += sadd
        canvas.update()
        message = "企業調べを行う！！\n " + str(syukatu) + "就活力を身に付けた\n就活力は" + str(sadd) + "です。"
        tkm.showinfo("所持額", message)

    elif n == 113:
        cadd = -20000
        coin += cadd
        canvas.update()
        message = "スーツを購入する\n " + str(coin) +"就活力を身に付けた\n就活力は" + str(cadd) + "です。"
        tkm.showinfo("所持額", message)

# 1.キャンバスの生成
root = tk.Tk()
size = str(xcanvas + 20) + "x" + str(ycanvas + 20)
root.geometry(size)
root.title("人生ゲーム")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tk.Canvas(width=xcanvas + 20, height=ycanvas + 20, bg="white")
canvas.place(x=0, y=0, width=xcanvas + 20, height=ycanvas + 20)

# 2.キャンバスにスクロールバーを配置
bar_y = tk.Scrollbar(canvas, orient=tk.VERTICAL)
bar_x = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
bar_y.pack(side=tk.RIGHT, fill=tk.Y)
bar_x.pack(side=tk.BOTTOM, fill=tk.X)
bar_y.config(command=canvas.yview)
bar_x.config(command=canvas.xview)
canvas.config(yscrollcommand=bar_y.set, xscrollcommand=bar_x.set)
# Canvasのスクロール範囲を設定
canvas.config(scrollregion=(0, 0, xsize * xmasu, ysize * ymasu))

# 3.マスを生成
for y in range(ymasu):
    for x in range(xmasu):
        canvas.create_rectangle(x * xsize, y * ysize, x * xsize + xsize, y * ysize + ysize, fill="skyblue")

###text###
t = 1
text = "スタート"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 2
text = "お七夜"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 3
text = "1歳の誕生日"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 4
text = "3歳七五三"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 5
text = "幼稚園入園祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 6
text = "5歳七五三"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 7
text = "初の夏祭り"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 8
text = "お年玉"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 9
text = "小学校入学祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 10
text = "友達と遊ぶ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 11
text = "ゲームソフトを買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 12
text = "友達と遊ぶ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 13
text = "十歳の祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 14
text = "初めてのお使い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 15
text = "ゲームソフトを買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 16
text = "3教科テストで満点"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 17
text = "全国模試でTop100以内"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)


t = 18
text = "少年サッカーに加入"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 19
text = "修学旅行に行く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 20
text = "小学校卒業祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 21
text = "中学校入学祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 22
text = "将棋部に加入"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 23
text = "卓球部に加入"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 24
text = "テストで2教科満点"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 25
text = "友達と遊ぶ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 26
text = "定期テストでTOP10"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 27
text = "大会で3位"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 28
text = "参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 29
text = "修学旅行に行く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 30
text = "定期テストでTOP50"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 31
text = "クラスで卒業打ち上げ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 32
text = "中学校卒業祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 33
text = "高校第一志望に合格"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 34
text = "文化祭を楽しむ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 35
text = "友達と遊ぶ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 36
text = "体育祭を満喫する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 37
text = "定期テストでworst100"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 38
text = "定期テストでtop100"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 39
text = "家族旅行に行く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 40
text = "誕生日だ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 41
text = "クリスマス"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 42
text = "クリスマスデートをする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 43
text = "お正月にお年玉を貰う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 44
text = "受験に備え参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 45
text = "カラオケに行く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 46
text = "友達と遊ぶ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 47
text = "タピオカジュースを買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 48
text = "定期テストでtop100"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 49
text = "英会話スクールに通う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 50
text = "1週間の短期留学する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 51
text = "体育祭で入賞する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 52
text = "塾に入塾する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 53
text = "受験期に突入"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 54
text = "一日8時間勉強する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 55
text = "苦手を集中的に解く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 56
text = "ゲームをする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 57
text = "勉強するやる気が無い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 58
text = "問題集をこなす"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 59
text = "志望校の過去問を解く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 60
text = "赤本を解く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 61
text = "参考書を読む"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 62
text = "ゲームをする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 63
text = "問題集をする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 64
text = "勉強するやる気が無い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 65
text = "参考書を読む"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 66
text = "一日中寝ていた"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 67
text = "勉強するやる気が無い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 68
text = "センター過去問を解く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 69
text = "勉強するやる気が無い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 70
text = "友達と遊んだ"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 71
text = "一日中動画を見ていた"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 72
text = "受験終了！"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 73
text = "浪人期間に突入"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 74
text = "問題集を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 75
text = "参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 76
text = "問題集を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 77
text = "試験を申し込む"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 78
text = "問題集を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 79
text = "問題集を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 80
text = "参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 81
text = "問題集を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 82
text = "試験を申し込む"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 83
text = "参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 84
text = "過去問集を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 85
text = "大学入学準備をする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 86
text = "大学入学祝い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 87
text = "教科書の購入する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 88
text = "バイトする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 89
text = "学祭を満喫する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 90
text = "デートをする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 91
text = "帰省しお金をもらう"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 92
text = "バイトする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 93
text = "参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 94
text = "参考書を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 95
text = "服を買う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 96
text = "サークル合宿に参加"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 97
text = "帰省しお金をもらう"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 98
text = "就活に突入"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 99
text = "企業調べを行う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 100
text = "SPIを解く！"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 101
text = "やる気が出ない"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 102
text = "遊んでしまった"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 103
text = "動画を一日中見る"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 104
text = "SPIを解く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 105
text = "インターンシップに参加"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 106
text = "就活の情報交換を行う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 107
text = "面接対策をする"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 108
text = "飲み会でストレス発散"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 109
text = "二日酔い"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 110
text = "ESを書く"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 111
text = "やる気がない"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 112
text = "企業調べを行う"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 113
text = "スーツを購入する"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)

t = 114
text = "ゴール！"
text_place()
canvas.create_text(tx * xsize - 100, ty * ysize - 90, text=text, font=(font, fontsize, "bold"), angle=0)
###text end###

# 4.キャラクター画像の読み込みと表示
img1 = tk.PhotoImage(file=cha1)
img2 = tk.PhotoImage(file=cha2)
canvas.create_image(p1x * xsize - xsize / 4, p1y * ysize - ysize / 2, image=img1, tag="MYCHR")
canvas.create_image(p2x * xsize - xsize / 4 * 3, p2y * ysize - ysize / 2, image=img2, tag="MYCHR2")

main_proc()
root.mainloop()

