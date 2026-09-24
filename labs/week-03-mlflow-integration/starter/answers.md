## Exercise 4

- 1. kérdés: Nem egyezik meg. Az F1 score alapján a Random Forest a legjobb, míg a ROC-AUC alapján a Logistic Regression (C=1.0). Ez azért van, mert az F1 egyetlen, fix döntési küszöb mellett méri a modell teljesítményét. A ROC-AUC viszont a modell osztályozó képességét méri az összes lehetséges küszöbérték mentén. 

- 2. Én a 772d78eb589546009ff374b9ae752430 run_id-val rendelkező Random Forest modellt választom, mert ez egy orvosi diagnosztikai probléma, a betegek felismerése (Recall érték) kritikusabb, mint a téves riasztások elkerülése. Bár a LogReg ROC-AUC értéke minimálisan jobb, az alapértelmezett küszöbérték mellett a Random Forest jelentősen kevesebb False Negative hibát vét, amit a legmagasabb, 0.5821-es Recall érték mutat.

- 3. Például azt, hogy pontosan melyik git commit hash-ből futott a kód a betanítás pillanatában, illetve a futások pontos timestampjét és a hozzájuk tartozó konfúziós mátrix ábrákat.