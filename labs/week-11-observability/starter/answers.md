## Exercise 1

### Első kérdés
- Nem hagynám jóvá mert a  nyers age címke kb. 50 értéket vehet fel. A két outcome értékkel ez kb. 100 idősorozatot jelentene a jelenlegi 2 helyett. Az életkort inkább strukturált logban tárolnám és a metrikában csak előre rögzített korcsoportokat használnék.


## Exercsie 2
### Első kérdés
- Nem a p95-ök átlaga nem adja meg a teljes forgalom p95-ét. Előbb a hisztogram-bucketek sebességét kell összegezni a replikák között, majd abból számítani a kvantilist:
  `histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket{route="/predict"}[5m])))`
  Így az összes replika bucketjeiből számított p95-öt kapjuk, másodpercben. 

## Exercise 3
### Első kérdés:
- Nem fogadnám el automatikusan mert a 99,9%-os cél 30 nap alatt 43,2 perc hibakeretet ad, ami a 99%-os cél 7 óra 12 perces keretének tizede. Csak akkor vállalnám, ha ezt üzleti igény feltétlenül indokolja, és a szükséges megbízhatósági infrastruktúra is biztosított.