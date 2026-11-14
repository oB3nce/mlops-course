## Exercise 2

### Első kérdés
- Promóció: a jel az ellenőrzések hibamentessége legkorábban 24 óra után dönthetünk. Visszaállítás bármely smoke check hibája már az első smoke futás után. Valódi diagnózis nincs a kérésekhez címkézve, ezért csak közvetett jeleket figyelünk.
### Második kérdés
- 10% × 300 = napi 30 beteg. Ez kevés annak bizonyítására, hogy v2 jobb v1-nél, de a durva hibák és a terhelési problémák észlelésére alkalmas.
### Harmadik kérdés
- A választott küszöb 0,1. v3 spreadje 0,1754, ezért 0,1754-nél nagyobb küszöb, például 0,2, már elbukik rajta v2 spreadje 0,71. A v2 spreadjéhez közeli küszöb túl szigorú lenne, és egy jó modellt is elutasíthatna kisebb eltérés esetén.

## Exercise 3 

### Első kérdés
- A 200 kérés csak minta, ezért a véletlen eltérés miatt lett 11% a beállított 10% helyett. Ez belefér a ±2,1 százalékpontos (1 szórásnyi) tartományba. 1 százalékpontos szóráshoz kb. 900 kérés kell, 95%-os megbízhatósághoz kb. 3500.

## Exercise 4
### Első kérdés
- Elbukott az identity.gate (NO-GO) és a behaviour.positive_is_positive (a beteg pozitív helyett negatív predikciót kapott). Átment az identity.health, identity.version, contract.illegal_rejected, behaviour.negative_is_negative, behaviour.not_a_constant és protocol.v1_agrees. Ha csak egy maradhatna, a viselkedésellenőrzést tartanám meg mert ez a tényleges predikciót vizsgálja, nem csak a modell metaadatait.

## Exercise 5
### Első kérdés
- A make rollback a forgalmat állította vissza: v1 100%, v3 0% (a v3 pod Ready maradt). Az MLflow aliashoz nem nyúlt; annak jelenlegi célja MLflow-kiesés miatt nem ellenőrizhető. A metrics/baseline.json week-5-ös referenciaértékeit és a DVC-adat hash-ét sem állította vissza. A v3 által már adott válaszokat sem lehet visszavonni: a pozitív betegre 0-t adott (p=0,4751).
### Második kérdés
- 1. make rollback: v3 forgalma 0% (tesztelve, kb. 5,9 mp). 
- 2. make isvc-status és make isvc-health: v1 100%, v3 0%, az endpoint v1-et szolgál (tesztelve). 
- 3. Ha a teljes konfigurációt is vissza kell állítani, a make rollback-reapply parancsot kell futtatni de ezt nem teszteltük.