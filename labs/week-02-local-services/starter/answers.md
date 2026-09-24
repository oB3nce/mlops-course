### 4. Exercise

**Melyik tárhely milyen adatokat tárol?**
*   **Postgres (Backend Store):** Strukturált metaadatokat tárol. Ide tartoznak a kísérletek részletei, a futások azonosítói, a paraméterek, a kiértékelési metrikák  és a tagek is.
*   **MinIO (Artifact Store):** Strukturálatlan adatokat és nagy méretű fájlokat (artifact-okat) tárol. Ide tartoznak maguk a lefordított modellek (pl. `model.pkl`), a környezeti konfigurációk (`conda.yaml`, `requirements.txt`), valamint bármilyen generált grafikon vagy adathalmaz.

**Miért nem a Postgresben tároljuk a modell fájlokat?**
1. **Teljesítmény és optimalizáció:** A relációs adatbázisokat a strukturált adatok gyors lekérdezésére, indexelésére és szűrésére tervezték. A nagy bináris fájlok tárolása indokolatlanul megnöveli az adatbázis méretét, és jelentősen rontja a lekérdezések sebességét.
2. **Skálázhatóság és költségek:** Az objektumtárolókat (mint a MinIO vagy az AWS S3) kifejezetten arra találták ki, hogy hatalmas mennyiségű fájlt tároljanak olcsón, és könnyen skálázhatóak legyenek. Egy relációs adatbázis tárhelyének és memóriájának növelése gigabájtnyi modellfájlokhoz nagyon drága és nem hatékony lenne.
3. **I/O szűk keresztmetszet:** A modern gépi tanulási modellek óriásiak lehetnek. Nagy fájlok mozgatása a relációs adatbázison keresztül leterheli a rendszert, ami lelassítaná vagy akár blokkolná a többi, egyszerű metrikákat lekérdező felhasználót.


### 5. Exercise 

1. **Reprodukálhatóság:** Az 1. héten, ha eltűnt a terminál előzménye, elvesztek a paraméterek, amikkel az adott eredményt elértük. Most minden egyes futáshoz pontosan rögzítve van, milyen beállításokat (pl. `random_seed=7` vagy `42`) használtunk, így bármikor hajszálpontosan újra tudjuk alkotni ugyanazt a modellt.
2. **Összehasonlíthatóság:** A terminálban manuálisan, fel-le görgetve kellett volna összehasonlítani a metrikákat. Az MLflow felületén a különböző kísérleteket kijelölve egyszerűen, egymás mellett láthatjuk, hogy az adott paraméterváltoztatás hogyan hatott a metrikákra.
3. **Megoszthatóság:** Nem csak egy kimásolt szöveget tudunk elküldeni a csapattársaknak, hanem egy konkrét linket a kísérletről. Ezen a linken keresztül a többiek nemcsak a metrikákat látják, hanem hozzáférnek a betanított modellhez és a pontos Python környezeti követelményekhez is, amit azonnal le is tudnak tölteni.