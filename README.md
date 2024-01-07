# AUTO Twitch Downloader
設定ファイルで指定したチャンネルの配信を自動でダウンロードするツールです。

## 使い方

### TwitchDownloaderCLIのインストール
[TwitchDownloaderCLI](https://github.com/lay295/TwitchDownloader/tree/master?tab=readme-ov-file#cli)に従って，TwitchDownloaderCLIをインストールしてください．


### settings.iniの設定
[./settings.example.ini](./settings.example.ini)をダウンロードし，settings.iniにリネームしてください．

settings.iniの設定は以下の通りです．

[Settings]
- Quality: ダウンロードする配信の画質を指定します．eg. 1080p60．指定した画質が配信されていない場合は最高画質でダウンロードします．
- StreamerIDs: ダウンロードする配信者のIDを指定します．
  - IDはTwitchのURLに含まれるユーザーネームとは異なるので注意．
  - ユーザー名からIDを取得するには，[Convert Twitch Username to Channel ID](https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/)を利用してください．
- OutputDirectory: ダウンロードしたファイルを保存するディレクトリを指定します．
- DownloaderPath: TwitchDownloaderCLI.exeのパスを指定します．

[Twitch]
- AppId: TwitchのAPIを利用するためのクライアントIDを指定します．
- AppSecret: TwitchのAPIを利用するためのアクセストークンを指定します．

### 実行ファイルのダウンロード
[Release](https://github.com/nntto/auto_twitch_downloader/releases)から，最新の実行ファイルをダウンロードしてください．
ダウンロードした実行ファイルは，settings.iniと同じディレクトリに配置してください．

### 実行
ダウンロードした実行ファイルを実行すると，OutputDirectoryにダウンロードしたファイルが保存されます．