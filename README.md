# bgr大喜利ルームの部屋管理ツール

## 使い方


1. Python導入  
  
[公式](https://www.python.org/)からPython3.6.5以上をダウンロードし、インストールする  

<br>
<br>

2. selenium導入
  
コマンドプロンプトを開き
```
pip install selenium
```
としてseleniumをインストールする
  
<br>
<br>


3. Webdriver導入  
  
[Firefox](https://github.com/mozilla/geckodriver/releases)から  
自分のOSに合ったgeckodriverをダウンロードし、Python36-32フォルダがある場所へ  
geckodriver.exeを移動させる

C:\Users\（ユーザー名）\AppData\Local\Programs\Python\Python36-32\  
がデフォルト  
  
<br>
<br>

4. 動かす  

このページ右上の  
clone or download => Download Zip  
からダウンロードして、適当なフォルダに解凍・移動させる。コマンドプロンプトで解凍したフォルダへ移動し

```
python main.py
```

とすれば良い  
画像やログ(csv)などをダウンロードしてくれる
  
<br>
<br>
<br>
  

## 設定について  
**bgrsrc**フォルダの中にある**config.py**内の数値を変更してください  
いじる必要があるのは  

```
ANSWER_TIME: 回答時間  
VOTE_TIME_BASE: 回答時間のベース値  
VOTE_TIME_COEFFICIENT: 回答時間の係数
```

だと思います  
部屋名や自分の名前も変更できます  

<br>
<br>
<br>

  
### 補足 コマンドプロンプトでのフォルダ間移動について  
  
```
C:\Users\(ユーザー名)>
```

のようになっていると思うのでそこから  

```
C:\Users\(ユーザー名)>cd Desktop
```

のようにcd コマンドでその直下のフォルダに移動できます（cd:カレントディレクトリ)   
<br>
ツールをDocuments以下に解凍・保存した場合は

```
C:\Users\(ユーザー名)>cd Documents

C:\Users\(ユーザー名)\Documents>python main.py
```

とすれば動きます  
  
## [動画での使い方説明はこちら](https://drive.google.com/open?id=1ZOGK6FnQBi_bLlsgZwTa4PfUD0OtG6D7)