## Exercise 2

### Első kérdés:
- A legjobb megoldás ha a validáció elött dropoljuk ezt az oszlopot, amennyiben nics rá szükségünk.
### Második kérdés:
- Sor: — (nincs konkrét sor), Oszlop: notes, Rossz érték: maga az oszlop létezése (a séma nem ismeri).

- Sor: 3, Oszlop: glucose, Rossz érték: "unknown" (szöveg egy szám oszlopban).

- Sor: 7, Oszlop: age, Rossz érték: 250 (irreálisan magas életkor).

- Sor: 23, Oszlop: bmi, Rossz érték: 280.0 (irreálisan magas BMI, átlépi a 100-as limitet).

- A 3. sorban lévő "unknown" szöveges érték a glucose oszlopban kaszkádoló hibát (láncreakciót) okozott, ami önmagában 4 sort generált a jelentésben:

## Exercise 4

### Első kérdés:
- Mielőtt a validációs kaput beépítettük volna a pipeline-ba, az age = 250 hibás sor gond nélkül átjutott a rendszeren, és bekerült a train.csv és test.csv fájlokba (ezt onnan tudjuk, hogy az MD5 hash megváltozott).
Ezeket az adatokat ezután a train és az evaluate lépések, illetve maga a gépi tanulási modell használta volna fel. Tehát a modell egy lehetetlenül magas életkort tartalmazó adaton tanult volna.

### Második kérdés:
- A prepare szkript hibával leáll, és megtagadja az adatok feldolgozását. Amit a src/week_05_data_validation/pipeline.py fájlban a prepare függvény elejére beírt ellenőrzés (ami beolvassa a reports/validation.json fájlt, és megnézi, hogy a teszt "PASS" volt-e) okoz. A dvc.yaml csak akkor védi meg a pipeline-t, ha a DVC-n keresztül indítjuk a folyamatot (dvc repro paranccsal). Ha egy csapattag siet, és közvetlenül a Python szkriptet futtatja (uv run python src/main.py prepare), azzal megkerüli a DVC-t. Ezért van szükség arra, hogy maga a Python kód is ellenőrizze az előző lépés kimenetét.

### Harmadik kérdés:
- Csak a validate lépés fog lefutni. A prepare, train és evaluate lépések kimaradnak. Azért mert a MAX_AGE átírásával megváltoztattuk a sémát definiáló kódot, ezért a DVC tudja, hogy a validate lépést újra kell futtatnia. Mivel azonban a bemeneti adat nem változott (nincs ugye benne 120 feletti életkor), a validate lépés sikeres lesz, és az általa generált validation.json fájl tartalma pontosan ugyanaz marad, mint előtte volt. Így a model nem tanult újra. Mivel a prepare bemenetei (measurements.csv és a validation.json) hash-szinten nem változtak, a DVC okosan felismeri, hogy felesleges tovább menni, így a modell újratanítását és a kiértékelést átugorja.