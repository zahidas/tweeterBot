# Twitter-Bot Free Ver.

このフォルダを Heroku にアップロードすることで、自動的にツイートすることができます。

# DEMO

画像は Full Ver. のものになります。Free Ver. では、限定的な TwitterUtil.post() のみ使用可能です。

![Image 1](./introduction/twitter-bot-01.png "Introduction")

# Features

Full Ver. の TwitterUtil クラスをインスタンス化することで自動ツイート・自動いいねをすることができます。

![Image 2](./introduction/twitter-bot-02.png "TwitterUtil.post()")

![Image 3](./introduction/twitter-bot-03.png "TwitterUtil.like()")

BlockingScheduler を使用することで、指定した時間（ ±second も可能）に実行できる。また、実行時間のインターバルも設定可能です。

![Image 4](./introduction/twitter-bot-04.png "BlockingScheduler")

pyinstaller でサンプルフォルダを作成する実行ファイル・APIキーとアクセストークンを暗号化する実行ファイルを作成しました。Windows と Linux に対応しております。

![Image 5](./introduction/twitter-bot-05.png "exefile")

# Requirement

* Python 
* APScheduler
* bottle
* datetime
* numpy
* pycryptodome
* python-twitter

# Preparation

Twitter-bot を使用する前に 3 つの作業を行ってください。まず、[Git](https://git-scm.com/) をインストールしてください。次に、[Twitter app](https://apps.twitter.com/) から API キーとアクセストークンを取得してください。最後に、[Heroku](https://dashboard.heroku.com/) にアクセスして、アカウントを作成してください。

[Twitter app](https://apps.twitter.com/) から取得した API キーとアクセストークンを config フォルダ内の API_Key, Access_Token 内に貼り付けてください。

Full Ver. の場合は、encrypt フォルダの create-api-token または create-api-token.exe を実行して API キーとアクセストークンを暗号化してください。暗号化したファイルは自動的に作成されます。

# Usage

以下のコマンドで、Heroku に APP を作成して、フォルダをアップロードしましょう。

変更をアップロードする場合は、update file を実行すると楽です。

```bash
cd Twitter-bot-Full

# First deployment
heroku login
$appname = Twitter-bot-001
heroku create $appname

git add .
git commit -m "new commit"
git remote add heroku https://git.heroku.com/$appname.git
git push heroku master

# Deploying the second and subsequent times
heroku login
update.bat   # windows
bash update.sh    # linux
```

# Installation

ソースコードを改善したい場合は、以下のコマンドでライブラリをインストールしてください。


```bash
# pip
pip install -y APScheduler, bottle, datetime, numpy, pycryptodome, python-twitter

or

# conda
conda create -y twitter
conda activate twitter
conda install -y APScheduler, bottle, datetime, numpy, pycryptodome, python-twitter
conda deactivate
```

# Note

* config フォルダ内の API_Key, Access_Token のホワイトスペースを消さないでください。読み込み時にエラーを吐きます。

# Author

* [Github DriCro6663](https://github.com/DriCro6663)
* [Twitter Dri_Cro_6663](https://twitter.com/Dri_Cro_6663)
* [PieceX DriCro6663]()
* [ドリクロの備忘録](https://dri-cro-6663.jp/)
* dri.cro.6663@gmail.com

# License

[LICENSE](./LISENCE) ファイルをご確認してください。