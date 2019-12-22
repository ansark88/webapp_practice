# TODO

* postgresのイメージを作る
* pipenvでPythonのサーバーサイド環境を作る（ローカルでよい）
* Python側からSQLAlchemyを使ってDBと疎通できるようになる
* Dockerイメージを作ってPython側をそちらに移す
* Vueを使ってフロント側の実装を始める

# Python側環境構築

```
$ pip3 install pipenv
$ pipenv sync
```

# psqlからのDB接続

`psql -h localhost -p 15432 -U test -d postgres`ßß