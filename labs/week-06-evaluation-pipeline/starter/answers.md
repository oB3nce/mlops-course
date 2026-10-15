## Exercise 2

###  Első kérdés:

- A modell az 50+ korcsoporton a legrosszabb. Itt a ROC AUC 0.6071, ami 0.2274-gyel alacsonyabb a 0.8345-ös összesített értéknél. Az F1 pedig 0.1341-gyel marad el az átlagtól. Emellett az FPR több mint hatszorosa a 21-29-es korcsoportnak.
- Ebben csak korlátozottan bízhatunk, mert a csoport elemszáma nagyon kicsi (19)

### Második kérdés:

- A kiértékelésnél ezt a csoportot az alacsony létszám miatt kihagyott állapotra kell állítani, hogy ne blokkolja a modell kiadását.
- Több adatra lenne szükség ebből a korosztályból.

### Harmadik kérdés:

- A két metrika mást mér szóval mindkettő lehet helyes. A ROC AUC = 1.0000 azt jelenti, hogy a modell az egyetlen pozitív páciensnek magasabb becsült valószínűséget adott, mint a 29 negatív páciens bármelyikének.
- Ez azt árulja el a csoportról, hogy a betegség előfordulása itt rendkívül alacsony (1/30 = 3.3%), ezért a modell jól kalibráltan alacsony alap-valószínűségeket rendel a csoporthoz, továbbá az egyetlen pozitív eset miatt az F1 metrika itt nem alkalmas a modell minőségének megítélésére

## Exercise 4

### Első kérdés:
- Az 5. héten az adat-gate a pipeline elején volt: ha fail-elt a prepare és a train fázis, le sem futott, így nem jött létre modellfájl. A modell-gate viszont a DVC DAG utolsó csomópontja, amely a train és az evaluate után fut le, tehát mire a gate NO-GO-val megáll, a models/model.pkl fájl és az MLflow futás már létezik és nincs további DVC stage, ami függne tőle.

### Második kérdés:
- Ha a register nem ellenőrizné a require_go-t, akkor egy NO-GO ítélet ellenére is gond nélkül felvehetnénk a hibás modellt az MLflow Model Registry-be.
- Ha a promote sem ellenőrizné, a gyenge modell egyenesen kikerülne Staging/Production környezetbe, és csak az orvosok, a páciensek vagy egy utólagos monitoring venné észre.

### Harmadik kérdés:
- Mindkét szám matematikailag helyes, de más kérdésre válaszol: az erős regularizáció (C: 0.005) kisimította a modellt, így a páciensek kockázati sorbarendezése (ROC AUC) kissé javult (0.8345 -> 0.8427), ugyanakkor a becsült valószínűségeket a 0.5-ös küszöb alá nyomta, így a 0.5-ös küszöb melletti bináris osztályozás (F1) összeomlott (0.6341 -> 0.5243).
- Ahhoz, hogy tudjuk, melyik számít, ismernünk kell, hogyan használják a modellt a gyakorlatban: ha a rendszer a nyers valószínűségek alapján rangsorol, akkor a ROC AUC a mérvadó, ha viszont a rendszer a 0.5-ös küszöbnél automatikus igen/nem döntést hoz, akkor az F1 a helyes mutató.

## Exercise 5

### Első kérdés:
- A demográfiai paritás csak akkor elvárható, ha a célváltozó valós előfordulása megegyezik a csoportok között, vagy ha a különbség történelmi torzításból fakad. A cukorbetegség előfordulása azonban biológiai okokból erősen függ az életkortól. Teljesen indokolt és kívánatos, hogy a modell gyakrabban jelezzen pozitívat abban a korcsoportban, ahol a betegség több mint kétszer olyan gyakori.

### Második kérdés:
- Egyrészt statisztikai okból, az age_band 4 részcsoportra vágja az adatokat, így egy-egy korcsoportban kevesebb a pozitív eset (jelen esetben pontosan: 7, 17, 21, 22 fő), ami nagyobb mintavételi szórást eredményez a szélsőértékek különbségében mint a 2 nagyobb csoportból álló insulin_missing (42 és 25 pozitív eset ebben a példában) esetén. Másrészt a korcsoportok között a betegség klinikai megjelenése és alap-valószínűsége is erősebben eltér, ami fix 0.5-ös küszöbnél természetes ingadozást okoz a TPR-ben.