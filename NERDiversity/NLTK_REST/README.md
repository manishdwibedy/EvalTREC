------------------------------------
Starting NLTK server on a virtualenv
------------------------------------


1. Moving to the folder containing my virtual environment
cd ~/EvalTREC/

2. Starting my virtual environment
source bin/activate

3. Starting the NLTK server
nltk-server -v --port 8888

--------------------------------------
Linking Tika to user the NLTK tika-app
--------------------------------------

1. Moving into the NLTK_Rest folder

cd NERDiversity/NLTK_Rest

2. Testing the NLTK integration with Tika

java -Dner.impl.class=org.apache.tika.parser.ner.nltk.NLTKNERecogniser -classpath .:../tika-app-1.13-SNAPSHOT.jar org.apache.tika.cli.TikaCLI --config=tika-config.xml -m  http://www.hawking.org.uk/


------------------------------------
Linking Tikas to use the NLTK server
------------------------------------

1. Moving into the NLTK_Rest folder

cd NERDiversity/NLTK_Rest

2. Starting the tika server integrated with NLTK

java -Dner.impl.class=org.apache.tika.parser.ner.nltk.NLTKNERecogniser -classpath .:../tika-server-1.13-SNAPSHOT.jar org.apache.tika.server.TikaServerCli --config=tika-config.xml


-----------------
Testing with CURL
-----------------

curl -T ./input.txt -H "Content-Disposition: attachment; filename=0A0C0478C62A4BF29F47B5783CBD2CEB12DCF27E5BCD56A4871AFF84FB0C5DD2" -H "Accept: application/json" http://localhost:9998/meta

