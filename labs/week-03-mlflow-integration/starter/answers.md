## Exercise 4

- 1. kérdés: Nem egyezik meg. Az F1 score alapján a Random Forest a legjobb, míg a ROC-AUC alapján a Logistic Regression (C=1.0). Ez azért van, mert az F1 egyetlen, fix döntési küszöb mellett méri a modell teljesítményét. A ROC-AUC viszont a modell osztályozó képességét méri az összes lehetséges küszöbérték mentén. 

- 2. Én a 772d78eb589546009ff374b9ae752430 run_id-val rendelkező Random Forest modellt választom, mert ez egy orvosi diagnosztikai probléma, a betegek felismerése (Recall érték) kritikusabb, mint a téves riasztások elkerülése. Bár a LogReg ROC-AUC értéke minimálisan jobb, az alapértelmezett küszöbérték mellett a Random Forest jelentősen kevesebb False Negative hibát vét, amit a legmagasabb, 0.5821-es Recall érték mutat.

- 3. Például azt, hogy pontosan melyik git commit hash-ből futott a kód a betanítás pillanatában, illetve a futások pontos timestampjét és a hozzájuk tartozó konfúziós mátrix ábrákat.


## Exercise 6

# 1.
- Alias --> Version: Lekérdezem a Registry-t, hogy melyik verzióhoz van rendelve a @staging alias
- Version --> Run ID: Lekérdezzük a verzió metaadataiból a hozzá tartozó source_run_id-t
- Run ID --> Params & Git: Lekérdezzük a Tracking szerverről az adott run paramétereit és tageket
- Git commit -> Kód: Lokálisan negnézzük a Git segítségével, hogy mi volt a kód állapota

# 2.
- A második részben egy olyan kódot mutatott, ami tele volt TODO kommentekkel, vagyis ez nem az a kód volt ami valójában lefutott a tanításkor. A git_dirty rögzítése megoldotta, hogy most már tudjuk, ha a kód nem volt tiszta a commitkor.

# 3.
- Igen, vissza kéne utasítania a "dirty" kódot, a reprodukálhatóság miatt.

# 4.
- Dinamikusan hivatkozhatunk modellekre kódmódosítás nélkül
- Egy verzióhoz több alias is tartozhat egyszerre

# 5. 
- Azt jelenti, hogy tudjuk milyen kóddal és paraméterekkel tanítottuk a modellt, de azt nem hogy az adathalamz változott-e közben.


## Exercise 7

# 1.
- Csak a pointer változott meg úgy, hogy a hármas helyett újra a kettesre mutat.

# 2.
- A tagekből lehet vissza követni csak.

# 3.
- Nem, mert az ötöts feladatnál regisztráltuk, mielött commitoltunk volna, tehát ez dirty kód.