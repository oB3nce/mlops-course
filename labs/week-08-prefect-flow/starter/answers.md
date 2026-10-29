## Exercise 2 

### Első kérdés:
- A Prefect futási előzményeket, taskonkénti állapotokat és időtartamokat, valamint ütemezést és újrapróbálkozást ad. A DVC ezekről nem gondoskodik. Cserébe a DVC tartalomhash-ek alapján eldönti, mely pipeline-szakaszok elavultak, és melyeket kell újrafuttatni; ezt a Prefect önmagában nem tudja.
### Második kérdés:
- Ha a DVC-szakaszokat külön Prefect taskokra bontanánk, két ütemező kezelné ugyanazt a függőségi gráfot: a Prefect elveszíthetné a DVC teljes tartalom- és cache-információját, emiatt hibásan futtathatna vagy hagyhatna ki szakaszokat. Bontás akkor indokolt, ha a lépések önálló szolgáltatásokat vagy eltérő infrastruktúrát igényelnek, és a függőségeket, cache-elést már nem a DVC-re bízzuk.

## Exercise 5
### Első kérdés:
- A build_dataset és a write_params lefutott, a run_pipeline a validate szakasznál megbukott, a verify_params_applied nem indult el, a notify lefutott a flow Failed állapotban ért véget.

### Második kérdés:
- A hiba pillanatában a hibás sort tartalmazó nyers batch és az abból újraépített, 769 soros measurements.csv volt lemezen, továbbá a sikertelen validáció jelentése és a FAILED értesítés. Új modell, kiértékelési metrika vagy gate-eredmény nem készült a korábbi modell és pipeline-kimenetek maradtak meg.

### Harmadik kérdés:
- A dvc repro újra megpróbálta volna a validate szakaszt, mert a hibás adathalmaz eltért a korábbi sikeres futás bemenetétől ugyanaz a lehetetlen sor ismét megbuktatta volna a validációt, így a későbbi szakaszok nem futnak le.

### Negyedik kérdés:
- Igen, a notify lefutott, és a reports/last_run.txt fájlba rögzítette a FAILED állapotot. Nélküle a jelentésből nem derült volna ki egyértelműen, hogy a futás meghiúsult, a Prefect előzményeit és naplóit kellett volna külön megkeresni.

## Exercise 6
A UI-ban ellenőrzött ütemezett futás neve lilac-groundhog, végállapota Failed; a run_pipeline feladat hibázott a train szakasznál (dvc repro 255-ös kilépés), a notify lefutott.

### Első kérdés:
- Nem. A GO szükséges, de nem elég: kiadás előtt kell emberi jóváhagyás, független validáció (például holdout/árnyékfutás), fokozatos bevezetés és visszaállítási terv.
### Második kérdés:
- A modellért és az üzemeltetésért felelős csapat kapjon értesítést sikerről és hibáról is, a futás nevével, állapotával, gate-eredményével és a szükséges teendőkkel.
### Harmadik kérdés:
- A második egymást követő hiba már eszkalálódjon az ügyeletesnek, és állítsuk le az automatikus kiadást vagy további próbálkozásokat a kivizsgálásig; az első lehet átmeneti hiba.
### Negyedik kérdés:
- Ha a serve-folyamat vagy Prefect szerver leáll, illetve a deployment ütemezése nem indít futást, a flow és annak notify feladata sem fut le; ezt külső heartbeat- vagy schedule-watchdognak kell jeleznie.