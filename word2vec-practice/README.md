# word2vec-practice
Word2Vecの練習

## Usage
`pipenv`で環境構築ができます。
以下のコマンドを実行してください。
```
$ pipenv install
```

実行には学習済みのWord2Vecモデルが必要です。
[Kyubyong/wordvectors](https://github.com/Kyubyong/wordvectors)から日本語の学習済みWord2Vecをダウンロードして`model`ディレクトリに配置してください。

以下のコマンドで単語のベクトルを用いた演算を行います。
```
$ python run.py
```
