import csv
from collections import defaultdict
import re
import os

INPUT_FILES = './input/'
OUTPUT_FILES = './output/'
DATA_FILES = './data/'

def loadOrdainketak():
    ordainketak = {}
    with open(os.path.join(DATA_FILES, 'ikasle_ordainketa_modua.csv'), 'rU') as ordainketakFile:
        reader = csv.reader(ordainketakFile, delimiter=',')
        for lerroa in reader:
            ikaslea, ordainketa = lerroa
            ordainketak[ikaslea.lower().strip()] = ordainketa
    return ordainketak

def loadPrezioak(zikloa):
    prezioak = {}
    with open(os.path.join(DATA_FILES, 'prezioak_{}.csv'.format(zikloa)), 'rU') as prezioakFile:
        reader = csv.reader(prezioakFile, delimiter=',')
        for lerroa in reader:
            ikastaroa, prezioa = lerroa
            prezioak[ikastaroa.strip()] = int(prezioa)
    return prezioak

def kalkulatuPrezioaIkasleko(zikloa):
    ikasleak = defaultdict(int)
    prezioak = loadPrezioak(zikloa)
    with open(os.path.join(OUTPUT_FILES, 'ikasleak_{}.csv'.format(zikloa)), encoding='utf-8') as ikasleakFile:
        reader = csv.reader(ikasleakFile, delimiter=',')
        for lerroa in reader:
            izena = lerroa[1].lower()
            maila = lerroa[2]
            ikastaroa = lerroa[3].strip()
            ikasleak[izena] += prezioak[ikastaroa.strip()] 
    return ikasleak

def osatu_ikasle_fitxategia(zikloa):
    filename_pattern = re.compile(r'(.*)_{}.csv'.format(zikloa))
    ikasleak_data = []
    for root, dirs, files in os.walk(INPUT_FILES):
        for file in files:
            match = filename_pattern.match(file)
            if match:
                with open(os.path.join(root,file), 'r') as fitxategia:
                    reader = csv.reader(fitxategia, delimiter=',')
                    for row in reader:
                        ikasleak_data.append(row)              
    with open(os.path.join(OUTPUT_FILES, 'ikasleak_{}.csv'.format(zikloa)), 'w') as outputfile:
        writer = csv.writer(outputfile)
        for row in ikasleak_data:
            writer.writerow(row)

def parse_ordainketa(ordainketa_string):
    fixed = 'Guraso elkarteko bazkidetza kuota odaintzen den kontu berdinetik.'
    epeak = 1
    if ordainketa_string:
        matcher = re.compile(r'{} (?P<ordainketa_epeak>.*)'.format(fixed))
        match = matcher.match(ordainketa_string)
        ordainketak = match.group('ordainketa_epeak')
        if 'Hiru' in ordainketak:
            epeak = 3
        elif 'Bi' in ordainketak:
            epeak = 2
    return fixed, epeak 

if __name__ == '__main__':
    zikloak = ('HH', 'LH')
    ordainketak = loadOrdainketak()
    for zikloa in zikloak:
        osatu_ikasle_fitxategia(zikloa)
        kostua = kalkulatuPrezioaIkasleko(zikloa)
        with open('kostua_{}.csv'.format(zikloa), 'w', encoding='utf-8') as kostuakFile:
            writer = csv.writer(kostuakFile)
            for ikasle, kostu in kostua.items():
                ordainketa_testua, epea = parse_ordainketa(ordainketak.get(ikasle.lower().strip(), '')) 
                writer.writerow([ikasle, kostu, ordainketa_testua, epea])
                print('{}\t{}\t{}\t{}'.format(ikasle, kostu, ordainketa_testua, epea))
