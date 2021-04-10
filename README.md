停止コンテナ一括削除
```
docker rm `docker ps -f "status=exited" -q`
```

全コンテナ削除
```
docker rm -f `docker ps -a -q`
```

未使用イメージ一括削除
```
docker rmi `docker images -q`
```

タグ無しイメージ一括削除
```
docker rmi `docker images -f "dangling=true" -q`
```

未使用ボリューム一括削除
```
docker volume rm `docker volume ls -q`
```

未使用ネットワーク一括削除
```
docker network rm `docker network ls -q`
```