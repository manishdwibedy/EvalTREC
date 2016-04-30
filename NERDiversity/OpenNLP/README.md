
-----------------------
Starting as TIKA server
-----------------------

PROJECT_HOME = /Users/manishdwibedy/PycharmProjects/EvalTREC

cd PROJECT_HOME/NERDiversity/OpenNLP

java -classpath ./models/:../tika-server-1.12.jar org.apache.tika.server.TikaServerCli --config=./tika-config.xml



------------------------
TESTING WITH A HTML FILE
------------------------

File Location - /Users/manishdwibedy/PycharmProjects/MIME/Data/html/Training/0A0C0478C62A4BF29F47B5783CBD2CEB12DCF27E5BCD56A4871AFF84FB0C5DD2


Curl request to the server : 

curl -T /Users/manishdwibedy/PycharmProjects/MIME/Data/html/Training/0A0C0478C62A4BF29F47B5783CBD2CEB12DCF27E5BCD56A4871AFF84FB0C5DD2 -H "Content-Disposition: attachment; filename=0A0C0478C62A4BF29F47B5783CBD2CEB12DCF27E5BCD56A4871AFF84FB0C5DD2" -H "Accept: application/json" http://localhost:9998/meta

