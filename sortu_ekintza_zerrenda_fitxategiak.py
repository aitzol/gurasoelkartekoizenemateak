import csv
import os
import re
from collections import defaultdict

def sortuEkintzaFitxategiak(sarrera_fitxategi_izena, zikloa):
    """
    Google formeko datuak jaso eta ekintza bakoitzerako apuntatutakoen zerrendak sortu
    params: prozesatuko den csv fitxategiaren izena
    returns: ikasle bakoitzaren ordainketa modua
    """
    ikasle_ekintzak = defaultdict(list)
    ikasle_ordainketak = {}
    with open(sarrera_fitxategi_izena) as sarrera:
        sarrera_csv = csv.reader(sarrera)
        sarrera_csv.next()
        for ikaslea in sarrera_csv:
            data = ikaslea[0]
            izena = ikaslea[2]
            ikasmaila = ikaslea[3]
            ekintzak = ikaslea[4]
            ikasle_ordainketak[izena] = ikaslea[7]
            ekintza_lista = ekintzak.split(';')
            for ekintza in ekintza_lista:
                ikasle_ekintzak[ekintza].append((data, izena, ikasmaila))
    for ekintza, ikasleak in ikasle_ekintzak.items():
        with open(os.path.join("output","{}_{}.csv".format(ekintza, zikloa)), 'a') as ekintza_file:
            ekintza_writer = csv.writer(ekintza_file)
            for ikaslea in ikasleak:
                ekintza_writer.writerow(ikaslea)
    return ikasle_ordainketak

def sortuIkasleOrdainketaModuaFitxategia(ikasle_ordainketa_aukerak):
    """
    Ikasle bakoitzari nola kobratu behar zaion gordetzen duen csv fitxategia sortzen du
    params: ikasle bakoitzaren izena eta ordainketa modua lotzen duen hiztegia
    """
    with open(os.path.join("data","ikasle_ordainketa_modua.csv"), "w") as ordainketa_aukerak_fitxategia:
        ikasle_ordainketak_csv = csv.writer(ordainketa_aukerak_fitxategia)
        for ikasle_ordainketa in ikasle_ordainketa_aukerak.items():
            ikasle_ordainketak_csv.writerow(ikasle_ordainketa)

def borratuAurrekoFitxategiak():
    dirname = 'output'
    for filename in os.listdir(dirname):
        os.remove(os.path.join(dirname, filename))

if __name__=='__main__':
    ordainketak = {}
    zikloa_matcher = re.compile(r'(HH|LH)+')
    borratuAurrekoFitxategiak()
    for filename in os.listdir('izenemateorriak'):
        zikloa = zikloa_matcher.search(filename)
        path_osoa = os.path.join("izenemateorriak", filename)
        if zikloa:
            ordainketa = sortuEkintzaFitxategiak(path_osoa, zikloa.group(0))
            ordainketak.update(ordainketa)
    sortuIkasleOrdainketaModuaFitxategia(ordainketak)