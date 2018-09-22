import csv
from collections import defaultdict

def loadOrdainketak(zikloa):
    ordainketak = {}
    with open('ordainketa_{}.csv'.format(zikloa), 'rU') as ordainketakFile:
        reader = csv.reader(ordainketakFile, delimiter=',')
        for lerroa in reader:
            ikaslea, ordainketa = lerroa
            ordainketak[ikaslea.lower().strip()] = ordainketa
    return ordainketak

def loadPrezioak(zikloa):
    prezioak = {}
    with open('prezioak_{}.csv'.format(zikloa), 'rU') as prezioakFile:
        reader = csv.reader(prezioakFile, delimiter=',')
        for lerroa in reader:
            ikastaroa, prezioa = lerroa
            prezioak[ikastaroa.strip()] = int(prezioa)
    return prezioak

def kalkulatuPrezioaIkasleko(zikloa):
    ikasleak = defaultdict(int)
    prezioak = loadPrezioak(zikloa)
    with open('ikasleak_{}.csv'.format(zikloa), encoding='utf-8') as ikasleakFile:
        reader = csv.reader(ikasleakFile, delimiter=',')
        for lerroa in reader:
            izena = lerroa[0].lower()
            maila = lerroa[1]
            ikastaroa = lerroa[2].strip()
            ikasleak[izena] += prezioak[ikastaroa.strip()] 
    return ikasleak

if __name__ == '__main__':
    zikloak = ('HH', 'LH')
    for zikloa in zikloak:
        ordainketak = loadOrdainketak(zikloa)
        kostua = kalkulatuPrezioaIkasleko(zikloa)
        with open('kostua_{}.csv'.format(zikloa), 'w', encoding='utf-8') as kostuakFile:
            writer = csv.writer(kostuakFile)
            for ikasle, kostu in kostua.items():
                ordainketa = ordainketak.get(ikasle.lower().strip(), '')
                writer.writerow([ikasle, kostu, ordainketa])
                print('{}\t{}'.format(ikasle, kostu, ordainketa))