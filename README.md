DESKRIBAPENA
============

Repositorio honetan [Hondar Ahua](http://hondarahua.eus) guraso elkarteak antolatzen dituen eskolaz kanpoko ekintzen izen emate orriak prozesatzeko erabiltzen diren python scriptak daude. 

Egun, guraso elkarteak, google forms bidez jasotzen ditu izen emateak, eta izen emate orrien emaitza formatuarekin oso lotuta daude script hauek. Kontutan izan hortaz datu sarreren formatua ez baldin bada egokia emaitzak ere ez direla izango.

Script hauek erabiltzeko, aldatzeko eta aztertzeko libre zara, baina zure erantzunkizunpean. 

NOLA EXEKUTATU
==============

Script hauek exekutatzeko eragiketa bakoitzaren betebeharrak asetu (ikus beherago) eta python 3 eskuragarri duen sistema batean exekutatu beharko dituzu. Horretarako zabaldu terminal bat eta exekutatu 
```
python __script_izena__
````

*Software hau MacOSx sistema batean frogatu da.

ERAGIKETAK
==========

Eskolaz kanpoko ekintzetako partaide zerrendak kalkulatu
--------------------------------------------------------

- Kodearen kopia egin ondoren, sortu script-en maila berean _input_, '_izenemateorriak_', eta _output_ direktorioak. 
- Deskargatu google forms-ak sortzen dituen csv karpertak eta gorde _izenemateorriak_ , script-ek fitxategi izenetik eratortzen dute zein ziklotako ikasleei dagozkien datuak, hortaz garrantzitsua da izenean adieraztea HH edo LH den ( adib. izendatu _izenemateaHH.csv_ eta _izenemateaLH.csv_)
- Izen emandako ikasleekin ekintza bakoitzari dagokion partaide fitxategiak sortzeko erabili __sortu_ekintza_zerrenda.py__ fitxategia
- Scriptak bukatzerakoan _output_ direktorioak ekintza + ziklo bakoitzari dagozkion fitxategiak izango dituzu
- Zerrendez gain _ikasle_ordainketa_modua.csv_ izeneko fitxategia sortuko du. Fitxatego hau BEHARREZKOA da hurrengo eragiketaren sarrera gisa.

Ikasle bakoitzari dagokion kostu eta ordainketa mota kalkulatu
--------------------------------------------------------------

- Eragiketa honen funtzionamentua aldatzen ari da.
- Bertsio honetan _ikasleak_{zikloa}.csv_ izeneko fitxategiak hartu eta prozesatzen ditu
- _data_ direktorioan ekintza bakoitzaren prezioa zehazten duen _prezioa_{zikloa}.csv_ izeneko fitxategiak behar ditu


DATU FORMATUAK
==============

Izen emate orriak
-----------------

Komaz banatutako fitxategi bat izan behar da. Hauek izan behar dira:

| izen emate data | emaila | ikaslearen izena | zikloa | ekintzak* | emaila** | telefonoa | ordainketa mota |

*ekintzak ';' karaktereaz banaturik egon behar dira
**Arrazoi historikoak medio


