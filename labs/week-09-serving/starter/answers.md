## Exercise 5 — Kubernetes `/health`
```json
{"status":"ok","model_version":"1","run_id":"5c70d36eb50d4cfc8a25df6242ba4ab9","gate_verdict":"GO","schema_version":"1.0.0","model_source":"registry champion"}
```

## Exercise 1
### Első kérdés:
- Az alap kérés: **200**, válasz: `{"predictions": [1]}`.

	| Módosított kérés | HTTP | Válasz / hiba |
	|---|---:|---|
	| `glucose = 0` | 200 | `{"predictions": [0]}` |
	| `glucose = -50` | 200 | `{"predictions": [0]}` |
	| `age = 250`, `bmi = 336` | 200 | `{"predictions": [1]}` |
	| `cholesterol` extra oszlop | 400 | A scikit-learn `ValueError`-t adott: a `cholesterol` fitkor nem látott feature-név. |
	| `bmi` oszlop nélkül | 400 | A scikit-learn `ValueError`-t adott: a fitkor látott `bmi` feature hiányzik. |
	| Ugyanazok az oszlopok más sorrendben | 400 | A scikit-learn `ValueError`-t adott: a feature-nevek sorrendje eltér a fitkoritól. |

	A három numerikusan módosított kérést a modell pontozta. A három oszlopszerkezeti kérést a scikit-learn pipeline ellenőrzése utasította vissza.

    
### Második kérdés:
- Mindhárom pontozott, de kontraktum szerint érvénytelen kérésnek meg kellett volna állnia a modell előtt:
	- `glucose = 0` és `glucose = -50`: a `PredictionInput`/`ModelInput` kontraktus `glucose > 0` szabálya (`pa.Field(gt=0)`). A nulla sentinelérték sem érvényes mérés.
	- `bmi = 336`: a BMI felső korlátja `bmi <= 100` (`MAX_BMI`).
	- `age = 250`: az életkor felső korlátja `age <= 120` (`MAX_AGE`).

	Az extra oszlopra a kontraktus `strict = True` szabálya adna korai, érthető hibát; a hiányzó BMI-t pedig a kötelező, nem nullázható mezőként definiált szerződés utasítaná el. Az oszlopsorrend más kérdés: a serving `PredictionInput` nem követel sorrendet (`ordered = False`), ezért a szolgáltatásnak név szerint kellene a modell által várt sorrendbe rendeznie a mezőket. Az MLflow-végpont ezt nem tette meg, így a scikit-learn dobta a hibát.
### Harmadik kérdés:
- Például hitelesítés és jogosultságkezelés, hogy ne férhessen hozzá bárki az előrejelzési végponthoz.Valamint forgalomkorlátozás (rate limit vagy kvóta), hogy egy kliens ne terhelhesse túl a szolgáltatást. Ezeket a szolgáltatás köré kellene építeni.

## Exercise 3
Mérés 192 tesztsoron, két futásban: batch 0,0477 s és online 3,3831 s (71×); majd batch 0,0578 s és online 4,1621 s (72×). Nem volt sikertelen online kérés.

### Első kérdés:
- Online módban minden beteg külön TestClient/FastAPI-kérésen megy át: útvonalkezelés, Pydantic típusellenőrzés, Pandera-kontraktusellenőrzés, payloadból DataFrame építése és sorrendezése, majd a modell pipeline-ja, végül a válasz előállítása. A batch közvetlenül, egyetlen `predict_proba` hívásban pontozza az összes sort; nincs soronkénti kéréskezelés és szerződésellenőrzés.
### Második kérdés:
- **Batch:** éjszakai pontozás egy nap alatt összegyűlt beteglistán, amikor az eredmény később is felhasználható. **Online:** egy beteg adatainak pontozása egy konzultáció alatt, amikor azonnali válasz kell. A különbség az, hogy az adatok egyszerre rendelkezésre állnak-e, illetve mennyire szigorú a válaszidő.
### Harmadik kérdés:
- Az átlagot néhány lassú kérés erősen eltolhatja, és elrejti a tipikus, illetve a szélső válaszidőket. A p50 a tipikus késleltetést mutatja, a p95 pedig a lassú esetek felső részét, ezért jobban látszik belőlük a szolgáltatás késleltetési eloszlása.


## Exercise 4
### Első kérdés:
- A modell image-be másolt példányával a pod registry nélkül is elindul, és azonnal tud kiszolgálni; a /health a beépített modell verzióját és run ID-ját jelzi. A registryből induláskor letöltő image viszont nem tudná megszerezni a modellt, ezért a pod nem válna szolgálatra kész állapotúvá. A beépített modell frissítéséhez új image-et kell kiadni.
