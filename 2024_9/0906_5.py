# たてH cm よこ W cm の長方形を描くプログラムを作成して下さい。

# 1 cm × 1cm の長方形を '#'で表します。

# Input
# 入力は複数のデータセットから構成されています。各データセットの形式は以下のとおりです：

# H W

# H, W がともに 0 のとき、入力の終わりとします。

while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    for x in range(H):
        print("#"*W)
        
    
    
