# Exercise 2

- A Git csak egy apró mutató fájlt kapott, míg a MinIO egy nagyobb fájlt. A DVC lényege, hogy a kicsi fájlokat giten míg a nagyokat külső tárhelyen tároljuk.

- Ehhez az kell hogy az index oszlop ne legyen benne és a sorvégződések egységesek legyenek. A byte azonos hash könnyen eltörhet egy sorvégződés miatt.

- A dvc pull parancsot kell futtatni

# Exercise 4

- A git checkout a dvc mutató fájl állította vissza a régi verzióra. A dvc checkout pedig ezalapján töltötte be a tényleges csv adatokat.

- A dvc checkout hibát dobna mert nincs lokális cache-ben az adott hashű file. 

# Exercise 5

- Ha például a model.pkl hiányzik a deps listából, a pipeline lefut hiba nélkül, de a DVC nem fogja észrevenni, ha a modell változott. Így az evaluate lépés nem fut le újra automatikusan, és a kimenet régi, hibás marad.

- A sorok beérkezési sorrendje eltérő a darabokban érkezett batch-eknél, mint az eredeti egyben lévő fájlnál. Az eltérő sorrend miatt máshogy történik a train-test felosztás, ami más pontosságot és metrikákat eredményez.

# Exercise 6

- Az MLflow (8 karakter) a fájl nevét és útvonalát/metaadatait hasheli, a DVC md5 (32 karakter) viszont byte-pontosan a fájl tartalmát. Az auditornak a DVC md5-öt kell adni a bizonyításhoz, az MLflow hash csak az UI gyors változáskövetéséhez jó.

