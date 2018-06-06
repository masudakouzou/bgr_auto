## bgr大喜利ルームの部屋管理ツール

# 使い方

① Python導入  
  
[公式](https://www.python.org/)からPython3.6.5以上をダウンロードし、インストールする  

② selenium導入
  
コマンドプロンプトを開き
```
pip install selenium
```
としてseleniumをインストールする
  
③ Webdriver導入
[Firefox](https://github.com/mozilla/geckodriver/releases)から  
自分のOSに合ったgeckodriverをダウンロードし、Python36-32フォルダがある場所へ  
geckodriver.exeを移動させる
(  
C:\Users\（ユーザー名）\AppData\Local\Programs\Python\Python36-32\  
がデフォルト  
) 

④ 動かす
このツール自体を右上のDownload Zipからダウンロードして、適当なフォルダに移動させる  

コマンドプロンプトで先ほどのフォルダへ移動し

```
python main.py
```

とすれば良い 
画像やログ(csv)などをダウンロードしてくれる



### 補足 コマンドプロンプトでのフォルダ間移動について  
```
C:\Users\(ユーザー名)>
```

のようになっていると思うのでそこから  

```
C:\Users\(ユーザー名)>cd Desktop
```

のようにcd コマンドでその直下のフォルダに移動できる（cd:カレントディレクトリ） 

ツールをDocuments以下に解凍・保存した場合は

```
C:\Users\(ユーザー名)>cd Documents

C:\Users\(ユーザー名)\Documents>python main.py
```

とすればできる